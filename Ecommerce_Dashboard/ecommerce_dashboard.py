Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============================ RESTART: C:/Users/user/AppData/Local/Programs/Python/Python313/git_hub.py ============================

============================ RESTART: C:/Users/user/AppData/Local/Programs/Python/Python313/git_hub.py ============================

=================== RESTART: C:/Users/user/AppData/Local/Programs/Python/Python313/data-visualization-project.py ==================

============================== RESTART: C:\Users\user\AppData\Local\Programs\Python\Python313\new2.py =============================

================ FIRST 5 ROWS ================

  Order ID              Order Date  ... Quantity   Profit
0  ORD1000 2024-01-01 00:00:00.000  ...        5   149.93
1  ORD1001 2024-01-04 16:02:24.724  ...        3   876.90
2  ORD1002 2024-01-08 08:04:49.447  ...        7   153.73
3  ORD1003 2024-01-12 00:07:14.171  ...        2  1003.94
4  ORD1004 2024-01-15 16:09:38.894  ...        9    98.54

[5 rows x 9 columns]

================ DATA INFO ================

<class 'pandas.DataFrame'>
RangeIndex: 200 entries, 0 to 199
Data columns (total 9 columns):
 #   Column            Non-Null Count  Dtype         
---  ------            --------------  -----         
 0   Order ID          200 non-null    str           
 1   Order Date        200 non-null    datetime64[us]
 2   Customer Name     200 non-null    str           
 3   City              200 non-null    str           
 4   Product Category  200 non-null    str           
 5   Product Name      200 non-null    str           
 6   Sales Amount      200 non-null    int64         
 7   Quantity          200 non-null    int64         
 8   Profit            200 non-null    float64       
dtypes: datetime64[us](1), float64(1), int64(2), str(5)
memory usage: 21.5 KB
None

================ NULL VALUES ================

Order ID            0
Order Date          0
Customer Name       0
City                0
Product Category    0
Product Name        0
Sales Amount        0
Quantity            0
Profit              0
dtype: int64

================ STATISTICAL SUMMARY ================

                Order Date  Sales Amount    Quantity       Profit
count                  200    200.000000  200.000000   200.000000
mean   2024-12-31 00:00:00   2840.920000    4.725000   521.431550
min    2024-01-01 00:00:00    504.000000    1.000000    26.150000
25%    2024-07-01 12:00:00   1645.750000    2.000000   236.340000
50%    2024-12-31 00:00:00   2996.500000    5.000000   485.770000
75%    2025-07-01 12:00:00   3850.000000    7.000000   771.265000
max    2025-12-31 00:00:00   4995.000000    9.000000  1353.510000
std                    NaN   1283.591394    2.555785   328.656056

================ COLUMN NAMES ================

Index(['Order ID', 'Order Date', 'Customer Name', 'City', 'Product Category',
       'Product Name', 'Sales Amount', 'Quantity', 'Profit'],
      dtype='str')

================ OVERALL SUMMARY ================

Total Sales      : 568184
Total Profit     : 104286.31
Total Quantity   : 945
Total Orders     : 200

================================================
SUMMARY REPORT SAVED SUCCESSFULLY
File Name : summary_report.xlsx
================================================

Cleaned data saved as cleaned_data.xlsx

=========================== RESTART: C:\Users\user\AppData\Local\Programs\Python\Python313\matplotpr1.py ==========================

========== DATASET OVERVIEW ==========
  Order ID  Order Date Customer_Name  ... Total_Amount Payment Method Order Status
0  ORD1000  2024-04-07   Sanjana Rao  ...    184100.00            UPI    Delivered
1  ORD1001  2024-05-02    Riya Verma  ...     44028.00            COD      Shipped
2  ORD1002  2024-05-08    Riya Verma  ...    116805.30            COD      Shipped
3  ORD1003  2024-06-06    Amit Singh  ...     37304.60    Credit Card    Cancelled
4  ORD1004  2024-03-19   Rahul Gupta  ...     89425.95    Credit Card    Delivered

[5 rows x 14 columns]

========== DATASET SHAPE ==========
(300, 14)

