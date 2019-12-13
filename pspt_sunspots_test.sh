test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# There are pycodestyle tests on my code. I didn't have time to do this.

# There are no unit tests on my code. I didn't have time to write these.

run data_distribution_test python pspt_data.py
assert_no_stderr
assert_exit_code 0
# Run script to make data distribution plot.

# The tests below may fail if Python can't find the astropy library. I thought this was a standard 
# library but this may not be the case. If the astropy library isn't found, none of the tests below
# will run to completion and no plots will be made.

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
