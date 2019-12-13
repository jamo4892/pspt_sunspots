"""
This script runs find_pspt_fits_images_sunspots.py on all 3 image filters. It is not a function so there are no inputs.
After running the script to find the sunspots as a function of time, it plots the sunspot number vs. time for each
filter. A screenshot of the plot is saved to the working directory.
"""

import find_pspt_fits_images_sunspots
import numpy as np
import matplotlib.pyplot as plt
import os
# Import modules.

red_sunspots = []
red_year = []
red_month = []
blue_sunspots = []
blue_year = []
blue_month = []
calcium_sunspots = []
calcium_year = []
calcium_month = []
# Lists for sunspot number and timestamps.

red_directory = './PSPTRedImages/FITS/'
blue_directory = './PSPTBlueImages/FITS/'
calcium_directory = './PSPTCalciumImages/FITS/'
# Assign FITS image directory based on filter.
    
red_image_files = os.listdir(red_directory)
red_fits_file = np.arange(len(red_image_files))
blue_image_files = os.listdir(blue_directory)
blue_fits_file = np.arange(len(blue_image_files))
calcium_image_files = os.listdir(calcium_directory)
calcium_fits_file = np.arange(len(calcium_image_files))
# Find all FITS images in the directories.

for fits_file in red_image_files:
    # Loop over all FITS images in the directory.
    
    sunspot_data = find_pspt_fits_images_sunspots(fits_file, red_directory)
    # Run the sunspot function on the image.
    
    red_sunspots.append(sunspot_data[0])
    red_year.append(sunspot_data[1])
    red_month.append(sunspot_data[2])
    # Add to sunspot number, year and month lists.

red_sunspots = np.array(red_sunspots)
red_date = list(zip(red_year, red_month))
# Make arrays of the red sunspot & date lists.

plt.figure(figsize=(20,12))
plt.plot(red_sunspots, 'r')
plt.ylabel('# of Sunspots')
plt.xlabel('Image')
plt.title('PSPT Red Filter (607.097nm) Sunspots')
plt.savefig('./pspt_red_sunspots.png', bbox_inches = 'tight')
# Plot red sunspot number vs. time. 

for fits_file in blue_image_files:
    # Loop over all FITS images in the directory.
    
    sunspot_data = find_pspt_fits_images_sunspots(fits_file, blue_directory)
    # Run the sunspot function on the image.
    
    blue_sunspots.append(sunspot_data[0])
    blue_year.append(sunspot_data[1])
    blue_month.append(sunspot_data[2])
    # Add to sunspot number, year and month lists.

blue_sunspots = np.array(blue_sunspots)
blue_date = list(zip(blue_year, blue_month))
# Make arrays of the blue sunspot & date lists.

plt.figure(figsize=(20,12))
plt.plot(blue_sunspots, 'b')
plt.ylabel('# of Sunspots')
plt.xlabel('Image')
plt.title('PSPT Blue Filter (409.412nm) Sunspots')
plt.savefig('./pspt_blue_sunspots.png', bbox_inches = 'tight')
# Plot blue sunspot number vs. time. 

for fits_file in calcium_image_files:
    # Loop over all FITS images in the directory.
    
    sunspot_data = find_pspt_fits_images_sunspots(fits_file, calcium_directory)
    # Run the sunspot function on the image.
    
    calcium_sunspots.append(sunspot_data[0])
    calcium_year.append(sunspot_data[1])
    calcium_month.append(sunspot_data[2])
    # Add to sunspot number, year and month lists.

calcium_sunspots = np.array(calcium_sunspots)
calcium_date = list(zip(calcium_year, calcium_month))
# Make arrays of the calcium sunspot & date lists.

plt.figure(figsize=(20,12))
plt.plot(calcium_sunspots, 'g')
plt.ylabel('# of Sunspots')
plt.xlabel('Image')
plt.title('PSPT Calcium Filter (393.416nm) Sunspots')
plt.savefig('./pspt_calcium_sunspots.png', bbox_inches = 'tight')
# Plot calcium sunspot number vs. time. 
