

# here is the complete map with all endings https://www.canva.com/design/DAGVQcCFVes/iZKJyrzBext6Z3wV3WrQVQ/view?utm_content=DAGVQcCFVes&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h17b5bb5702



import os

error = "NOT VALID"

def A():
    print("You wake up in a room. It is bright outside and the thatched roof drips with dew. The memories of yesterday begin pouring in again. You left your home to meet a strange person at an inn. They wanted you to help them retrive a special item for them, Dragons blood. A rare substance in this relm. He gives you a sword that has been hardened to be sharp enough to cut through dragon scales. He also mentioned that you will get a large amount of gold and silver from him. As you prepare to leave, you consolt your map. if you go straight, you can reach dragons peak is half the time, but with a more perolous path, if you go right, you can take a longer path, but more safer. Which do you choose?\n1.STRAIGHT\t2.RIGHT")
   
    a = int(input(": "))
    if a == 1:
        return 1
    elif a == 2:
        return 2
    else:
        print(error)
       
def Ba():
    print("You picked STRAGHT. You start your journy on a good note, you travel fast and light. Suddenly, a large hawk swoops down and you fend it off. It flies away but not after swiping your map! You dont know what else to do so you just tred on. You come to a tripple fork in the road. luckly, you think that most of them lead eventualy to the dragons. Where do you go?\n1.LEFT\t2.STRAIGT\t3.RIGHT")
    ba = int(input(": "))
    if ba == 1:
        return 1
    elif ba == 2:
        return 2
    elif ba == 3:
        return 3
    else:
        print(error)
       
def Bb():
    print("You picked RIGHT. It turns out the map was wrong. This path was super dangerous. probably more than the other one seeing as it says DANGER ROAD. What will you do?\n1.TRY TO FIND THE OTHER PATH\t2.CONTINUE AS FAR AS YOU CAN")
    bb = int(input(": "))
    if bb == 1:
        return 1
    elif bb == 2:
        return 2
    else:
        print(error)
def Ca():
    print("You picked LEFT\nYou continue down the left road and you see the hawk with your map! It is in a tree a little way off the road but you think you can manage it. What do you do? \n1.RETREIVE MAP\t2.CONTINUE")
    ca = int(input(": "))
    if ca == 1:
        return 1
    elif ca == 2:
        return 2
    else:
        print(error)
def Cb():
    print("You picked STRAIGHT. Its dark and daunting. you have a bad feeling that this is not the path you should have taken. What will you do?\n1.GO BACK\t2.CONTINUE")
    cb = int(input(": "))
    if cb == 1:
        return 1
    elif cb == 2:
        return 2
    else:
        print(error)
def Cc():
    print("You picked RIGHT. You go down the path and you have a felling that this is not the right path. it may literaly be the \"right\" panth but it isnt. Sorta. What do you do?\n1.GO BACK\t2.CONTINUE")
    cc = int(input(": "))
    if cc == 1:
        return 1
    elif cc == 2:
        return 2
    else:
        print(error)
def Cd():
    print("You picked CONTINUE AS FAR AS YOU CAN. As you go down the path, you dont have high hopes. There is a cabin in the distance. it is made of candy. You feel compelled to go in. A witch jump scares you and because you are already prety large because of your muscles, she cooks you and eats you. You died fast!\n(A bit too Cliche, ending 1)")
   
   
   
def Da():
    print("You picked RETREIVE MAP. You pull your sword out of its sheath and start to climb. The bird sees you! You slash at it and continue to climb. It scratches you up but you retrived the map! You get yourself on the right path and reach the dragons lair in no time. What will you do?\n1.REST AND RECOVER\t2.GO STRAIGHT INTO THE LAIR")
    da = int(input(": "))
    if da == 1:
        return 1
    elif da == 2:
        return 2
    else:
        print(error)
def Db():
    print("You picked GO BACK. You go back to try to find the fork in the road again. You cant seem to find it. You see the hawk again and this time there is no decision. you need that map. you go after the hawk and climb a tree. the hawk scratches at you and you fall to your death.\n(fall to your death, ending 2)")
   
   
   
def Dc():
    print("You picked CONTINUE. You think to yourself that its not worth the damage to retrive your map. So you continue. You notice a small sound but wave it away. You walk a short ways and around the corner is a gigantic lake! You don't remember any bodies of water on the map so this is suprising to you. There is a feint glow coming from the water. What will you do? \n1.GO BACK\t2.CLIMB A TREE\t3.GO INTO THE WATER")
    dc = int(input(": "))
    if dc == 1:
        return 1
    elif dc == 2:
        return 2
    elif dc == 3:
        return 3
    else:
        print(error)
