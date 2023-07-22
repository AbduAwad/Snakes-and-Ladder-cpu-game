# Abdulrahman Awad
# Student #: 101256090

import random, pygame #Import pygame and random libraries
pygame.init() #Initialize pygame modules

#initialize global constants
block_size = 100 
(w,h) = (block_size * 6 , (block_size * 7)+50) #(600,700) 6 colums, 7 rows, each block is a 100 pixels 6 x 7
black = (0,0,0)
white = (225,225,225)
blue = (0,0,255)
red = (255,0,0)
screen = pygame.display.set_mode((w,h)) #Initialzing screen "Surface"

def text_scoreboard(text2, text3, color1, color2, x, y): #Scoreboard function
    text_font = pygame.font.Font("freesansbold.ttf", 13)  #Initializes font
    text1 = text_font.render(f"{text2} {text3}", True, color1 , color2)
    textbox1 = text1.get_rect()  # Creates a textbox
    textbox1.center = (x, y)  #Sets Textbox location
    screen.blit(text1, textbox1) # Displays text to screen

def checkerboard(): #Checkerboard function: 6 x 7 = 42
    num = 0
    for x in range (0, 6): # Iterates through 6 columns.
        for y in range (0, 7):  #Iterates throug 7 rows.
            num += 1 #Counter to increment each iteration of the loop to determine if it's even or odd.
            if (num % 2) == 0:  # if it is an even iteration of the loop the block color will be purple, otherwise it will be black.
                block_color = white
            else:
                block_color = black
            #Draw each box at specified x and y multiplied by the block size.
            pygame.draw.rect(screen, block_color,(x * block_size , y * block_size,  block_size, block_size))

def tiles(): #Extra Feature - numbered tiles Function:
    tile_num = 42 #Starts at 42 and counts down
    text_font = pygame.font.Font("freesansbold.ttf", 12) #Initializes font
    for y in range(0, 7): #Starts at top of screen and goes down
        for x in range(6, 0, -1): # Starts at far right of screen and goes left (steps negative)
            text_tile = text_font.render(f"{tile_num}", True, white , black) #Writes tile_num at specifc tile_num count
            textbox = text_tile.get_rect() # Creates a textbox
            textbox.center = ((x) * block_size - 50, (y) * block_size + 50) #Textbox Will move where the text is located based on x , y location in loop.
            screen.blit(text_tile , textbox) #Displays to screen
            tile_num -= 1 # Decrements tile_num each iteration through the loop.

def winner_display(): #Winner display - function
    screen.fill(black)
    text_font = pygame.font.Font("freesansbold.ttf", 30) #Font
    win_text = text_font.render(f"WINNER {winner}", True, winner_color , black) #Text to be displayed to screen
    textbox = win_text.get_rect() # Creates a textbox
    textbox.center = (w/2, h/2) #Place textbox at center of screen
    screen.blit(win_text, textbox) #Copies text to screen

turn_num = random.randint(1 , 2) #counter for turn determination - starts at either red or blue '1' or '2'
location_num_red = 1 #Initalizing location - indexed by number - player 1
location_num_blue = 1 #Initalizing location - indexed by number - player 2

