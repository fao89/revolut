


class CurrencyJson:

    def __init__(self, input):
        self.input = input
        self.output = {}

    def parse(self):
        for currency_dict in self.input:
            currency = currency_dict.get('currency')
            country = currency_dict.get('country')
            if country in str(self.output):
                self.output[currency][country].update(
                        {
                            currency_dict.get('city'): [
                                {'amount': currency_dict.get('amount')}
                            ]
                        }    
                )

            elif currency in self.output:
                self.output[currency].update(
                    {
                    country:
                        {
                            currency_dict.get('city'): [
                                {'amount': currency_dict.get('amount')}
                            ]
                        }    
                    }
                )
            else:
                self.output.update(
                    {currency: 
                        {
                        currency_dict.get('country'):
                            {
                                currency_dict.get('city'): [
                                    {'amount': currency_dict.get('amount')}
                                ]
                            }    
                        }
                    }
                )