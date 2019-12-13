"""
This script bins the PSPT image data by hourly UT timestamp (e.g., images with a timestamp of 1500-1559 hours UT, 
etc.) and makes a bar graph of the resulting distribution. This plot is then used to select the hour with the most
images in each filter. The selected data is then used in the analysis.
"""

import numpy as np
import matplotlib.pyplot as plt
# Import modules.

pspt_blue_image_amounts = [253, 5693, 8937, 1870, 447, 523, 386, 363, 307, 281, 76, 1]
pspt_blue_image_times = ['1600', '1700', '1800', '1900', '2000', '2100', '2200', '2300', '0000', '0100', '0200', \
                         '0300']
# Number of blue images in each UT hour timestamp.

pspt_red_image_amounts = [250, 5726, 8845, 1835, 496, 524, 376, 307, 263, 223, 53]
pspt_red_image_times = ['1600', '1700', '1800', '1900', '2000', '2100', '2200', '2300', '0000', '0100', '0200']
# Number of red images in each UT hour timestamp.

pspt_calcium_image_amounts = [435, 9320, 14631, 3112, 766, 943, 748, 721, 613, 531, 109, 3]
pspt_calcium_image_times = ['1600', '1700', '1800', '1900', '2000', '2100', '2200', '2300', '0000', '0100', '0200', \
                            '0300']
# Number of calcium images in each UT hour timestamp.

f, axis = plt.subplots(3, 1, figsize = (40, 50))
# Subplotting parameters.

x = np.arange(0, len(pspt_blue_image_times))
plt.subplot(3, 1, 1)
plt.bar(x, pspt_blue_image_amounts, width = 0.5, color = 'blue', align = 'center')
plt.xticks(x, pspt_blue_image_times, fontsize = 30)
plt.yticks(fontsize = 30)
plt.xlabel('UT Hour Range', fontsize = 35)
plt.ylabel('# of Images', fontsize = 35)
plt.title('PSPT Blue Image Temporal Distribution\n ', fontsize = 40)
plt.margins(0.01, 0.01)
plt.subplots_adjust(hspace = 0.25)
# Plot blue image distribution.

x = np.arange(0, len(pspt_red_image_times))
plt.subplot(3, 1, 2)
plt.bar(x, pspt_red_image_amounts, width = 0.5, color = 'red', align = 'center')
plt.xticks(x, pspt_red_image_times, fontsize = 30)
plt.yticks(fontsize = 30)
plt.xlabel('UT Hour Range', fontsize = 35)
plt.ylabel('# of Images', fontsize = 35)
plt.title('PSPT Red Image Temporal Distribution\n ', fontsize = 40)
plt.margins(0.01, 0.01)
plt.subplots_adjust(hspace = 0.25)
# Plot red image distribution.

x = np.arange(0, len(pspt_calcium_image_times))
plt.subplot(3, 1, 3)
plt.bar(x, pspt_calcium_image_amounts, width = 0.5, color = 'gold', align = 'center')
plt.xticks(x, pspt_calcium_image_times, fontsize = 30)
plt.yticks(fontsize = 30)
plt.xlabel('UT Hour Range', fontsize = 35)
plt.ylabel('# of Images', fontsize = 35)
plt.title('PSPT Calcium Image Temporal Distribution\n ', fontsize = 40)
plt.margins(0.01, 0.01)
plt.subplots_adjust(hspace = 0.25)
# Plot calcium image distribution.

plt.savefig('./pspt_data_distribution.png', bbox_inches = 'tight')
