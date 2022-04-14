import sys
import time

a = 2
b = 0.2
c = 0.08

def intro():
    print()
    print("(EVERYTHING IS FLASHING)")
    time.sleep(a)
    print("Everything is a blur, trying to figure exactly what happened.")
    time.sleep(a)
    print("The ground is cold, damp, and covered in glass.")
    time.sleep(a)
    print("A darkness comes across my face asking if I'm ok, why wouldn't I be, what happpened?")
    time.sleep(a)
    print("A deep wind chill flows across your body.")
    time.sleep(a)
    print("Your heart thumps harder but slower, and slower, and slower.")
    time.sleep(a)
    print("The darkness turns into light and then .")
    time.sleep(a)
    print()
    question = '"I was driving..., was I in a wreck?"'
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1.0)
    print()
    print()
    print("Blinded by the light three paths appear.")
    time.sleep(a)
    print("Three paths are revealed:")
    time.sleep(a)
    print()
    print("Path #1: Pass through the first gate covered in Silver.")
    time.sleep(a)
    print("Path #2: Pass through the second gate covered in Diamonds.")
    time.sleep(a)
    print("Path #3: Pass through the second gate made out of Steel.")
    time.sleep(a)
    print()
    firstPath = input("Which path will you choose? (1/2/3): ")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()
    elif firstPath == '3':
        print()
        path3()


def path1():
    print("You passed through the Silver Gate, into the light.")
    time.sleep(a)
    print("It's incredibly bright but your vision adjusts as you continue.")
    time.sleep(a)
    print("The gate exit closes, there's no going back now.")
    time.sleep(a)
    print("You look out and see that you're back in your old neighborhood.")
    time.sleep(a)
    print("Your old friend calls out to you.")
    time.sleep(a)
    print()
    s1 = '"Yo what is up!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...I have been thinking..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...I really think you should talk to Amber..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "She's been really looking checking you out lately..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "She's considered the most attractive girl in town."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...You should go talk to her or I will..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...However, If you are scared then I understand.\""
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)

    time.sleep(1)
    print()
    print()
    print("There are two paths to take:")
    time.sleep(a)
    print("Path #1: Go talk to her.")
    time.sleep(a)
    print("Path #2: Pass, because there are more important things.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2): ")
    if secondPath == '1':
        path1_1()
    elif secondPath == '2':
        path1_2()


def path1_1():
    print()
    print("You see Amber hanging out at the local coffee shop.")
    time.sleep(a)
    print("She's alone and the butterflies are starting to swell.")
    time.sleep(a)
    print("The sky is bright and blue and a warm breeze hits your face with the confidence you need.")
    time.sleep(a)
    s8 = '  "I really hope this works..."'
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself.')
    time.sleep(a)
    print("Amber calls out to you.")
    time.sleep(a)
    print()
    s1 = '"Hey there stranger!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...What brings you over here? I did not take you as a coffee drinker..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "You - ...Well I am not really, but I have beening thinking. Would you like to go out on a date some time?..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "Amber - ...Umm, that might be nice. I have to let you know that you will have to spoil me..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "You - ...I have always been taught to be a gentleman, you will recieve nothing less..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "Amber - ...Great, so pick a Michelin Star restuarant and let me know when you picking me up..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()
    print()
    s7 = '..."THE CHEAPEST PLATE ON THE MENU IS $100 AND I DO NOT EVEN OWN A CAR, THERE\'S NO WAY YOU CAN AFFORD THIS..."'
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    intro()


def path1_2():
    print()
    print("You decided to pass on asking Amber out.")
    time.sleep(a)
    print("And you friend was quick to take your place.")
    time.sleep(a)
    print("You are kind of jealous that he went and spoke to her but you have goals.")
    time.sleep(a)
    s1 = '  "I don\'t believe my eyes..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print()
    print("You see them out and seems to be having a great time, but your friends face is pale.")
    time.sleep(a)
    s2 = '  "Hey Bro! I did not expect to see you out."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('You see him signal you over.')
    time.sleep(a)
    print("You shake hands and use the other to embrace each other in a tight hug.")
    time.sleep(a)
    print("Your friend whispers in your ear to check your phone and you read the a series of messages.")
    time.sleep(a)
    print()
    s3 = "Hey man I really need your help."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...I really did not expect this date to become this expensive..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Can you send me some money to help cover the date?..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...This is not something I should have got myself into..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "You - I will see what I can do..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "You - I always thought she needed more attention than I could offer."
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "You - All I have to spare is a $100."
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...I am glad I did not waste time with her..."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    intro()


def path2():
    print("You passed through the Diamond Gate, into the light.")
    time.sleep(a)
    print("It's incredibly dark but your vision adjusts as you continue forward.")
    time.sleep(a)
    print("...The gate closes...")
    time.sleep(a)
    print("You turn around your realize that you are back in your old room.")
    time.sleep(a)
    print("A woman calls out to you, its your mom.")
    time.sleep(a)
    print()
    s1 = '"Come downstairs your friends are outside.'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "You - I am on my way."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "You - Hey guys what is going on?"
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "Friend(s) - There is a party tonight and wanted to see if you wanted to come."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "Friend(s) - anyone who is someone will be there. "
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "You - I am not sure, parties are not really not my thing."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "Friend(s) - Come on, you only live once."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()
    print()
    print("There are two paths to continue after the Diamond Gate:")
    time.sleep(a)
    print("Path #1: Go to the party.")
    time.sleep(a)
    print("Path #2: Stay home.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2): ")
    if secondPath == '1':
        path2_1()
    elif secondPath == '2':
        path2_2()


