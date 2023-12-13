import argparse
import glob

def main():
    parser = argparse.ArgumentParser(
        prog='File Manager',
        description='Managing file easily'
    )

    parser.add_argument("--operation-mode", "-op", help="choose operation", choices=["write file", "list items"], required=True)
    parser.add_argument("--path", "-p", help="path of the file/folder", default=".", required=True)
    parser.add_argument("--content", "-c", help="content of the file", default="")
    args = parser.parse_args()

    if args.operation_mode == "write file":
        with open(args.path, 'a') as f:
            f.write(args.content)

    elif args.operation_mode == "list items":
        for f in glob.glob(f"{args.path}/**", recursive=True):
            print(f)

if __name__ == "__main__":
    main()

# python .\main_3.py --op-mode "write file" --path "file.txt" --content "yes"
# python .\main_3.py --op-mode "list items" --path "C:\LibsSoftLink\dasarpemrogramanpython\examples\cli-arguments-flags"