def Dd():
    print("You picked CONTINUE. It somehow gets darker. There is a horrible feeling in your stomach and you wonder why you took this quest in the first place. You quicken your pace. faster. faster still, until you are at a dead sprint. there is a noise to your right, then the left and you trip on a root. you pull out your sword while you are on the ground and wave it in the air. it is silent again, and you continue your journy, spooked by the sounds around you. Eventualy you reatch a gigantic boulder in the path. What do you do?\n1.CLIMB IT\t2.GO OFF THE PATH")
    dd = int(input(": "))
    if dd == 1:
        return 1
    elif dd == 2:
        return 2
    else:
        print(error)

def Df():
    print("You picked GO BACK. You feel relived as you go back to the town. You go back to the tavern and the myterious man is still there. What will you do? \n1.SNEAK IN\t2.DISGUISE YOURSELF")
    df = int(input(": "))
    if df == 1:
        return 1
    elif df == 2:
        return 2
    else:
        print(error)
def Dg():
    print("You picked CONTINUE. You continue and you know this is not the right path. The hawk that stole your map must have come from here! There is a ginormous nest at least a mile wide filled  to the brim with vultures and giant hawks. There is no escape. they see you and you get eaten alive. You should have listened to your gut.\n(Gut feeling, ending 3)")
   
   
   

def Eb():
    print("You picked GO INTO THE WATER. You jump in and instantly the water freezes on your skin. But for some reason, you feel compelled to go deeper. Dispite being frozen you keep on diving. your lungs are burning but you wont swim to the surface. The last moments of your life show a glowing perl at the floor of the lake.\n(Drowned, ending 4)")
   
   
   
def Ec():
    print("You picked CLIMB A TREE. You climb the tallest tree you can find. You can see for miles. You see the dragons lair and point your compas that direction. You finaly made it. What will you do?\n1.INTO THE DRAGONS LAIR\t2.FIND ANOTHER WAY IN\t3.REST AND RECOVER")
    ec = int(input(": "))
    if ec == 1:
        return 1
    elif ec == 2:
        return 2
    elif ec == 3:
        return 3
    else:
        print(error)

def Ee():
    print("You picked GO OFF THE PATH. You shuffle through the woods and find a gigantic cave! that must have been a troll giant back there. good thing you didn't climb it! There is a lot of gold in the cave and you can take some of it. you could also just take the gold and go home. What will you do?\n1.GET MORE GOLD FROM THE DRAGONS\t2.TAKE IT AND LEAVE")
    ee = int(input(": "))
    if ee == 1:
        return 1
    elif ee == 2:
        return 2
    else:
        print(error)
def Ef():
    print("You picked CLIMB IT. You jump on and start scaling it. It wakes up and attacks! It's a Giant troll! He pulls out a club bigger than your house and stands up. his head seems to reach to the clouds. you try to attack but fail and your last thoughts are \"How would I survive the dragons if I can't even survive a troll\"\n(Killed by troll-giant, ending 5)")

def Eh():
    print("You picked TRY TO FIND THE OTHER PATH. As you rustle around in the bushed. A lion pops out. how convenient. What will you do?\n1.RUN\t2.FIGHT IT")
    eh = int(input(": "))
    if eh == 1:
        return 1
    elif eh == 2:
        return 2
    else:
        print(error)
def Ei():
    print("You picked DISGUISE. You change your cloths to look like a poor and dirty pesant. you walk in and nobody seems to care. There are a couple of people in the tavern. there are two old men and a shopkeeper who you dont pay too much attention to. who do you want to talk to? \n1.OLD MAN BY CORNER\t2.OLD MAN AT THE BAR")
    ei = input(": ")
    if ei == "1":
        return 1
    elif ei == "2":
        return 2
    elif ei != "1" or ei != "2" or ei != "" or ei != " ":
        return 3
    else:
        print(error)
def Ej():
    print("You picked SNEAK. You start in and make your way upstairs. The tavernkeeper stopsyou with his hand and grunts. he sticks his hand out and you give him a bit of gold. He leaves you and you make your way upstairs. You stay the night and in the morning the mysterious man is gone. You don't see him ever again. You later learn that he recognized you sneaking around the night before and left because the quest was actualy a bet he made with someone. Oh well, you sill live happy and live the rest of your life.\n (The truth of the quest, ending 13)")
def Fa():
    print("You picked STAY AND REST. You take a quick nap and wake up to goblins nawing on your cloths! You shake them off and get up to see them gathering. They start to eat the base of a tree and it falls down! You happen to be right in the way.\n(Smashed to death, ending 6)")
