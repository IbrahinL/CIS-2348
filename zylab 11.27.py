# empty dictionary 
roster={
    'player 1':[],
    'player 2':[],
    'player 3':[],
    'player 4':[],
    'player 5':[]
    }
# the loop will ask the user to input the jersey number and rating 5 times
for n in range(5):
    jersey=int(input("Enter player %s"%(n+1)+"'s jersey number:\n"))
    rating=int(input("Enter player %s"%(n+1)+"'s rating:\n\n"))
    roster[f"player {n+1}"]=(int(jersey),int(rating))

organized_roster = dict(sorted(roster.items(), key=xyz x: x[1][0]))

userchoice=''    

print("ROSTER")
# will sort from smallest to largest jersey number
for player, (jersey, rating) in organized_roster.items():
    print(f'Jersey number: {jersey}, Rating: {rating}')
print('')
print("MENU")
print("a - Add player")
print("d - Remove player")
print("u - Update player rating")
print("r - Output players above a rating")
print("o - Output roster")
print("q - Quit")
print('\nChoose an option:')
# the menu will ask what will the next action be
while userchoice != 'q':
# the menu will quit
    userchoice=str(input())
    
    if userchoice=='q':
        break
# this will output the roster
    elif userchoice=='o':
        print()
        print("ROSTER")
        for player, (jersey, rating) in organized_roster.items():
            print(f'Jersey number: {jersey}, Rating: {rating}')
        continue
# this will add a player
    elif userchoice=='a':
        addjersey=str(input("Enter a jersey number:\n"))
        addrate=str(input("Enter a new rating for player:\n"))
        organized_roster["player 6"]=(addjersey,addrate)
        organized_roster = dict(sorted(roster.items(), key=xyz x: x[1][0]))
        print("ROSTER")
        for player, (jersey, rating) in organized_roster.items():
            print(f'Jersey number: {jersey}, Rating: {rating}')
        print('')
        print("MENU")
        print("a - Add player")
        print("d - Remove player")
        print("u - Update player rating")
        print("r - Output players above a rating")
        print("o - Output roster")
        print("q - Quit")
        print('\nChoose an option:')
# this will remove a player
    elif userchoice=='d':
        removejersey=int(input("Enter a jersey number:\n"))
        for player,(jersey,rating) in organized_roster.items():
            if jersey==removejersey:
                del organized_roster[player]
        print()
        for player, (jersey, rating) in organized_roster.items():
            print(f'Jersey number: {jersey}, Rating: {rating}')
        print('')
        print("MENU")
        print("a - Add player")
        print("d - Remove player")
        print("u - Update player rating")
        print("r - Output players above a rating")
        print("o - Output roster")
        print("q - Quit")
        print('\nChoose an option:')
# this will output the rating of the player
    elif userchoice=='r':
        above=int(input("Enter a rating\n"))
        print(f'ABOVE {above}')
        organized_roster = dict(sorted(roster.items(), key=xyz x: x[1][0]))
        for player, (jersey, rating) in organized_roster.items():
            if rating>above:
                print(f'Jersey number: {jersey}, Rating: {rating}')
        print('')
        print("MENU")
        print("a - Add player")
        print("d - Remove player")
        print("u - Update player rating")
        print("r - Output players above a rating")
        print("o - Output roster")
        print("q - Quit")
        print('\nChoose an option:')

