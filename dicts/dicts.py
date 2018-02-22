def main():

    d = {
        "pickup": "sign",
        "talk to": "LeChuck",
        "walk to": "Stan's used ship emporium",
        "ask": "For help",
    }

    # loop over keys and values
    for key,value in d.items():
        print("{} {}".format(key, value))

    # print sorted keys
    sortedKeys = sorted(d.keys())
    for k in sortedKeys:
        print(k)


    # test if key exists
    if "ask" in d:
        print("Key exists")

    # or not exists
    if "moop" not in d:
        print("No moop")
        

if __name__ == "__main__":
    main()
    
