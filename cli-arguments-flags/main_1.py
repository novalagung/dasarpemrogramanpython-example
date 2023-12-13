import sys

if __name__ == "__main__":
    print(f"type: {type(sys.argv).__name__}")
    print(f"len:  {len(sys.argv)}")

    for arg in sys.argv:
        print(f" ➜  {arg}")
