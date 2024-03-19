​Datediff(x, y) = x 와 y의 날짜 차이를 표기함. 

아래처럼 join 없이 할 수 도 있음.
SELECT w1.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature;