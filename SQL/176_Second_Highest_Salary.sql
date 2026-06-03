SELECT(
    SELECT DISTINCT
        e.salary
    from Employee e
    ORDER by salary DESC
    LIMIT 1 OFFSET 1
) as secondhighestsalary