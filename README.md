# Insight Data Engineer Challenge
### Problem
1. Get "CERTIFIED" cases
2. Get **Occupation counts** and **State counts** 
3. Get the percentage, which is (Numbers of Occupation or State counts / Total Certified Case) * 100%
4. Sort the counts and select top 10 items
5. Output the results to ```top_10_occupations.txt``` and ```top_10_states.txt```

### My Approach
1. Directly open the file, read the data line by line, filter the "CERTIFIED" data and count the numbers of *Occupations* & *States*.
**Key point:** I did not save the raw data to a list but only save the term frequencies to two dictionaries, which represent the numbers of *Occupations* and *States*.
2. Sort two ditionaries by the built-in function and set two orders as the question requested.
3. Calculate percentages and add the results to the sorting lists.
**Key point:** Because tuples are immunicable, I change the original sort tuples to lists that we can further calculate percentages.
4. Write output files ```top_10_occupations.txt``` and ```top_10_states.txt```.
**Key point:** Use OOP to make codes more scalable, reusable and understandable.

*Note: I did not use packages like pandas, csv, numpy etc*

### Comparison (Two versions)
* Version 1: Save the data line by line and then creates two dictionary to store **Occupation counts** and **State counts**. OOP not used.
* Version 2: Directly save **Occupation counts** and **State counts** to dictionary without saving the original data. OOP used.


| Version  | Speed | Data Structure (load file)| Data Structure (count frequency)| OOP |
| -------- | -------- | --------- | --------- | --------- | --------- |
| Version 1 | 20 seconds | list | dictionary | Yes |
| Version 2 | 6 seconds | x | dictionary | No |



### Assumptions
1. The column names
In my code, I use **"CASE_STATUS"**, **"SOC_NAME"** and **"WORKSITE_STATE"**, which fits the data in year 2016 and 2015.
  * Problem: Sometimes, the column names will change by year. For example, In year 2016, the occupation was stored in "SOC_NAME" column. However, in year 2014, the occupation was stored in "LCA_CASE_SOC_NAME" column.
  * Solution: Change manually. Or we can create a column list to store column names by year. Afterward, we can compare this column list with the header from our raw data. However, this method will increase the time/space complexity.

2. Ignore typos
  * Problem: The **"WORKSITE_STATE"** column also stores city names or other contents, which I did not clean them.
  * Solution: Remove non-state contents.


### Plan for the Future
#### **Question: Find the average certified amount for each occupations**
*1. Example*
  * year 2016: ("job1", 150), ("job2", 100), ("job3", 50)
  * year 2015: ("job1", 200), ("job2", 80)
*2. Record frequency - mapValues*
  * year 2016: ("job1", (150, 1)), ("job2", (100, 1)), ("job3", (50, 1))
  * year 2015: ("job1", (200, 1)), ("job2", (80, 1))
*3. Sum the values by key - reduceByKey*
("job1", (350, 2)), ("job2", (180, 2)), ("job3", (50, 1))
*4. Calculate the average certified amount - mapValues & collect*
("job1", 175), ("job2", 90), ("job3", 50)


### How to Execute
Please run ```./run.sh``` and you will see two output files in the output folder.


### Note
Because I'm really interested in how to efficiently tackle this problem, I add more details about how to decrease the time/space complexity and even think about a future case after the submission deadline.
