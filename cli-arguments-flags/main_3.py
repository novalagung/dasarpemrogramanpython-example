import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='File Manager',
        description='Managing file easily'
    )

    parser.add_argument("--path", help="path of the file/folder", default="file.txt", required=True)
    parser.add_argument("--content", help="content of the file", default="")
    args = parser.parse_args()

    with open(args.path, 'a') as f:
        f.write(args.content)

if __name__ == "__main__":
    main()