game_on = True #Boolean for game termination
while game_on == True: # While loop for game
    
    #Turn determination if it is an odd numbered loop it will be red if not it will be blue
    if (turn_num % 2) == 0: 
        turn = 'red' # if turn red
        #2 six sided dice
        dice1 = random.randint(1, 6)  #Random integer from 1 - 6 inclusive
        dice2 = random.randint(1, 6)  #Random integer from 1 - 6 inclusive
        dice_sum = dice1 + dice2 #Set the sum of dice by adding the numbers from dice1 and dice2
        location_num_red += dice_sum #Increments Location Number for red based on dice sum
    else: 
        turn = 'blue' #if turn blue
        #2 six sided dice
        dice1 = random.randint(1, 6)  #Random integer from 1 - 6 inclusive
        dice2 = random.randint(1, 6)  #Random integer from 1 - 6 inclusive
        dice_sum = dice1 + dice2 #Set the sum of dice by adding the numbers from dice1 and dice2
        location_num_blue += dice_sum #Increments Location Number for blue based on dice sum
   
    #Sorry Collision Case:
    # For turn red - If the red location is equal to blue location and it is not the starting initial location it will send red location back to location_num 1 (start)
    if turn == 'red' and location_num_red == location_num_blue and location_num_red != 1: 
        location_num_red = 1
    #For turn blue - If the blue location is equal to red location and it is not the starting initial location it will send blue location back to location_num 1 (start)
    elif turn == 'blue' and location_num_blue == location_num_red and location_num_blue != 1:
        location_num_blue = 1

    #Row number is done in reverse so row 1 starts at the top while columns are from left to right , this is due to the way x and y values work in pygame.
    col_num_1 = (location_num_red % 6) #Column Classification - Algorithm the location number / 6, the remainder will always equal the correct column number.
    if col_num_1 == 0:
        col_num_1 = 6
    row_num_1 = (7 - (int((location_num_red-1)/6))) #Row Classification - Algorithm (7 - the (location number - 1) / 6))) will always equal to the row number.
    #Example - location_num = 12 (7 - int(((12 - 1)/6))) = 7 - (11 / 6) = 7 - 1 = 6, row num = 6 if location num = 12
    
    col_num_2 = (location_num_blue % 6) #Column Classification - Algorithm
    if col_num_2 == 0:
        col_num_2 = 6
    row_num_2 = (7 - (int((location_num_blue-1)/6))) #Row Classification - Algorithm

    #Sets location of x and y of each player based on column and row number multiplied by 100 pixels (block size)
    x_rect_1 = (col_num_1 * block_size) - 40
    y_rect_1 = (row_num_1 * block_size) - 40
    x_rect_2 = (col_num_2 * block_size) - 45 #Made it 45 so if both players overlap it is visible to the viewer.
    y_rect_2 = (row_num_2 * block_size) - 45
    
    checkerboard() #redraw the checkerboard after each turn
    tiles() #Redraw the tile number after each turn
    #Will draw the red or blue player based on turn on the screen at its specified location based on score.
    pygame.draw.rect(screen, red, (x_rect_1, y_rect_1, 20, 20)) #Player 1 - graphic
    pygame.draw.rect(screen, blue, (x_rect_2, y_rect_2, 20, 20)) #Player 2 - graphic

    # ------------------------Scoreboard-------------------------#
    #Turn
    txt1 = 'Turn: '
    txt2 = turn
    text_scoreboard(txt1, txt2, white, black, 40, 730)

    #Dice 1
    txt1 = 'Dice1: '
    txt2 = dice1 
    text_scoreboard(txt1, txt2, white, black, 140, 730)

    #Dice 2
    txt1 = 'Dice2: '
    txt2 = dice2 
    text_scoreboard(txt1, txt2, white, black, 240, 730)
 
    #Red Location #
    txt1 = 'Red Score: '
    txt2 = location_num_red 
    text_scoreboard(txt1, txt2, white, red, 370, 730)

    #Blue Location #
    txt1 = 'Blue Score: '
    txt2 = location_num_blue
    text_scoreboard(txt1, txt2, white, blue, 480, 730)
    #--------------------------------------------------------
    #Winner Condition
    if location_num_red >= 42: #If red player location number is >= 42 winner is red
        winner = 'RED'
        winner_color = red
        pygame.draw.rect(screen, red, (560, 60, 20, 20)) #Player 1 - graphic
        pygame.time.delay(1000)
        game_on = False
    elif location_num_blue >= 42: #If blue player location number is >= 42 winner is blue
        winner = 'BLUE'
        winner_color = blue
        pygame.draw.rect(screen, blue, (560, 60, 20, 20)) #Player 1 - graphic
        pygame.time.delay(1000)
        game_on = False

    turn_num += 1 #Counter for turn determination will change turn each iteration because if it odd it will be even when you add 1 and vice versa. 
    pygame.display.update() #Update Display after each turn.
    pygame.time.delay(1500) # 1.5 second delay.
    # End of main game loop

# --------------- winner - Display --------------------
winner_display() #Function call to winner display
pygame.display.update() #Updates Display for final winner screen
# -----------------------------------------------------

#Post - Condition loop to terminate screen
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit() 