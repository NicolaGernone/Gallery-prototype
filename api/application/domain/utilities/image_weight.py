from functools import cached_property

@cached_property
def weight_calculator(self, data):
    return (data['click'] * 0.7 + data['view'] * 0.3)