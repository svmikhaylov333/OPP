from src.category import Category
#from src.product import Product

class ProductIterator:
    def __init__(self, category : Category):
        self.category = category
        self.index =0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.get_product_list()):
            product =self.category.get_product_list()[self.index]
            self.index += 1
            return  product
        else:
            raise StopIteration

