SELECT Sum(user_id_amount_and_rate_per_currency.rate * user_id_amount_and_rate_per_currency.amount)AS user_amount_in_gbp,
       user_id_amount_and_rate_per_currency.user_id
FROM  (SELECT user_id_amount_per_ts.currency,
              user_id_amount_per_ts.user_id,
              user_id_amount_per_ts.amount,
              exchange_rates.rate
       FROM  (SELECT Max(exchange_rates_joined_transactions.e_ts) AS ts,
                     exchange_rates_joined_transactions.currency,
                     exchange_rates_joined_transactions.user_id,
                     exchange_rates_joined_transactions.amount
              FROM   (SELECT exchange_rates.ts AS e_ts,
                             transactions.ts   AS t_ts,
                             exchange_rates.rate,
                             transactions.user_id,
                             transactions.currency,
                             transactions.amount
                      FROM   exchange_rates
                             LEFT OUTER JOIN transactions
                                          ON exchange_rates.from_currency =
                                             transactions.currency
                      WHERE  exchange_rates.ts <= transactions.ts
                             AND to_currency = 'GBP') AS exchange_rates_joined_transactions
              GROUP  BY t_ts,
                        currency,
                        user_id,
                        amount) AS user_id_amount_per_ts
             INNER JOIN exchange_rates
                     ON user_id_amount_per_ts.ts = exchange_rates.ts
                        AND user_id_amount_per_ts.currency = exchange_rates.from_currency
       WHERE  to_currency = 'GBP'
       UNION
       SELECT currency,
              user_id,
              amount,
              1 AS rate
       FROM   transactions
       WHERE  currency = 'GBP') AS user_id_amount_and_rate_per_currency
GROUP  BY user_id_amount_and_rate_per_currency.user_id; 