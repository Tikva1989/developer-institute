** Daily Challenge : SQL Puzzle **
Q1. 3 !---0, is Null is operator which returns true or false.
 SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

Q2.---2
--  SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
--Q3 ==0
--  SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

--Q4 ==3
-- SELECT * FROM SecondTab
--    SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
