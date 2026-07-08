# Program which accept one num and display below pattern
# *   *   *
# *   *   *
# *   *   *

def pattern():
    no = int(input("Enter Number :"))
    for i in range(1,no+1,1):
        print("* " * no)


def main():
    pattern()

if __name__ == "__main__":
    main()