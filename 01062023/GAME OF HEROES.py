


#constants
C_BEGIN = '1'
C_EXPLANATION = '2'
C_EXIT = '3'
C_EXPLORE_BATMAN = '1'
C_STR_SCM_JESSICA = '2'

#this function prints the menu and asks for input
def get_menu_option():
    print('Welcome to "super" choices')
    print('MENU')
    print('(1) Begin')
    print('(2) Explanation')
    print('(3) EXIT')
    menu_option = input ('CHOOSE')
    return menu_option
#end get_menu option

#Jessica Jones story
def jessica_jones_story():
    print("""Good Choice! You are Jessica Jones, sitting down in a bar and enjoying your favorite drink.
          When a big a big fellow walks in, sits down next to you and starts talking.""")
    #Options for how to react
   
    print("""The guy starts talking to you. What do you do now?""")
    choice = input("""
    (1) NOTHING
    (2) SARCASM
    (3) LEAVE
    === """)
    if choice == '1':
        print ("""You ignore the guy and have another sip of your drink, why bother?
               He does not like being ignore and insists on starting a bar fight. You leave your favorite bar in bad shape""")
        print ('Your favorite bar is ruined for days - time to find a new spot.')
        print ('Regret your super hero choice - try again.')
        
    elif choice == '2': # Give a snarky comment
        print ('You make a snarky comment and the guy leaves. Finally you can enjoy your drink in peace.')
        print ('ANOTHER EVENTLESS EVENING IN YOUR FAVORITE BAR.')
        print ('Regret your super hero choice - try again.')
    elif choice =='3': # Just go home
        print ("""You are not up for dealing with people and decide to drink in the comfort of your own home.""")
        print ("ANOTHER EVENTLESS EVENING IN THE COMFORT OF YOUR OWN HOME.")
        print ('Regret your super hero choice - try again.')
    else:
        print('what else do you want to do - pick again')            


super_power=input("""Welcome to the game of heroes. Please pick your super power : 
1) To explore 
2) Make Children happy or unhappy 
3) Illogical thinking   
4) Make order out of chaos 
5) Sleep all day 
6) Superstrength and sarcasm
=== """)
#### Chose a number as an input
if super_power=='1':
    print('Woohoo !! You are Batman')
elif super_power=='2':
    print('You are Santa Claus <3')
elif super_power=='3':
    print('You are Detective Harry du Bois ')
elif super_power=='4':
    print('You are Ms. Cleanington')
elif super_power=='5':
    print('You are Winnie Pooh')
elif super_power=='6':
    jessica_jones_story() #run function
   
else:
    print('Invalid input! Please choose a number!')