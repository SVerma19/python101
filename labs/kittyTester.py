from kitty import Kitty

def main():
    myKitty = Kitty("snowball", "meow")

    print(myKitty)
    print(" ")
    print("true or false, the kitty likes milk?", myKitty.likesMilk())
    print(" ")

    myKitty.setSound("ROAR!")
    print("the new sound the kitty makes is", myKitty.getSound())
    print(" ")

    print(myKitty)

if __name__ == "__main__":
   main()
