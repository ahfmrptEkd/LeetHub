​이 쿼리는 데이터베이스 내의 Delivery 테이블에서 각 고객의 첫 번째 주문 중 즉시 주문(order_date와 customer_pref_delivery_date가 같은 경우)의 비율을 계산합니다. 쿼리의 작동 방식은 다음과 같습니다:

서브쿼리:
SELECT customer_id, MIN(order_date) AS first_order_date FROM Delivery GROUP BY customer_id 이 부분은 Delivery 테이블에서 각 고객별(customer_id)로 가장 이른 order_date(첫 번째 주문 날짜)를 찾습니다. 결과로, 각 고객의 ID와 그들의 첫 주문 날짜를 포함하는 목록이 생성됩니다.

WHERE 절:
서브쿼리의 결과(각 고객의 첫 주문 날짜)를 사용하여, 메인 쿼리의 WHERE 절은 Delivery 테이블에서 해당 고객의 첫 번째 주문 정보만을 필터링합니다. 즉, (customer_id, order_date) IN (서브쿼리 결과)를 통해, 주어진 고객 ID와 첫 주문 날짜에 해당하는 주문만을 선택합니다.

SELECT 절:
ROUND(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0 / COUNT(DISTINCT customer_id), 2) AS immediate_percentage 이 부분은 선택된 주문(각 고객의 첫 주문) 중에서 즉시 주문의 비율을 계산합니다. CASE 문을 사용하여 order_date와 customer_pref_delivery_date가 같은 경우(즉시 주문)에는 1을, 그렇지 않은 경우에는 0을 반환합니다. 이 값들을 합산하여 즉시 주문의 총 수를 구하고, 이를 전체 고객 수(COUNT(DISTINCT customer_id))로 나눈 후 100을 곱하여 백분율을 얻습니다. 마지막으로, ROUND 함수를 사용하여 결과를 소수점 두 자리까지 반올림합니다.

결과적으로, 이 쿼리는 모든 고객의 첫 번째 주문 중 즉시 주문의 비율을 백분율로 반올림하여 immediate_percentage라는 이름의 열로 반환합니다.
