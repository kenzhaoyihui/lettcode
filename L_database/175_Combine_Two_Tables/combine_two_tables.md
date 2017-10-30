# Info:
```
MariaDB [test]> select * from Person;
+----------+-----------+----------+
| PersonId | FirstName | LastName |
+----------+-----------+----------+
|        1 | Jia       | Liu      |
|        2 | Yihui     | zhao     |
+----------+-----------+----------+
2 rows in set (0.00 sec)

MariaDB [test]> select * from Address;
+-----------+----------+---------+---------+
| AddressId | PersonId | City    | State   |
+-----------+----------+---------+---------+
|         1 |        1 | Nanjing | China   |
|         2 |        2 | NJ      | ChinaNJ |
+-----------+----------+---------+---------+
2 rows in set (0.00 sec)
```

1. `SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person LEFT JOIN Address ON Person.PersonId = Address.PersonId;`

2. `SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person LEFT JOIN Address USING(PersonId);`

3. `SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person NATURAL LEFT JOIN Address;`



## Mysql union select method: inner join, left outer join, right outer join, full outer join

1. 把两个表中都存在PersonId的行拼成一行（即内联）
 inner join: `select * from Person inner join Address on Person.PersonId=Address.PersonId;`
2. 显示左表Person中的所有行，并把右表Address中符合条件加到左表Person中；
右表Address中不符合条件，就不用加入结果表中，并且NULL表示。
 left outer join : `select Person.FirstName, Person.LastName, Address.City, Address.State from Person left join Address on Person.PersonId=Address.PersonId;`

3. 显示右表Address中的所有行，并把左表Person中符合条件加到右表Address中；
左表Person中不符合条件，就不用加入结果表中，并且NULL表示。
right outer join: `select Person.FirstName, Person.LastName, Address.City, Address.State from Address right join Person on Person.PersonId=Address.PersonId;`

