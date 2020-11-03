import sys 

def decorator_func(func):
    def wrapper(args):
        with open('output.html', 'w') as f:
            f.write("<body>")
            f.write(func(args))
            f.write("</body>")
    return wrapper

@decorator_func
def stringify_args(args):
    return ' '.join(args)
        
if __name__ == "__main__":
    args = sys.argv[1:]
    stringify_args(args)
    