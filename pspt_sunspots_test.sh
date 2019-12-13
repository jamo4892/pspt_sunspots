test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# There are pycodestyle tests on my code. I didn't have time to do this.

# There are no unit tests on my code. I didn't have time to write these.

run data_distribution_test python pspt_data.py
assert_no_stderr
assert_exit_code 0
# Run script to make data distribution plot.

run red_image_test python plot_pspt_red_image.py
assert_no_stderr
assert_exit_code 0
# Run script to make red image plots.

run blue_image_test python plot_pspt_blue_image.py
assert_no_stderr
assert_exit_code 0
# Run script to make blue image plots.

run calcium_image_test python plot_pspt_calcium_image.py
assert_no_stderr
assert_exit_code 0
# Run script to make calcium image plots.

run sunspot_test python plot_pspt_sunspots.py
assert_no_stderr
assert_exit_code 0
# Run scripts to make red, blue & calcium sunspot plots.
# This script is not working. My code is not running find_pspt_fits_images_sunspots.py the correct way.
