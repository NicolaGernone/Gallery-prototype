from dataclasses import dataclass

@dataclass
class ImageWeightCalculator:
    data: dict
    
    @cached_property
    def weight_calculator(self, data):
        weight = data['click'] * 0.7 + data['view'] * 0.3
        return weight