def main():

    money = """Money, get away
Get a good job with more pay and you're okay
Money, it's a gas
Grab that cash with both hands and make a stash
New car, caviar, four-star daydream
Think I'll buy me a football team"""
    money = money.strip()
    money = money.replace(",", "")
    money = money.replace("\n", " ")
    words = money.split(" ")
    print(words)

    # print the first 3 words
    print(words[0:3])
    print(words[:3])

    # print the last 3 words
    print(words[-3:])

    #copy list
    rev = words.copy()
    
    
    # reverse in place
    rev.reverse()
    print(words)
    print(rev)

    # length
    print(len(words))
    
if __name__ == "__main__":
    main()
