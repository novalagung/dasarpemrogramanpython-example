class Company:

    def __init__(self, name = "", products =[]):
        self.name = name
        self.products = products
        self.__version = 1.0
    
    def info(self):
        self.__print_name()
        self.__print_products()

    def __print_name(self):
        print(f"company name: {self.name}")

    def __print_products(self):
        print(f"products:")
        for p in self.products:
            print(f"  -> {p.name} ({p.category})")
