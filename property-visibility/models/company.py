class Company:

    def __init__(self, name = "", products =[]):
        self.name = name
        self.products = products
    
    def info(self):
        print(f"company name: {self.name}")
        print(f"products:")
        for p in self.products:
            print(f"  -> {p.name} ({p.category})")
