## Scott Schulze, 9/27/2020, Homework #5
___
### Grade
3/3 - Nice work. I'm glad you were able to get the histograms made. Next time try previewing your markdown file so t hat you can check your formatting a bit.  You can do  this by using control-shift-m in atom.  Also next time try including images in your markdown  file.

___

- Summary first, then homework questions. I know this is odd, but I enjoy how the bullet centers this block.

**Summary of this week's forecast**

This week's forecast was made by taking the tail of the dataset, expanded to 7 instead of the last 5. This gave me the previous week's flow information. I then ran the basic calculation suite on the data using .describe() to find its average. Because there is still no precipitation expected, I do expect the flow rates to continue to decrease so I set my first week's flow at the average flow, minus a standard deviation, and then subtracted one more cfs for good measure. *See table below.*

The second week of the forecast was set to one more standard deviation below the first week, to allow for further and expected recession. Though less confidence is had with the second week so the extra one cfs was not taken. I am very tempted to start paying closer attention to the weather for that area.

I will freely admit I still do not have the slightest idea how the long range forecast part works and therefore have likely shot myself in the foot for having any semblance of success with respect to doing well in that part of the competition.


| Calculated values |  |
| ---------- | ----------- |
| count	| 7.00 |
| mean	| 56.20 |
| std	| 1.89 |
| min	| 53.30 |
| 25%	| 54.85 |
| 50%	| 57.30 |
| 75%	| 57.45 |
| max	| 58.20 |

## Homework questions:

 1.
    1. The column names for the dataframe are: the agency code, the site number, the date and time, the flow, the code for the flow, year, month, and day.
    2. The index for this data set is an object data type and is a 1 dimensional array comprised of the column names.
    3. The data types are as follows: agency code is an object, site number is an integer, date and time is an object, flow is a float, the code is an object, year, month, and day are all integers.

 2. A complete summary of the flow column has characteristics as follows:
 | Calculated values |  |
 | ---------- | ----------- |
| count |	11585.00 |
| mean |	345.80 |
| std	| 1411.24 |
| min	| 19.00 |
| 25%	| 93.80 |
| 50%	| 158.00 |
| 75% |	216.00 |
| max |	63400.00 |

 3.
 | Calculated Monthly values |  |  |  |  |  |  |  |  |
 | ---------- | ----------- | ---------- | ----------- | ---------- |  ---------- | ---------- | ---------- | ---------- |
| month	| count |	mean |	std |	min |	25% |	50% |	75% |	max |
| 1	| 992.0	| 706.32	| 2749.15	| 158.0	| 202.00	| 219.50	| 292.00	| 63400.0 |
| 2	| 904.0	| 925.25	| 3348.82	| 136.0	| 201.00	| 244.00	| 631.00	| 61000.0 |
| 3	| 992.0	| 941.73	| 1645.80	| 97.0	| 179.00	| 387.50	| 1060.00	| 30500.0 |
| 4	| 960.0	| 301.24	| 548.14	| 64.9	| 112.00	| 142.00	| 214.50	| 4690.0 |
| 5	| 992.0	| 105.44	| 50.77	| 46.0	| 77.97	| 92.95	| 118.00	| 546.0 |
| 6	| 960.0	| 66.00	| 28.97	| 22.1	| 49.22	| 60.50	| 77.00	| 481.0 |
| 7	| 992.0	| 95.57	| 83.51	| 19.0	| 53.00	| 70.90	| 110.00	| 1040.0 |
| 8	| 992.0	| 164.35	| 274.46	| 29.6	| 76.07	| 114.00	| 170.25	| 5360.0 |
| 9	| 949.0	| 173.53	| 287.66	| 36.6	| 88.70	| 121.00	| 172.00	| 5590.0 |
| 10	| 961.0	| 146.17	| 111.78	| 69.9	| 107.00	| 125.00	| 153.00	| 1910.0 |
| 11	| 930.0	| 205.11	| 235.67	| 117.0	| 156.00	| 175.00	| 199.00	| 4600.0 |
| 12	| 961.0	| 337.10	| 1097.28	| 155.0	| 191.00	| 204.00	| 228.00	| 28700.0 |


