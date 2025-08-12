-- Orders delivered late
SELECT order_id, customer_id, order_estimated_delivery_date, order_delivered_customer_date
FROM orders
WHERE order_delivered_customer_date > order_estimated_delivery_date;

-- SLA breach detection (example: more than 3 late orders per day)
SELECT DATE(order_purchase_timestamp) as order_date, COUNT(*) as late_orders
FROM orders
WHERE order_delivered_customer_date > order_estimated_delivery_date
GROUP BY order_date
HAVING late_orders > 3;