def Fb():
    print("You picked DRAGONS LAIR. It nighttime so the dragons will be less rowdy. That will make it easy to prick the dragon without it noticing. You sneak in and see one sleeping. Just your luck! there is also endless tresure soruounding it. What do you do?\n1.GET SOME DRAGON BLOOD AND LEAVE\t2.TAKE SOME GOLD WITH YOU")
    fb = int(input(": "))
    if fb == 1:
        return 1
    elif fb == 2:
        return 2
    else:
        print(error)
def Fc():
    print("You picked FIND ANOTHER WAY IN. You snoop around for a bit until you find a peice of a corner on the castle wall broken off. there is a small enough hole to crawl into. You now can go in two directions. left looks dark and daunting, right loos like the main chamber is there to get all the gold. Which way do you go?\n1.EXPLORE LEFT\t2.GET SOME GOLD")
    fc = int(input(": "))
    if fc == 1:
        return 1
    elif fc == 2:
        return 2
    else:
        print(error)
def Fd():
    print("You picked CONTINUE AND GET MORE GOLD FROM THE DRAGON.The gold weighed you down and so traveling was slower. you get there at morning and the dragons are awake! You were too greedy. the dragons burning breath scorch you before you even get close.\n(Too greedy, ending 7)")
def Fe():
    print("You picked RUN. You run. the lion was obviously faster.\n(Pure Logic, ending 8)")
def Ff():
    print("You chose to talk to THE OLD MAN IN THE CORNER. You go to talk to him.")
def Fg():
    print("You chose to talk to THE OLD MAN AT THE BAR. You sit down next to him and talk for a while. he has a family and kids and a fun life. you tell him about your family and life and how rich you are dispite your cloths not matching up with your story. the old man gets bored and leaves. there is a paper in his spot that says   \"TALK TO THE SHOP KEEPER\"   you toss it aside (though it might be hinting at something) and go over to the old man in the corner. you talk for a while.")
def Fh():
    print("You picked FIGHT IT. You underestimated the lion...s. Three more jump out from behind you and attack. You struggle but they get to you. (Death by lions, ending 15)")
def Fi():
    print("You found the secret!\nYou go over and talk to the shopkeeper because of a bit of inspiration you had. He talks with you for a while and explanes that he has been watching you and knows your situation. The quest was actualy a bet that the mysterious man made with someone, the old man in the corner. He hands you a vile of very convincing dragons blood and tells you to give it to the mysterious man. so you change out of your pesant cloths and come back to give it too him. He is suprised and says it is the most rare of all the dragons gold. he rewards you with countless amounts of gold because he won the bet.\n(Fake blood, SECRET ENDING)")
def Fj():
    print("You picked TAKE IT AND LEAVE. You decide to just embark back home with your earnings and make a good living with yourself, never bothered by the thought that the mysterious man might be looking for vengance.\n(I feel like thats cheating..., ending 12)")

def Ga():
    print("You picked GET SOME BLOOD. You pull up the scales and prick the dragon with your sword. You get a vile out and put it in. You return home and get a small amount of gold. you dont think it was worth it and wish you picked up some of that extra gold. But still, you made it out alive! \n(Made it out! without the gold, ending 9)")
def Gb():
    print("You picked TAKE SOME GOLD SOME GOLD. You gather 6 1/2 bags of gold and some blood without waking the dragon. You return home and get a sufficient prize. It was totaly worth it. (You made it out! with a hefty amount of gold, ending 10")
def Gc():
    print("You picked EXPLORE LEFT. You find an even bigger chamber filled to the top with gold! You have to take 7 trips until you are satisfied with the amount of gold. you get 32 bags filled to the top with gold and 6 viles of dragon blood. It also then occures to you that you don't have to give the mysterious man all of your stuff, you never gave him your name and he cirtainly doesnt know where you live... so you keep it. And you build your house out of gold and silver. \n(Too much gold, ending 11)")

def Ge():
    print("The man was secretly working with the other mysterious man! he recognises you and yells out to the secret man and you are caught. the mysterious man loses his bet, (refer to ending 13) and you go home in shame knowing you didn't complete the quest.\n(Shamed to death, ending 14)")
   
   
   
def haveEnding(A_):
    if int(A_) in Ending:
        return True
   
