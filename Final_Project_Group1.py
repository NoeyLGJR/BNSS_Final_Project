alignment = 0
player_character = "Def"
companions = []
towns = {"town 1": "Corinth","town 2":"Cathedralis","town 3": "Beezlebub",}




# Creates a selection menu for the user.
def print_menu():
    print("\nMain Menu")
    print("1. Start Game")
    print("2. Exit")




# Defining story functions/choices.
def story_1():
    print("\nWith a deep breath,", player_character, "reaches out to Dominaris and accepts the mission.\nA warm light envelops his hands as the gift of Heroes Blessing, and whispers of ancient tongues fill his mind, granting him the powers of Mental Manipulation into his being. ")
    print("\n",player_character,"is teleported to a path that  leads him to a village on the brink of despair.\nThe village almost looks like it is in shambles. The eyes or the villages look like they have lost all sense of purpose and hope. A sickness has taken hold, one that no medicine can cure.\nThe villagers eye him fear, ",player_character,"does look pretty scary, perhaps thinking he is a raider.")
    print("1: Seeing that people are in need and wanting to be just and ease their pain use Celestial Healing  to cure the villagers, potentially revealing his divine gifts to all.")
    print("2: Use Mental Manipulation to delve into the villagers’ minds, seeking the source of their affliction and attempting to free them from its grasp.")




def story_2():
    print("\nYou leave the village headed East toward the capital city of Cathedralis. The village chief explained that the church called Conclave of Sanctification reigns supreme over the land of Troika.\nThe church originally were worshipers of Plegathon, but slowly began to change, abandoning Plegathon and creating their own God to worship.\nThe Conclave of Sanctification began a holy war against the demi-humans around 13 years ago, deeming them as unholy abominations. The Vatican mercilessly persecutes any non-human species and those who support them.")
    print("\nYour journey to Cathedralis you enter a forest. You have been traveling through the forest for five days.\n You are hating yourself for not asking to take some kind of beast for transportation, you hear a loud commotion. You hear the sound of metal clashing against metal and a frightening scream.\nYou quickly run to inspect what is going on. You surprisingly find yourself at the end of the forest in a beautiful valley. You scan the area and you find what alarmed you.\nYou spot two people engaged in mortal combat. One person is a human, who looks to be dressed in some type of clerical robes bleeding on the ground crawling potentially on the verge of death.\nThe human is crying to you to save him. The other is a being who resembles a large lizard clad in bright red armor. The lizard looks at you and raises his axe prepared to deal a death blow to a defenseless human.")
    print("\n1: Cast Heal on Human!")
    print("\n2: Cast Mental Manipulation on Lizard")




def story_3():
    print("\nAs the party continues their journey toward Cathedralis, they encounter a checkpoint manned by the Conclave of Sanctification's guards. You explain who you are, and the quest given to you by Dominaris.\n You soon realize that this was a mistake. The energy of the conversation changes between you, the guards, and Seraphim Wrathborne. \nThe guards immediately take up fighting stances and cast binding magic on you. HERETIC! HERETIC! HERETIC! The guards start shouting. You look to Seraphim Wrathborne in disbelief, eyes searching for some type of answer, but you find nothing but rage and shock on his face.\n  Despite your efforts to explain your mission, you are accused of being a sympathizer of the demi-humans and branded a heretic against the church for talking about another god. As tensions rise you feel your anger and disbelief spilling over.")
    print("\n1: Fight!\n")
    print("\n2: Peacefully Comply\n")




def story_3_version_2():
    print("\nAs the party continues their journey toward Cathedralis, they encounter a checkpoint manned by the Conclave of Sanctification's guards. The guards see you with Emberton Draconis the lizard and immediately raise their weapons. \nYou explain who you are, and the quest given to you by Dominaris. You soon realize that this was a mistake. The guards are not listening at all.  The guards immediately take up fighting stances and cast binding magic on you. \nHERETIC! HERETIC! HERETIC! The guards start shouting.  Despite your efforts to explain your mission, you are accused of being a sympathizer of the demi-humans and branded a heretic against the church for talking about another god. \nAs tensions rise you feel your anger and disbelief spilling over.")
    print("\n1: Fight!\n")
    print("\n2: Peacefully Comply\n")




def story_4():
    print("\nThrown into the dungeons of Cathedralis, you find yourself in a grim and oppressive environment. The jailers, loyal to the Conclave, subject you to harsh treatment, including physical abuse, deprivation of food and water, and psychological torment.\n You cant fathom why you are being treated like this. You face your own internal struggles as you reflect on the choices that led you to this point and question if they are worth saving. \nYou curse the church and Seraphim Wrathborne. They have forgotten who Dominaris is. Can they repent you wonder? The church presents you with an option: ")
    print("\n1: Serve the church")
    print("\n2: remain in prison and wait for trial where you will most likely be executed.")


