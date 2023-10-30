from models import company
from models import product

if __name__ == "__main__":
    data = []

    c1 = company.Company(name="Microsoft", products=[
        product.Product(name="Windows", category="Operating system"),
        product.Product(name="Office 365", category="Productivity software")
    ])
    data.append(c1)
    
    c2 = company.Company(name="Mattel", products=[
        product.Product(name="Hot Wheels", category="Car toys"),
        product.Product(name="Uno", category="Card game")
    ])
    data.append(c2)

    for d in data:
        d.info()
