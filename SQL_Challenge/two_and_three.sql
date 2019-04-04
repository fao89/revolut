WITH exchange_rate_with_max AS
  (SELECT Max(exchange_rates.ts) FILTER (
                                         WHERE exchange_rates.ts <= transactions.ts) AS ts,
          from_currency AS currency,
          user_id,
          amount
   FROM exchange_rates,
        transactions
   WHERE to_currency = 'GBP'
     AND currency = from_currency
   GROUP BY transactions.ts,
            from_currency,
            amount,
            user_id),
     max_exchange_rate AS
  (SELECT exchange_rate_with_max.*,
          rate
   FROM exchange_rate_with_max,
        exchange_rates
   WHERE exchange_rate_with_max.ts = exchange_rates.ts
     AND currency = from_currency
     AND to_currency = 'GBP'
   UNION SELECT ts,
                currency,
                user_id,
                amount,
                1 AS rate
   FROM transactions
   WHERE currency = 'GBP'),
     converted_amount_per_transaction AS
  (SELECT sum(rate * amount) AS total_spent_gbp,
          user_id
   FROM max_exchange_rate
   GROUP BY user_id)
SELECT *
FROM converted_amount_per_transaction
ORDER BY user_id