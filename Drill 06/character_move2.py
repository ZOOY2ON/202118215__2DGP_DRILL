from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

count = 0
x=400
y = 90

while (count < 5):
          if(count == 0):
                    count = count + 1
                    while(x<790):
                              clear_canvas_now()
                              grass.draw_now(400,30)
                              character.draw_now(x, 90)
                              x = x+2
                              delay(0.01)
                              
          elif(count == 1):
                    count = count + 1
                    while(y<580):
                              clear_canvas_now()
                              grass.draw_now(400,30)
                              character.draw_now(790, y)
                              y = y+2
                              delay(0.01)
                              
          elif(count == 2):
                    count = count + 1
                    while(x>5):
                              clear_canvas_now()
                              grass.draw_now(400,30)
                              character.draw_now(x, 580)
                              x = x-2
                              delay(0.01)

          elif(count == 3):
                    count = count + 1
                    while(y>90):
                              clear_canvas_now()
                              grass.draw_now(400,30)
                              character.draw_now(5, y)
                              y = y-2
                              delay(0.01)

          elif(count == 4):
                    count = count + 1
                    while(x<400):
                              clear_canvas_now()
                              grass.draw_now(400,30)
                              character.draw_now(x, 90)
                              x = x+2
                              delay(0.01)

close_canvas()
