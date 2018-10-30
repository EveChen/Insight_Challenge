# Insight Data Engineer Challenge
### Problem
1. Get "CERTIFIED" cases
2. Get *Occupation counts* and *State counts* 
3. Get the percentage, which is (Numbers of Occupation or State counts / Total Certified Case) * 100%

### My Approach
Directly open the file, filter the "CERTIFIED" data, count the numbers of Occupation & State & percentages, and finally write output files ```top_10_occupations.txt``` and ```top_10_states.txt```.

*Note: I did not use packages like pandas, csv, numpy etc*

### Future Improvements
1. Use **csv** package to decrease the space complexity.
2. Be aware of the column names, which change by year. e.g. In year 2016, the occupation was stored in "SOC_NAME" column. However, in year 2014, the occupation was stored in "LCA_CASE_SOC_NAME" column.
3. Use more stuctured OOP for further scaling up.


### How to Execute
Please run ```./run.sh``` and you will see two output files in the output folder.
