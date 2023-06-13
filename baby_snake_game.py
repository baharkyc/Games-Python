from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    velocity = SIZE
#draw the player square.
    square_x = 0
    square_y = 0
    player_square = canvas.create_rectangle(square_x,square_y,
                                            square_x+SIZE, square_y+SIZE, 'blue')

#draw the goal square    
    goal_x = random.randrange(0,CANVAS_WIDTH-SIZE, SIZE)
    goal_y = random.randrange(0,CANVAS_HEIGHT-SIZE, SIZE)
    goal_square = canvas.create_rectangle(goal_x,goal_y, goal_x+SIZE, goal_y+SIZE, 'orange')
   
    travel_direction = None
    score = 0
    #create score text object.
    score_text = canvas.create_text(20, CANVAS_HEIGHT-40,font_size= 20, text='Score:' + str(score))


 #the animation loop.  
    while True:
        key = canvas.get_last_key_press()   

        # store the direction in a variable to prevent it from changing in each loop.
        if key != None:
            travel_direction = key

        # check the travel direction and change the x or y value of player_square according to the direction.
        if travel_direction == "ArrowRight":
            square_x += velocity
        elif travel_direction == "ArrowLeft":
            square_x -= velocity
        elif travel_direction == "ArrowUp":
            square_y -= velocity
        elif travel_direction == "ArrowDown":
            square_y += velocity
        
        
            
                    
        #if player hits the wall, game is over.
        if (square_x + SIZE > CANVAS_WIDTH) or (square_y + SIZE > CANVAS_HEIGHT) or (square_x < 0) or (square_y < 0):
            #print the exit screen and score.
            gameOver_text = canvas.create_text(CANVAS_WIDTH/2-50, CANVAS_HEIGHT/2,font_size=20, text='GAME OVER')
            gameOver_text = canvas.create_text(CANVAS_WIDTH/2-30, CANVAS_HEIGHT/2-20 + 40,font_size=20, text='Score: '+ str(score))
            break
        
        
        #move the player square to new location.
        canvas.moveto(player_square, square_x, square_y)

        # check if the player square ovelaps with the goal square, move the goal square to a new random coordinate
        # and add 1 to the score.
        overlapping_objs = canvas.find_overlapping(square_x, square_y, square_x + SIZE, square_y + SIZE)
        
        if goal_square in overlapping_objs:
            goal_x = random.randrange(0, CANVAS_WIDTH-SIZE, SIZE)
            goal_y = random.randrange(0,CANVAS_HEIGHT-SIZE, SIZE)
            canvas.moveto(goal_square, goal_x, goal_y)

            score +=  1
            canvas.change_text(score_text, 'Score: '+ str(score))


        time.sleep(DELAY)

    
if __name__ == '__main__':
    main()