# 176. Second Highest Salary

```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

```
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

```
1. SELECT MAX(Salary) as SecondHighestSalary FROM Employee WHERE Salary NOT IN (SELECT MAX(Salary)  FROM Employee);

2. SELECT Salary as SecondHighestSalary   FROM Employee GROUP BY Salary UNION ALL (SELECT NULL AS Salary) ORDER BY SecondHighestSalary DESC LIMIT 1 OFFSET 1;

3. select case when count(Salary)>1 then  (select distinct Salary from Employee order by Salary DESC limit 1, 1) else NULL end as SecondHighestSalary from Employee;

```


