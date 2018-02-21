def main():

    with open("franklin.txt") as f:
        for line in f:
            print(line.rstrip())
    

if __name__ == "__main__":
    main()
