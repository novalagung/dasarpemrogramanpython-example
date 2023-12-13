import csv

filename = 'data.csv'
fieldnames = ['name', 'email', 'phone']

def prepare_csv():
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

def write_data(name, email, phone):
    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({
            'name': name,
            'email': email,
            'phone': phone
        })

def read_data():
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader):
            print(" ->", f"(row {index + 1})", row['name'], row['email'], row['phone'])

def control_flow():
    while True:
        print("Choose mode:")
        print("1. Write data")
        print("2. Read data")
        print("3. Delete by row")
        print("4. Exit")

        mode = input('Choice (1/2/3/4): ')
        if mode == '1':
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            write_data(name, email, phone)
        elif mode == '2':
            read_data()
        elif mode == '3':
            pass
        else:
            break

def main():
    prepare_csv()
    control_flow()

if __name__ == '__main__':
    main()