##### The coding for the above was easy, formatting this table...was not.
4.

| Maximum daily flows (Top 5) |  |  |  |
| ---------- | ----------- | ---------- | ----------- |
| flow |	year |	month |	day |
| 30500.0	| 1995	| 3	| 6 |
| 35600.0	| 2005	| 2	| 12 |
| 45500.0	| 1995	| 2	| 15 |
| 61000.0	| 1993	| 2	| 20 |
| 63400.0	| 1993	| 1	| 8 |

| Minimum daily flows (Top 5) |  |  |  |
| ---------- | ----------- | ---------- | ----------- |
| flow |	year |	month |	day |
|	19.0	| 2012	| 7	| 1 |
|	20.1	| 2012	| 7	| 2 |
|	22.1	| 2012	| 6	| 30 |
|	22.5	| 2012	| 6	| 29 |
|	23.4	| 2012	| 7	| 3 |

5.  
Find the max and min for each month...
Given as month, then the minimum, then maximum and the respective years.
0
       flow  year
5143  158.0  2003
         flow  year
1468  63400.0  1993
1
      flow  year
783  136.0  1991
         flow  year
1511  61000.0  1993
2
    flow  year
83  97.0  1989
         flow  year
2255  30500.0  1995
3
       flow  year
10710  64.9  2018
       flow  year
821  4690.0  1991
4
      flow  year
5620  46.0  2004
       flow  year
1246  546.0  1992
5
      flow  year
8581  22.1  2012
       flow  year
1247  481.0  1992
6
      flow  year
8582  19.0  2012
        flow  year
6420  1040.0  2006
7
       flow  year
11192  29.6  2019
        flow  year
1330  5360.0  1992
8
       flow  year
11574  36.6  2020
        flow  year
5742  5590.0  2004
9
      flow  year
8677  69.9  2012
        flow  year
7949  1910.0  2010
10
        flow  year
10167  117.0  2016
        flow  year
5805  4600.0  2004
11
       flow  year
8735  155.0  2012
         flow  year
5842  28700.0  2004

6.  | flows within forecast range |  |  |
| ---------- | ----------- |----------- |
| index | datetime	| flow |
| 4991	| 2002-09-01	| 52.8 |
| 4992	| 2002-09-02	| 52.3 |
| 4993	| 2002-09-03	| 49.9 |
| 4994	| 2002-09-04	| 50.5 |
| 4995	| 2002-09-05	| 51.3 |
| 5722	| 2004-09-01	| 56.5 |
| 5723	| 2004-09-02	| 56.2 |
| 5724	| 2004-09-03	| 55.6 |
| 5732	| 2004-09-11	| 56.3 |
| 5733	| 2004-09-12	| 53.4 |
| 5734	| 2004-09-13	| 53.2 |
| 5736	| 2004-09-15	| 52.0 |
| 5737	| 2004-09-16	| 53.1 |
| 5735	| 2004-09-14	| 49.3 |
| 5738	| 2004-09-17	| 52.8 |
| 5739	| 2004-09-18	| 55.1 |
| 7551	| 2009-09-04	| 54.3 |
| 7552	| 2009-09-05	| 56.6 |
| 11200	| 2019-09-01	| 51.4 |
| 11210	| 2019-09-11	| 55.3 |
| 11211	| 2019-09-12	| 56.0 |
| 11212	| 2019-09-13	| 52.2 |
| 11213	| 2019-09-14	| 48.6 |
| 11214	| 2019-09-15	| 48.9 |
| 11215	| 2019-09-16	| 52.3 |
| 11219	| 2019-09-20	| 57.1 |
| 11220	| 2019-09-21	| 53.9 |
| 11221	| 2019-09-22	| 51.2 |
| 11569	| 2020-09-04	| 51.4 |
| 11570	| 2020-09-05	| 47.3 |
| 11577	| 2020-09-12	| 50.1 |
| 11583	| 2020-09-18	| 55.6 |
| 11578	| 2020-09-13	| 53.3 |
| 11584	| 2020-09-19	| 54.1 |