========== COLUMN NAMES ==========
Index(['Order ID', 'Order Date', 'Customer_Name', 'City', 'State', 'Product',
       'Category', 'Sub-Category', 'Quantity', 'Unit Price', 'Discount',
       'Total_Amount', 'Payment Method', 'Order Status'],
      dtype='str')

========== MISSING VALUES ==========
Order ID          0
Order Date        0
Customer_Name     0
City              0
State             0
Product           0
Category          0
Sub-Category      0
Quantity          0
Unit Price        0
Discount          0
Total_Amount      0
Payment Method    0
Order Status      0
dtype: int64

========== DATA TYPES ==========
Order ID              str
Order Date            str
Customer_Name         str
City                  str
State                 str
Product               str
Category              str
Sub-Category          str
Quantity            int64
Unit Price          int64
Discount            int64
Total_Amount      float64
Payment Method        str
Order Status          str
dtype: object

========== STATISTICAL SUMMARY ==========
         Quantity    Unit Price    Discount   Total_Amount
count  300.000000    300.000000  300.000000     300.000000
mean     2.946667  25014.350000   10.000000   67057.105167
std      1.389337  14264.470018    7.094677   50858.988171
min      1.000000    307.000000    0.000000     782.850000
25%      2.000000  13562.500000    5.000000   28214.475000
50%      3.000000  24172.000000   10.000000   53420.300000
75%      4.000000  37139.250000   15.000000   97920.475000
max      5.000000  49858.000000   20.000000  196898.250000

========== BUSINESS SUMMARY ==========
Total Sales      : ₹20,117,131.55
Total Orders     : 300
Total Customers  : 8
Top Category     : Fashion

=========================== RESTART: C:\Users\user\AppData\Local\Programs\Python\Python313\matplotpr1.py ==========================

========== DATASET OVERVIEW ==========
  Order ID  Order Date Customer_Name  ... Total_Amount Payment Method Order Status
0  ORD1000  2024-04-07   Sanjana Rao  ...    184100.00            UPI    Delivered
1  ORD1001  2024-05-02    Riya Verma  ...     44028.00            COD      Shipped
2  ORD1002  2024-05-08    Riya Verma  ...    116805.30            COD      Shipped
3  ORD1003  2024-06-06    Amit Singh  ...     37304.60    Credit Card    Cancelled
4  ORD1004  2024-03-19   Rahul Gupta  ...     89425.95    Credit Card    Delivered

[5 rows x 14 columns]

========== DATASET SHAPE ==========
(300, 14)

========== COLUMN NAMES ==========
Index(['Order ID', 'Order Date', 'Customer_Name', 'City', 'State', 'Product',
       'Category', 'Sub-Category', 'Quantity', 'Unit Price', 'Discount',
       'Total_Amount', 'Payment Method', 'Order Status'],
      dtype='str')

========== MISSING VALUES ==========
Order ID          0
Order Date        0
Customer_Name     0
City              0
State             0
Product           0
Category          0
Sub-Category      0
Quantity          0
Unit Price        0
Discount          0
Total_Amount      0
Payment Method    0
Order Status      0
dtype: int64

========== DATA TYPES ==========
Order ID              str
Order Date            str
Customer_Name         str
City                  str
State                 str
Product               str
Category              str
Sub-Category          str
Quantity            int64
Unit Price          int64
Discount            int64
Total_Amount      float64
Payment Method        str
Order Status          str
dtype: object

========== STATISTICAL SUMMARY ==========
         Quantity    Unit Price    Discount   Total_Amount
count  300.000000    300.000000  300.000000     300.000000
mean     2.946667  25014.350000   10.000000   67057.105167
std      1.389337  14264.470018    7.094677   50858.988171
min      1.000000    307.000000    0.000000     782.850000
25%      2.000000  13562.500000    5.000000   28214.475000
50%      3.000000  24172.000000   10.000000   53420.300000
75%      4.000000  37139.250000   15.000000   97920.475000
max      5.000000  49858.000000   20.000000  196898.250000

========== BUSINESS SUMMARY ==========
Total Sales      : ₹20,117,131.55
Total Orders     : 300
Total Customers  : 8
Top Category     : Fashion