def story_4_version_2():
    print("\nThrown into the dungeons of Cathedralis, you and Emberton Draconis find themselves in a grim and oppressive environment. The jailers, loyal to the Conclave, subject them to harsh treatment, including physical abuse, deprivation of food and water, and psychological torment. \nThe party's belongings are confiscated, and they are stripped of their weapons and magical items. Separated from each other in different cells, you and Emberton Draconis must endure solitary confinement while grappling with their fears and doubts. \nEach member faces their internal struggles as they reflect on the choices that led them to this point and question their faith in their cause. \nYou hear the cries of Emberton Draconis and many other demi-humans locked away in the prison. The treatment and the horrific scenes you see have made you sick to your stomach.")
    print("\n1: Serve the church, betray Emberton Draconis.")
    print("\n2: Remain in prison and wait for trial where you and Emberton Draconis will most likely be executed.")




def story_5():
    print("\nStory text")
    print("1: 1st option")
    print("2: 2nd option")




while(True):
    print_menu()
    menu_options = input("Select 1 or 2: ")




    # Selects option 1 and asks the user to enter a name.
    if(menu_options == '1'):
        print("\nIn the land of Troika, where the shadows of conflict loom large and the echoes of divine intervention resonate through the ages, our journey begins with a choice that will shape the fate of not only our protagonist but the very fabric of this world. Dominaris the god of Troika summons his judge.")
        player_character = input("What is your name? ")
        if player_character.strip():  # Check if the input is not an empty string after removing leading/trailing spaces
            print("Meet",player_character,"a figure veiled in mystery, whose destiny intertwines with the threads of celestial powers and mortal strife. Dominaris tells you about Troika, a realm fraught with turmoil and uncertainty, and makes a decision that will set the wheels of fate in motion.\nDominaris tells ", player_character, "what he expects by appointing you as his judge.")
            break
       
    # Exits the program
    elif(menu_options == '2'):
        exit()
   
    # Catches any input besides 1 or 2 and prompts the user to try again.
    else:
        print("Invalid input. Try again.")




# Defining 1st story function/choice.




while(True):
    story_1()
    choice_1 = input("Make your choice: ")




    if(choice_1 == '1'):
        alignment += 1
        print("The people of the town look at you with thanks in their eyes. Corinth moving forward is able to rebuild, and maintain their place in this world with a renewed vigor.")
        break
   
    elif(choice_1 == '2'):
        alignment -= 1
        towns_removed = towns.pop("town 1")
        print("As you walk away from the town of Corinth, you think on all the hardships you just saved yourself and the world from by leaving the town to its fate.")
        break
    elif(choice_1) == "exit": #option to exit
        exit()
    else:
        print("Invalid input.")




# Testing alignment changes properly.
print(alignment)
#Second story choice
while(True):
    story_2()
    choice_2 = input("Make your choice: ")




    if(choice_2 == '1'):
        alignment += 1
        companions.append("Seraphim Wrathborne")
        print("\nYou cast heal on the defenseless human and immediately go into battle. You are remarkably calm about raising your sword towards the intimidating lizard. You remember about the Heroes blessing that the Dominaris gave to you. One of the powers of that blessing called (10,000 Arms) allowed you to learn fighting techniques from 10,000 combat specialists throughout time.  Your weapons clash violently. The lizard is a very capable fighter. It wields the heavy axe as if it were a mere dagger. The lizard's heavy blows are backing you down. He hits you with an overhead strike which you block but the sheer force brings you to take a knee.\nThe lizard raises his axe in preparation to deliver the final blow. As the axe begins its descent you pull out a small dagger and stab the lizard through the food causing the axe to alter its course.\nThe axe hits the ground, and the lizard lets out a loud cry. You stand up and stab the lizard killing it.")
        print("\nYou cast heal on yourself and the priestly-looking figure.You learn that the priest is a warrior for the church called an inquisitor. He was heading to the capital city when he was attacked by the lizard. He tells you his name is Seraphim Wrathborne and joins you as you head toward the capital city Cathedralis")
        break
   
    elif(choice_2 == '2'):
        alignment -= 1
        companions.append("Emberton Draconis")
        print("You cast Mental Manipulation on the lizard seeking to gain more information because you realize sometimes things are not always what they seem. Confused that he can hear your thoughts lowers his axe. You learn that the man before you is an inquisitor of the Conclave of Sanctification who has just murdered an entire village of demi-humans unprovoked.\nThe lizard had been tracking him when he finally caught up with him in the valley you see. Peering into the inquisitor's mind you confirm all that the lizard said was true and more. Such horrific atrocities the inquisitor committed in the name of the Conclave of Sanctification and Beezlebub.\nYou nod to the lizard and with a giant swing of his axe, splits the inquisitor in half.")
        print("The lizard tells you his name is Emberton Draconis and joins you on your quest as you head towards Cathedralis")#placeholder
        break
    elif(choice_2) == "exit": #option to exit
        exit()
    else:
        print("Invalid input.")




