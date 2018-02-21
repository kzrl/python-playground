def main():

    print("** loop over sequence of integers **")
    
    for i in range(10):
        print(i)

    words = ["Overhead", "the", "albatross", "hangs",
             "motionless", "upon", "the", "air"]

    print("** loop over items in list **")
    
    for w in words:
        print(w)


    x = 0
    while x < 5:
        print("While loop")
        x += 1

        
    
if __name__ == "__main__":
    main()
