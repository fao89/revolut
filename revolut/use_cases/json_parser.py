


class ParseJson:

    def __init__(self, input, nesting_order):
        self.input = input
        self.output = {}
        self.nesting_order = nesting_order

    def get_nest_level(self, flat_dict):
        value = self.output
        
        for index, nest in enumerate(self.nesting_order):
            previous = value
            value = value.get(flat_dict.get(nest))

            if not value:
                break
        
        return index, previous



    def parse(self):
        
        for flat_dict in self.input:
            leaf = list(set(flat_dict.keys()) - set(self.nesting_order))
            leaf_array = [{l: flat_dict.get(l) for l in leaf}]
            
            index, dict_to_update = self.get_nest_level(flat_dict)
            stop_at = self.nesting_order[index]
            current = leaf_array
            
            for nest in reversed(self.nesting_order):
                if nest == stop_at:
                    dict_to_update.update({flat_dict.get(nest): current})
                    break
                previous = current
                current = {flat_dict.get(nest): previous}

