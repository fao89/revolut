


class CurrencyJson:

    def __init__(self, input, nesting_order):
        self.input = input
        self.output = {}
        self.nesting_order = nesting_order

    def parse(self):
        first_level = self.nesting_order[0]
        second_level = self.nesting_order[1]
        last = self.nesting_order[-1]
        
        for flat_dict in self.input:
            first = flat_dict.get(first_level)
            second = flat_dict.get(second_level)

            if second in str(self.output.get(first)):
                self.output[first][second].update(
                        {
                            flat_dict.get(last): [
                                {'amount': flat_dict.get('amount')}
                            ]
                        }    
                )

            elif first in self.output:
                self.output[first].update(
                    {
                    second:
                        {
                            flat_dict.get(last): [
                                {'amount': flat_dict.get('amount')}
                            ]
                        }    
                    }
                )
            else:
                self.output.update(
                    {first: 
                        {
                        flat_dict.get(second_level):
                            {
                                flat_dict.get(last): [
                                    {'amount': flat_dict.get('amount')}
                                ]
                            }    
                        }
                    }
                )