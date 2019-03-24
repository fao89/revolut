SELECT Sum(user_amount_in_gbp.amount) AS total_spent_gbp,
       user_id
FROM  (SELECT ( rate * Sum(amount) ) AS amount,
              user_id
       FROM  (SELECT exchange_rates.rate,
                     exchange_rates.from_currency
              FROM   exchange_rates
                     INNER JOIN (SELECT Max(ts) AS ts,
                                        from_currency
                                 FROM   exchange_rates
                                 WHERE  to_currency = 'GBP'
                                 GROUP  BY from_currency) AS max_currencies
                             ON exchange_rates.ts = max_currencies.ts
                                AND exchange_rates.from_currency =
                                    max_currencies.from_currency
              WHERE  to_currency = 'GBP'
              UNION
              SELECT 1     AS rate,
                     'GBP' AS from_currency) AS rate_per_currency
             INNER JOIN (SELECT Sum(amount) AS amount,
                                user_id,
                                currency
                         FROM   transactions
                         GROUP  BY user_id,
                                   currency) AS user_amount_per_currency
                     ON user_amount_per_currency.currency = rate_per_currency.from_currency
       GROUP  BY rate_per_currency.rate,
                 user_amount_per_currency.user_id) AS user_amount_in_gbp
GROUP  BY user_amount_in_gbp.user_id; 