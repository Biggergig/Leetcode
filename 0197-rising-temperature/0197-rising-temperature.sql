# Write your MySQL query statement below
SELECT W2.id
FROM Weather as W1
JOIN Weather as W2
WHERE datediff(W2.recordDate,W1.recordDate) = 1
AND W2.temperature > W1.temperature;