print(alignment)
#Third story choice
while(True):
    if(choice_2 == '1'):
        story_3()
        choice_3 = input("Make your choice: ")




        if(choice_3 == '1'):
            alignment += 1
            print("Fueled by righteous anger, you choose to fight and defy the guards and Seraphim Wrathborne, refusing to submit to their unjust authority and treatment of you so far. Enough is enough. \nYou charge the guards first deeming that they are probably the easier opponents. Despite your efforts, you find yourself overwhelmed by the sheer number and ferocity of your adversaries.\n Despite landing several powerful blows and fighting with Gods blessing, you are ultimately overpowered by the combined strength of the guards and Seraphim Wrathborne. \nBound and restrained, you are dragged away to face the consequences of your choices. Your treatment is driving you to hate the church.")#placeholder
            break
   
        elif(choice_3 == '2'):
            alignment -= 1
            print("Recognizing the futility of resistance in the face of overwhelming force, you choose to calm down and try to pursue a diplomatic solution. \nYou tell yourself that King will be more reasonable once you speak with him in person.\n With a steady resolve, you allow yourself to be escorted to the dungeons, where you plan to peacefully await the opportunity to clear up the misconceptions surrounding their arrest ")#placeholder
            break
        elif(choice_3) == "exit": #option to exit
            exit()
        else:
            print("Invalid input.")




    elif(choice_2 == '2'):
        story_3_version_2()
        story_3_version_2_choice = input("Make your choice: ")




        if(story_3_version_2_choice == '1'):
            alignment += 1
            print("Fueled by righteous anger, you choose to fight and defy the guards, refusing to submit to their unjust authority and treatment of you and Emberton Draconis. \nEnough is enough! You charge the guards first deeming that they are probably the easier opponents. \nDespite your efforts, your party find themselves overwhelmed by the sheer number and ferocity of your adversaries. Despite landing several powerful blows and fighting with Gods blessing, you are ultimately overpowered by the combined strength of the guards and inquisitors. \nBound and restrained, you and Emberton Draconis are dragged away to face the consequences of your choices. Your treatment is driving you to hate the church.")#placeholder
            break
   
        elif(story_3_version_2_choice == '2'):
            alignment -= 1
            print("Recognizing the futility of resistance in the face of overwhelming force, you choose to calm down and try to pursue a diplomatic solution. \nYou tell yourself that King will be more reasonable once you speak with him in person. With a steady resolve, you allow yourself to be escorted to the dungeons, where you plan to peacefully await the opportunity to clear up the misconceptions surrounding their arrest.\n You assure Emberton Draconis that everything will be ok and you will clear things up and speak on his behalf.")#placeholder
            break
        elif(choice_3) == "exit": #option to exit
            exit()
        else:
            print("Invalid input.")





#Fourth story choice
while(True):
    if(choice_2 == '1'):
        story_4()
        choice_4 = input("Make your choice: ")




        if(choice_4 == '1'):
            alignment += 1
            break
   
        elif(choice_4 == '2'):
            alignment -= 1
            break
        elif(choice_4) == "exit": #option to exit
            exit()
        else:
            print("Invalid input.")




    elif(choice_2 == '2'):
        story_4_version_2()
        story_4_version_2_choice = input("Make your choice: ")




        if(story_4_version_2_choice == '1'):
            alignment += 1
            break
   
        elif(story_4_version_2_choice == '2'):
            alignment -= 1
            break
        elif(story_4_version_2_choice) == "exit": #option to exit
            exit()
        else:
            print("Invalid input.")


while(True):
    # ending
    # basic alignment check to determine the ending        
    while(True):
        if(alignment >= 1):
            print("You pledge your allegiance to humanity and vow to defend the city against the invading demi-human army. \nYour decision to help humanity signifies to Dominaris that humans are worth saving. \nWith a great flash of light, he descends from the heavens up the battlefield. All who witness are in awe of this omnipotent being. \nDominaris tells the demi-human army to leave or they will face his wrath. \nDominaris snaps his fingers and all statues, literature, and temples dedicated to Baal begin to crumble and disintegrate across Troika")
            break
       
        elif(alignment <= -1):
            print("You pledge your allegiance to the demi-humans, recognizing their worth and standing against the oppressive ways of humanity. \nYour decision reverberates across the realms, signaling to Dominaris that humans are no longer deserving of his favor and love. \nWith a great flash of light, Dominaris descends from the heavens onto the battlefield, a radiant figure of divine power. \nAll who behold his presence are filled with awe and fear.")
            print("Dominaris curses the humans and rebukes them for their wickedness. \nHe claps his hands together mightily and unleashes a wave of energy that shakes the earth, causing all statues, literature, \nand temples dedicated to Baal, the god of humanity, to crumble and disintegrate across (world name). \nThe once mighty symbols of human pride and arrogance now lie in ruins, a testament to the consequences of their hubris. God speaks the word DEATH and all human life begins to turn into dust and fade away")
            break
       
        elif(alignment == 0):
            print("In an unexpected turn of events. You open your eyes and realize that you are infact the god of Troika.")
            break
       
    break
