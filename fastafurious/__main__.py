import fastafurious
from sys import argv, exit

# Entry point for setuptools and ther sub-commands
def main():
    return fastafurious.run( argv[1:] )

if __name__ == "__main__":
    exit( main() )
