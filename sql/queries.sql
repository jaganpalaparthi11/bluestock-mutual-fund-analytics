-- 1 Average NAV by Fund
SELECT amfi_code, AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

-- 2 Top NAV Funds
SELECT amfi_code, MAX(nav)
FROM fact_nav
GROUP BY amfi_code
ORDER BY MAX(nav) DESC
LIMIT 5;

-- 3 Transactions by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 4 SIP Transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='Sip';

-- 5 KYC Status Distribution
SELECT kyc_status, COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;

-- 6 Average Investment Amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- 7 Transactions by Gender
SELECT gender, COUNT(*)
FROM fact_transactions
GROUP BY gender;

-- 8 Transactions by City Tier
SELECT city_tier, COUNT(*)
FROM fact_transactions
GROUP BY city_tier;

-- 9 Risk Grade Distribution
SELECT risk_grade, COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

-- 10 Expense Ratio Analysis
SELECT AVG(expense_ratio)
FROM fact_performance;