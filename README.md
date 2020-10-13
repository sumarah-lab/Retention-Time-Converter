# Retention-Time-Converter

## About RTC
Retention Time Converter is an open-source software for converting retention times in csv data files. The goal of this python tool and application is to provide an easy-to-use utility for retention time conversions. With this tool you may convert the retention times within any csv data to simulate if it was run under differing conditions, columns, or lengths of times. It is also useful for converting retention times to retention indices or even retention indices to retention times. This tool requires a reference file with the retention times of standard compounds run at the varying conditions.

## How to Use

A reference file in 'csv' format is required in order to convert retention times. For an example see the included reference file: 'reference.csv'. The first column should contain the values of the index or the retention times of the standard compounds in the run you are converting your retention times to. The second column contains the retention times or retention indicies of the same compounds but within the run you wish to convert from. In this way you may convert retention indices to retention times or retention times to retention indices depending on which column the values are placed.

Simply run the script at the command line or use the included .exe file to load up the tool. Keep in mind running the .exe file may take some time to load as it has to compile the code. It is included for those who wish to not use the command line. Simply browse to the locations of your reference file, your unconverted csv file, and the location/name of where you want to save your converted file. Click convert and wait until confirmation of conversion.

## How it works
RTC generates a cubic spline function using the Akima1DInterpolator from the scipy package. See https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.interpolate.Akima1DInterpolator.html for more details. Simply put a curve is drawn through the points in the reference file using the retention times for the given standard compounds as the x and y coordinates. This curve can then be used to convert retention times from one run to another run under differing conditions. 

Note that this interpolator is only used for precise data and the curve will only pass through the specified points exactly. As such, interpolating past the given standards will given inaccurate results. Therefore, files will only be converted within the given retention times of the standard compounds.