def path2_1():
    print()
    print("You decided to go to the party.")
    time.sleep(a)
    print("You took time to get ready and look presentable.")
    time.sleep(a)
    print("You are just hoping your social anxiety does not get the best of you.")
    time.sleep(a)
    s1 = "I have no choice, I must go..."
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print("Still going, looking good, and will be the life of the party.")
    time.sleep(a)
    print()
    s2 = '  "Whooo!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You walk up to the house where the party is taking place.')
    time.sleep(a)
    print()
    print("You walk through the doors and see everyone has been partying for while.")
    time.sleep(a)
    print("I wonder how this is going to turn out...")
    time.sleep(a)
    print()
    s3 = "Friend(s) - aye, you made it!!!..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...Friend(s) - We took bets on if you were going to show or not, I believed in you..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...You - Well I here so maybe this party will no longer be lame, ha..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...Friend(s) there is some drinks in the kitchen, pool in the back, dance party everywhere..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...What's in the drinks?..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...Friend(s) - A little bit of this and a little bit of that, wink... wink..."
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...You - I guess a couple would not hurt..."
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...Friend(s) - O NO, Its the cops, run."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    intro()

def path2_2():
    print()
    print("You decided to stay home and be productive.")
    time.sleep(a)
    print("You decided to complete a school project and a personal project.")
    time.sleep(a)
    print("You turn in early and wake up to your friend calling you telling you about the party.")
    time.sleep(a)
    s1 = '  "Who could be calling me this late...?"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print("What in the world could have happened at the party")
    time.sleep(a)
    print()
    s2 = '  "I hope nothing crazy happened!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You see its your bestfriend.')
    print()
    time.sleep(a)
    s3 = '"You - Yo, what is up. Everything good?...'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...Friend - No the cops showed up and everyone is drinking..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Friend - I think mostly everyone got away..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...Friend - I think you still should have came..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = '...You - Why would I do that and get wrapped in trouble with you guys..."'
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...Friend - It is not like I got in trouble..."
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...Friend - You have not really been fun lately and do not like to hangout much..."
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a)
    intro()


def path3():
    print("You passed through the Gate made of Steel, into the light.")
    time.sleep(a)
    print("The gate was heavy and took a lot of strength to open.")
    time.sleep(a)
    print("The gate disappears behind you with no way to return.")
    time.sleep(a)
    print("You start walking down the stairs that look very similar to your house.")
    time.sleep(a)
    print("Someone calls out to you, and it is your parents.")
    time.sleep(a)
    print()
    s1 = '"Hey, we wanted to talk to you about your future....'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...You have been good and have many options..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...I know you have always wanted to follow the footsteps of your dad and join the military..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...But you have such a bright future with your education..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Whatever decision you make we will support you..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...Have you thought about it?..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...Which way do you think you are leaning towards."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1)
    print()
    print()
    print("Path #1: Join the Army and be all you can be.")
    time.sleep(a)
    print("Path #2: Attend a prestigous university for computer science.")
    time.sleep(a)
    thirdPath = input("Which path would you like to take? (1/2) ")
    if thirdPath == '1':
        path3_1()
    elif thirdPath == '2':
        path3_2()


def path3_1():
    print()
    print('You find yourself getting off a bus that brought you to basic training.')
    time.sleep(a)
    s1 = '"People are yelling at you to hurry every corner you turn."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print("You walk through double doors into a barbershop")
    print()
    print("They sit you down and start cutting off every piece of hair.")
    time.sleep(a)
    print("The whole day continues as such until you get placed in bunks for the night your sleeping above your bunk mate...")
    time.sleep(a)
    print()
    s3 = "Did you really expect that today?..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...I hope we made the right decision..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...We will have to live out our contracts being told what to do and where to be..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...No more late wake ups for a while..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...We have to get up every morning at 5:30AM every morning for physical training..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...Maybe we will get to be stationed somewhere cool..."
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...or..."
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...You could end up at Fort Polk..."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    intro()


def path3_2():
    print()
    print('You begin walking toward your first day of class')
    time.sleep(a)
    s1 = '  "I have tired to make the best decisions for my life for the best possible ..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s2 = '  "I think this will be the best choice for me."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a)
    print("You see that there a lot of amazing that a lot of people .")
    time.sleep(a)
    print("The campus is amazing.")
    time.sleep(a)
    print("My hard work seemed to pay off and I actually able to move away.")
    time.sleep(a)
    print("I really hope to make some great connections here...")
    time.sleep(a)
    print()
    s3 = "The computer science program here is great and I am learning alot!..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...I have a good routine and getting meet a lot of new people..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Your vision is keen. You see through the darkness and the light..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...And your strength has grown from your tough choices..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...I think I want to start my own business..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...My instincts have guided me right..."
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...Doing the right thing and being focused has paid off in the long run..."
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...It just takes time to see the outcome of our choices."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(5)


# Main Function ###

print()
print()
print("     ######################")
print("     |                    |")
print("     |    Life Choices    |")
print("     |                    |")
print("     ######################")
print()
print()
time.sleep(a)
print("Wha... What happened? Where am I?")
time.sleep(a)
print("It's too dark to see anything...")
time.sleep(a)
print()
startGame = input("Would you like to start the game? (Y/N): ")
if startGame == "n" or startGame == "N":
    print("Maybe next time")
    time.sleep(3)
elif startGame == "y" or startGame == "Y":
    intro()
