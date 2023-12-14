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

def delete_data(row_index):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for index, row in enumerate(rows):
            if index != (row_index - 1):
                writer.writerow({
                    'name': row['name'],
                    'email': row['email'],
                    'phone': row['phone']
                })

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
            row_index = int(input("Row index: "))
            delete_data(row_index)
        elif mode == '4':
            break
        else:
            print('Invalid mode')

def main():
    prepare_csv()
    control_flow()

if __name__ == '__main__':
    main()
