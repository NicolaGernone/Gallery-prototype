from dataclasses import dataclass

@dataclass
class ImageSorter:
    images: dict
    
    def sorter(self, images):
        return sorted(images, key=lambda i: i['weight'] if i['weight'] is not None else Decimal(0.0) , reverse=True)