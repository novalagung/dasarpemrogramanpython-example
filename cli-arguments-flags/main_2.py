import sys

def get_arg(index):
    if len(sys.argv) > index:
        return sys.argv[index]
    else:
        return None

if __name__ == "__main__":
    print(f"type: {type(sys.argv).__name__}")
    print(f"len:  {len(sys.argv)}")
    
    print(f"arg1: {get_arg(0)}")
    print(f"arg2: {get_arg(1)}")
    print(f"arg3: {get_arg(2)}")
    print(f"arg4: {get_arg(3)}")
    print(f"arg5: {get_arg(4)}")
