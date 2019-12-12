"""
This script opens a PSPT blue FITS image and plots two image views- 1 plot with a spectral image color scale,
 and 1 plot with a gray color scale. The grayscale is the same color map as the JPG images that accompany each 
FITS image. Additionally, the grayscale image shows the 'window' that is used to mask out the sun before 
identifying the sunspots.

This script is not a function- it has no inputs. The script saves a screenshot of the plot.
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import os
# Import modules.

image = fits.open('./PSPTBlueImages/FITS/20110131.1812.HW.B.P.rdc.fits.gz')
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
    
f, axis = plt.subplots(1, 2, figsize = (20, 10))
# Plot 2 different views of the FITS image.

plt.subplot(1, 2, 1)
plt.imshow(pspt, cmap = 'nipy_spectral')
plt.colorbar(shrink = 0.75)
plt.xlabel('X (Pixels)')
plt.ylabel('Y (Pixels)')
plt.title(np.str(year) + '/' + np.str(month) + '/' + np.str(day) + ' ' + np.str(hour) + ':' + np.str(minute) \
          + ' UT ' + im_filter + '@' + np.str(im_wavelength) + 'nm')
# Spectral image plot.

plt.subplot(1, 2, 2)
plt.imshow(pspt, cmap = 'gray')
plt.colorbar(shrink = 0.75)
plt.xlabel('X (Pixels)')
plt.ylabel('Y (Pixels)')
plt.title(np.str(year) + '/' + np.str(month) + '/' + np.str(day) + ' ' + np.str(hour) + ':' + np.str(minute) \
          + ' UT ' + im_filter + '@' + np.str(im_wavelength) + 'nm')
plt.axhline(solar_disk_max_y, color = 'r')
plt.axhline(solar_disk_min_y, color = 'r')
plt.axvline(solar_disk_min_x, color = 'r')
plt.axvline(solar_disk_max_x, color = 'r')
# Grayscale image plot (same coloring as the jpg).

plt.savefig('./blue_image.png', bbox_inches = 'tight')

plt.plot(pspt[875, :])
plt.xlabel('X Pixel @ Y = ' + np.str(875))
plt.ylabel('FITS Array Brightness')
plt.title(np.str(year) + '/' + np.str(month) + '/' + np.str(day) + ' ' + np.str(hour) + ':' + np.str(minute) \
          + ' UT ' + im_filter + '@' + np.str(im_wavelength) + 'nm')
plt.axhline(2200, color = 'g')
plt.axhline(1800, color = 'g')
plt.axvline(solar_disk_min_x, color = 'r')
plt.axvline(solar_disk_max_x, color = 'r')
plt.savefig('./blue_slice.png', bbox_inches = 'tight')
