-- # Write your MySQL query statement below

WITH unikalni_uzytkownicy AS (
    SELECT COUNT(DISTINCT user_id) AS liczba_unikalnych_uzytkownikow
    FROM Users
)
SELECT
    r.contest_id,
    ROUND(COUNT(r.user_id) / un.liczba_unikalnych_uzytkownikow * 100, 2) AS percentage
FROM Register r
LEFT JOIN Users u ON r.user_id = u.user_id
CROSS JOIN unikalni_uzytkownicy un
GROUP BY r.contest_id, un.liczba_unikalnych_uzytkownikow
ORDER BY percentage DESC, r.contest_id ASC;
