WITH exchange_rate_with_max
     AS (SELECT *,
                Max(ts)
                  OVER (
                    partition BY from_currency) max_ts
         FROM   exchange_rates
         WHERE  to_currency = 'GBP'),
     max_exchange_rate
     AS (SELECT *
         FROM   exchange_rate_with_max
         WHERE  ts = max_ts
         UNION
         SELECT Now() AS ts,
                'GBP' AS from_currency,
                'GBP' AS to_currency,
                1     AS rate,
                Now() AS max_ts),
     converted_amount_per_transaction
     AS (SELECT Sum(rate * amount) AS total_spent_gbp,
                user_id
         FROM   transactions,
                max_exchange_rate
         WHERE  currency = from_currency
         GROUP  BY user_id)
SELECT *
FROM   converted_amount_per_transaction 