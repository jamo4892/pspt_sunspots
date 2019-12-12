import numpy as np
from astropy.io import fits
import os
# Import modules.

def find_pspt_fits_images_sunspots(image, directory):
    """
    Purpose
    -------
    This function opens a PSPT FITS image, parses the header and scans the FITS image array for sunspot pixels.
    
    Inputs
    ------
    Image: string
    Filename of FITS file to analyze. The function loops over each image.
    
    Directory: string
    Path to directory of PSPT images of 1 filter.
    
    Outputs
    -------
    Array
    Array containing the sunspot number on each day, the year of each day and the month of each day. Each image has 
    each of the 3 values.
    """
        
    image = fits.open(directory + fits_file)
    # Open FITS file with astropy.

    hdr = image['primary'].header
    # Image header.

    pspt = image['primary'].data
    # FITS array is image data.

    im_filter = image['primary'].header['OBS_TYPE']
    # Image filter type.

    im_wavelength = image['primary'].header['WAVELNTH']
    # Image wavelength.

    starttime = hdr['DATE_END']
    start_year = starttime[0:4]
    start_month = starttime[5:7]
    start_day = starttime[8:10]
    start_hour = starttime[11:13]
    start_minute = starttime[14:16]
    # Observation start timestamp. These are string elements of the entire timestamp string.

    stoptime = hdr['DATE_OBS']
    stop_year = stoptime[0:4]
    stop_month = stoptime[5:7]
    stop_day = stoptime[8:10]
    stop_hour = stoptime[11:13]
    stop_minute = stoptime[14:16]
    # Observation end timestamp. These are string elements of the entire timestamp string.
    print(stoptime)

    year = np.int(np.mean([np.int(start_year), np.int(stop_year)]))
    month = np.int(np.mean([np.int(start_month), np.int(stop_month)]))
    day = np.int(np.mean([np.int(start_day), np.int(stop_day)]))
    hour = np.int(np.mean([np.int(start_hour), np.int(stop_hour)]))
    minute = np.int(np.mean([np.int(start_minute), np.int(stop_minute)]))
    # Average start/stop year, month, day, hour, minute to create a timestamp for the image used in graphing/array indexing.

    dark1 = image['primary'].header['DARK01']
    dark2 = image['primary'].header['DARK02']
    dark3 = image['primary'].header['DARK03']
    dark4 = image['primary'].header['DARK04']
    dark = np.mean([dark1, dark2, dark3, dark4])
    # Average value of dark pixels in the image. The header reports the average dark value by quadrant. The image must be
    # corrected to remove the sky behind the sun.

    dark_subtracted_image = pspt - dark
    # Dark-subtract the image.

    sun_radius_km = 696000.0
    sun_area_km = np.pi * np.square(sun_radius_km)
    # Solar radius & area in km.

    sunspot_radius_km = 5000.0
    sunspot_area_km = np.pi * np.square(sunspot_radius_km)
    # Sunspot radius & area in km. I am choosing an average value (~order of magnitude) for the sunspot radius.

    sunspot_fraction_km = sunspot_area_km / sun_area_km
    # Fractional area of 1 sunspot to total solar disk in km^2.

    sun_radius_x = int(round(image['primary'].header['XRADIUS']))
    sun_radius_y = int(round(image['primary'].header['YRADIUS']))
    sun_radius_pixels = np.mean([sun_radius_x, sun_radius_y])
    sun_area_pixels = np.pi * np.square(sun_radius_pixels)
    # X and Y solar disk radii are defined in the image header. Average the two radii, then find the area of the 
    # solar disk in pixels^2.

    km_per_pixel = sun_radius_km / sun_radius_pixels
    # km/pixel value, taken from the solar radius.

    sunspot_radius_pixels = sunspot_radius_km / km_per_pixel
    sunspot_area_pixels = np.pi * np.square(sunspot_radius_pixels)
    # Sunspot radius & area in pixels.

    sunspot_fraction_pixels = sunspot_area_pixels / sun_area_pixels
    # Fractional area of 1 sunspot to total solar disk in pixels^2.

    xcenter = int(round(image['primary'].header['CENTER_X']))
    ycenter = int(round(image['primary'].header['CENTER_Y']))
    # X & Y solar disk center pixel positions.

    xsize = np.arange(image['primary'].header['NAXIS1'])
    ysize = np.arange(image['primary'].header['NAXIS2'])
    # X and Y image dimensions.

    solar_disk_min_x = xcenter - sun_radius_x
    solar_disk_max_x = xcenter + sun_radius_x
    solar_disk_min_y = ycenter - sun_radius_y
    solar_disk_max_y = ycenter + sun_radius_y
    # X and Y radial edge pixel positions of the solar disk.

    sunspot_upper = np.where(dark_subtracted_image[solar_disk_min_x:solar_disk_max_x, solar_disk_min_y:solar_disk_max_y] \
                             < 2200.0)
    sunspot_intermediate = dark_subtracted_image[sunspot_upper]
    sunspots = np.where(sunspot_intermediate > 1800.0)
    # Sunspot pixels (brightness below a certain value).
    
    sunspot_area_pixels = len(sunspots[0])
    # Total area in pixels^2 of identified sunspot pixels- assume the sunspots are a 1xn pixel 'box' on the solar disk.

    all_sunspot_fraction_pixels = sunspot_area_pixels / sun_area_pixels
    # Fractional area of all identified sunspots to total solar disk in pixels^2.

    sunspot_number = int(round(all_sunspot_fraction_pixels / sunspot_fraction_pixels))
    return sunspot_number, year, month
    # Return sunspot number, year and month values.
