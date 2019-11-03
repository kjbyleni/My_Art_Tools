from lib.generator import Generator


class ItemGenerator(Generator):
    items_path = './items/items_list.txt'

    def __init__(self):
        Generator.__init__(self, 'Items')
        self.ITEMS = 'items'
        self.keys = [self.ITEMS]

    def generate(self, how_many=None,  attempt=0):
        if how_many is None:
            how_many = self.message.how_many()
        try:
            total = int(how_many)
            for i in range(total):
                self.get_rand_item(self.ITEMS)

            self.print_result()
        except ValueError:
            self.message.input_must_be_number()
            if attempt > 1:
                self.message.too_many_attempts()
            else:
                ItemGenerator.generate(self, how_many=None, attempt=attempt + 1)
