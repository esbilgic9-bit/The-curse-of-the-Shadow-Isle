print("𝔗𝔥𝔢 ℭ𝔲𝔯𝔰𝔢 𝔬𝔣 𝔱𝔥𝔢 𝔖𝔥𝔞𝔡𝔬𝔴 ℑ𝔰𝔩𝔢 ")

print("""
Ahoy, traveler! You've just stepped onto the Mysterious Isle of Shadows.
Be careful,treasures and traps are everywhere! ⚱️🐍
The path splits here! Before you stand two ancient gates: 🚪 a Crimson Red gate and  🚪 a Deep Blue gate.
""")
gate = input("Which one will you dare to enter?🚪🌋🌊 (Crimson red/ Deep blue): \n")
if gate.lower() == " Crimson red":
    print("""
    Fortune favors the bold ! You've safley entered the hidden chamber.
          """)
    boxes= input("Three ancient chests are in front of you. Pick 🎁 the silver, 🎁 the dark or 🎁 the gold one: \n").lower()
    


    if boxes.lower() == "silver":

          print("Oh no! The silver box is full of hungry cobras 🐍 😋. You lost!")

    elif boxes.lower() == "dark":
          print("Watch out! Giant spiders jumped out of the dark box 🕷️🕷️ .You lost!") 

    elif boxes.lower() == "gold":
          print("Amazing! The gold box has the Golden Treasure 💰. You are rich! 🤑 ") 

    else:
          print("Wrong color! That box does not exist 🤷‍♂️🙄❔. Try again!")



elif gate.lower() == "Deep blue":
    print("CRUNCH! You walked straight into the lair of the Giant Crocodile.Game Over! 🐊 💥 ")


else:
    print("That's not an option! Are you lost in the jungle?🌴😵 ")          
                                         
                
          

