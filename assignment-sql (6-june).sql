SELECT TOP 5 * FROM customer_nodes;
SELECT TOP 5 * FROM customer_transactions;

TRUNCATE TABLE customer_nodes ;


BULK INSERT customer_nodes
FROM 'C:\SQLData\customer_nodes.csv'
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0A',
    TABLOCK
);

BULK INSERT customer_transactions
FROM 'C:\SQLData\customer_transactions.csv'
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0A',
    TABLOCK
);

SELECT COUNT(*) FROM customer_nodes;
SELECT COUNT(*) FROM customer_transactions;

use data_bank ;
-- How many unique nodes are there on the Data Bank system?
select count(distinct node_id) as unique_nodes from customer_nodes;

-- What is the number of nodes per region?
select region_id , count(distinct node_id) as number_of_nodes from customer_nodes 
    group by region_id order by region_id asc ;


select r.region_name , count(cn.node_id) as number_of_nodes from customer_nodes as cn 
    join regions r on r.region_id = cn.region_id
        group by r.region_name ;



    --How many customers are allocated to each region?
    select region_id , count(distinct customer_id) as customer_count from customer_nodes
        group by region_id ;


        select r.region_name , count(cn.customer_id) as number_of_customers from customer_nodes as cn 
    join regions r on r.region_id = cn.region_id
        group by r.region_name ;


        --How many days on average are customers reallocated to a different node?
SELECT TOP 20
       customer_id,
       start_date,
       end_date,
       DATEDIFF(day, start_date, end_date) AS days_on_node
FROM customer_nodes; 


select avg(t.days_on_node) as avg_of_days from 
(select datediff(day, start_date ,end_date) as days_on_node 
from customer_nodes ) t;


-- 5.What is the median, 80th and 95th percentile for this same
--reallocation days metric for each region?

select distinct  r.region_name  , percentile_cont(0.5) within group (order by t.days_on_node ) over(partition by t.region_id) as median ,
percentile_cont(0.8) within group (order by t.days_on_node ) over(partition by t.region_id) as p80 ,
percentile_cont(0.95) within group (order by t.days_on_node ) over(partition by t.region_id) as p95 
from 
(select customer_id , region_id  , start_date , end_date , datediff( day , start_date , end_date) as days_on_node
from customer_nodes) t  join regions r on r.region_id = t.region_id 
;



--6. What is the unique count and total amount for each transaction type?

select txn_type , count(*) as transction_occured ,sum(txn_amount) as total_amount 
from customer_transactions
group by txn_type ;



--What is the average total historical deposit counts and amounts for all customers?

select avg(t.deposit_amount) as avg_deposit_amount , avg(t.deposit_count) as avg_deposit_count from
(
select customer_id ,count(*) as deposit_count ,  sum(txn_amount) as deposit_amount
from customer_transactions
where txn_type ='deposit'
group by customer_id ) t
;

 --  For each month - how many Data Bank customers make more than 1 deposit
 --   and either 1 purchase or 1 withdrawal in a single month?


 select t.month , count(
 case 
 when t.deposits > 1 and ( t.purchases = 1 or t.withdrawals = 1 ) 
 then t.customer_id end 
 )
 as customer_count from

 (
 select customer_id ,   DATENAME(MONTH,txn_date) as month, 
sum( case
        when txn_type = 'deposit' then 1
        else 0 end ) as deposits ,
 sum( case
        when txn_type = 'purchase' then 1
        else 0 end ) as purchases ,
 sum( case
        when txn_type = 'withdrawal' then 1
        else 0 end ) as withdrawals 
 from customer_transactions  
group by customer_id ,  DATENAME(MONTH,txn_date)  )  t 
group by t.month 
;
