# Mutual Fund Analytics Data Dictionary

## fact_nav

| Column    | Type    | Description                  |
| --------- | ------- | ---------------------------- |
| amfi_code | Integer | Mutual fund AMFI scheme code |
| date      | Date    | NAV date                     |
| nav       | Float   | Net Asset Value              |

## fact_transactions

| Column             | Type    | Description              |
| ------------------ | ------- | ------------------------ |
| investor_id        | Text    | Investor identifier      |
| transaction_date   | Date    | Transaction date         |
| amfi_code          | Integer | Scheme code              |
| transaction_type   | Text    | SIP, Lumpsum, Redemption |
| amount_inr         | Float   | Investment amount        |
| state              | Text    | Investor state           |
| city               | Text    | Investor city            |
| city_tier          | Text    | Tier classification      |
| age_group          | Text    | Investor age category    |
| gender             | Text    | Investor gender          |
| annual_income_lakh | Float   | Annual income in lakhs   |
| payment_mode       | Text    | Payment method           |
| kyc_status         | Text    | KYC verification status  |

## fact_performance

| Column        | Type    | Description             |
| ------------- | ------- | ----------------------- |
| amfi_code     | Integer | Scheme code             |
| scheme_name   | Text    | Mutual fund scheme name |
| expense_ratio | Float   | Fund expense ratio      |
| risk_grade    | Text    | Risk category           |
