import csv

def prepare_csv():
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'email', 'phone'])

def write_data(name, email, phone):
    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, email, phone])

def read_data():
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            if index == 0:
                continue
            print(" ->", f"(row {index})", row[0], row[1], row[2])

def delete_data(row_index):
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for index, row in enumerate(rows):
            if index != row_index:
                writer.writerow([row[0], row[1], row[2]])

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
        else:
            break

def main():
    prepare_csv()
    control_flow()

if __name__ == '__main__':
    main()
