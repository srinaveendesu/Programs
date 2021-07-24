
# https://leetcode.com/problems/employees-earning-more-than-their-managers/

# Write your MySQL query statement below

# SELECT
#     a.Name AS 'Employee'
# FROM
#     Employee AS a,
#     Employee AS b
# WHERE
#     a.ManagerId = b.Id
#         AND a.Salary > b.Salary
# ;

# SELECT
#      a.NAME AS Employee
# FROM Employee AS a JOIN Employee AS b
#      ON a.ManagerId = b.Id
#      AND a.Salary > b.Salary
# ;

# https://leetcode.com/problems/duplicate-emails/

# Write your MySQL query statement below

#
# select Email
# from Person
# group by Email
# having count(Email) > 1;


# select Email from
# (
#   select Email, count(Email) as num
#   from Person
#   group by Email
# ) as statistic
# where num > 1
# ;