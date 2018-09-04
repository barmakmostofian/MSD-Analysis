# MSD-Analysis

This analysis computes the two-dimensional mean-square displacement (MSD) as a function of time intervals, &tau;, and provides a 95% confidence interval at every &tau; based on bootstrapping.  In particular, the input trajectories may not have constant time steps and the user can set the value of &tau; as a command-line input, that is technically used as a binwidth to assign the given coordinates to a time interval.
<br />
<br />
**Example**
<br />
The example directory contains 10 sample data files with arbitrary time values (column 1) and sample x and y coordinates (columns 2 and 3). The python script requires 3 command line inputs: the number of trajectory files, the time interval &tau;, and the number of bootstrap iterations (e.g. 'python GetMSD_2D_bootstrap.py &nbsp;&nbsp; 10 &nbsp;&nbsp; 0.3 &nbsp;&nbsp; 500'). An output file is written with the MSD (column 2) and the upper (column 3) and lower value (column 4) of a 95% conficence interval at every time interval (column 1).
