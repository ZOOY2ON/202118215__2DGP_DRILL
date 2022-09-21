from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

count = 0
x=400
y = 90

while (count < 4):
          if(count == 0):
                    count = count + 1
                    while(x<650):
                              clear_canvas_now()
                              grass.draw_now(400,30)
                              character.draw_now(x, y)
                              x = x+0.2
                              y = y+0.2
                              delay(0.01)
                              
          elif(count == 1):
                    count = count + 1
                    while(x>400):
                              clear_canvas_now()
                              grass.draw_now(400,30)
                              character.draw_now(x, y)
                              x = x-0.2
                              y = y+0.2
                              delay(0.01)
                              
          elif(count == 2):
                    count = count + 1
                    while(x>150):
                              clear_canvas_now()
                              grass.draw_now(400,30)
                              character.draw_now(x, y)
                              x = x-0.2
                              y = y-0.2
                              delay(0.01)

          elif(count == 3):
                    count = count + 1
                    while(x<400):
                              clear_canvas_now()
                              grass.draw_now(400,30)
                              character.draw_now(x, y)
                              x = x+0.2
                              y = y-0.2
                              delay(0.01)


close_canvas()