Ending = []  
Endings = []    
   
   
while True:
   
   
   
   
   
   
   
   
    a_ = A()
    if a_ == 1:
       
        b_ = Ba()
        if b_ == 1:
           
            c_ = Ca()
            if c_ == 1:
               
                d_ = Da()
                if d_ == 1:
                    if not haveEnding(6):
                        Endings.append("Smashed to death, Ending 6")
                        Ending.append(6)
                    Fa()
                   
                elif d_ == 2:
                   
                    e_ = Fb()
                    if e_ == 1:
                        if not haveEnding(9):
                            Endings.append("Made it out! without the gold, ending 9")
                            Ending.append(9)
                        Ga()
                    elif e_ == 2:
                        if not haveEnding(10):
                            Endings.append("Made it out! without a hefty amount of gold, ending 10")
                            Ending.append(10)
                        Gb()
                       
                   
            elif c_ == 2:
               
                f_ = Dc()
                if f_ == 1:
                    if not haveEnding(2):
                        Endings.append("Fall to your death, ending 2")
                        Ending.append(2)
                    Db()
                   
                elif f_ == 2:
                   
                    g_ = Ec()
                    if g_ == 1:
                        e_ = Fb()
                        if e_ == 1:
                            if not haveEnding(9):
                                Endings.append("Made it out! without the gold, ending 9")
                                Ending.append(9)
                            Ga()
                        elif e_ == 2:
                            if not haveEnding(10):
                                Endings.append("Made it out! without a hefty amount of gold, ending 10")
                                Ending.append(10)
                            Gb()
                    elif g_ == 2:
                       
                        h_ = Fc()
                        if h_ == 1:
                            if not haveEnding(11):
                                Endings.append("Too much gold, ending 11")
                                Ending.append(11)
                            Gc()
                        elif h_ == 2:
                            if not haveEnding(10):
                                Endings.append("Made it out! without a hefty amount of gold, ending 10")
                                Ending.append(10)
                            Fd()
                           
                           
                       
                    elif g_ == 3:
                        if not haveEnding(6):
                            Endings.append("Smashed to death, ending 6")
                            Ending.append(6)
                        Fa()
                       
                elif f_ == 3:
                    if not haveEnding(4):
                                Endings.append("Drowned, ending 4")
                                Ending.append(4)
                               
                    Eb()
                   
               
        elif b_ == 2:
           
       
            i_ = Cb()
            if i_ == 1:
                if not haveEnding(2):
                    Endings.append("Fall to your death, ending 2")
                    Ending.append(2)
                Db()
           
            elif i_ == 2:
                j_ = Dd()
                if j_ == 1:
                    if not haveEnding(5):
                        Endings.append("Killed by troll-giant, ending 5")
                        Ending.append(5)
                    Ef()
                   
                elif j_ == 2:
                    k_ = Ee()
                    if k_ == 1:
                        if not haveEnding(7):
                            Endings.append("Too greedy, ending 7")
                            Ending.append(7)
                        Fd()
                       
                    elif k_ == 2:
                        if not haveEnding(12):
                            Endings.append("I feel like thats cheating..., ending 12")
                            Ending.append(12)
                        Fj()
                       
                   
               
        elif b_ == 3:
           
            l_ = Cc()
            if l_ == 1:
               
                m_ = Df()
                if m_ == 1:
                    if not haveEnding(13):
                        Endings.append("The truth of the quest, ending 13")
                        Ending.append(13)
                    Ej()
                   
                elif m_ == 2:
                   
                    n_ = Ei()
                    if n_ == 1:
                        if not haveEnding(14):
                            Endings.append("Shamed to death, ending 14")
                            Ending.append(14)
                        Ff()
                        Ge()
                       
                    elif n_ == 2:
                        if not haveEnding(14):
                            Endings.append("Shamed to death, ending 14")
                            Ending.append(14)
                        Fg()
                        Ge()
                       
                    elif n_ == 3:
                        if not haveEnding(16):
                            Endings.append("{Secret ending: Fake blood}")
                            Ending.append(16)
                        Fi()
                   
                   
            elif l_ == 2:
                if not haveEnding(3):
                    Endings.append("Gut feeling, ending 3")
                    Ending.append(3)
                Dg()
           
           
    elif a_ == 2:
       
        p_ = Bb()
        if p_ == 1:
            q_ = Eh()
            if q_ == 1:
                if not haveEnding(8):
                    Endings.append("Pure logic, ending 8")
                    Ending.append(8)
                Fe()
               
            elif q_ == 2:
                if not haveEnding(15):
                    Endings.append("Death by lions, ending 15")
                    Ending.append(15)
                Fh()
        elif p_ == 2:
            if not haveEnding(1):
                Endings.append("A bit too Cliche, ending 1")
                Ending.append(1)
            Cd()
               
   
   
   
    input("Press Enter to continue\n")
   
   
    os.system("clear")
   
    print("\n1. Play again\t2.See Endings")
    x = int(input(": "))
   
    if x == 2:
        print(Endings)
        input("Press Enter to continue\n")
        os.system("clear")
       
    else:
        os.system("clear")