from pico2d import *
open_canvas()
moon = load_image('moon.png')
character = load_image('rabbit_cookie_sheet.png')
end = load_image('end.png')

action = 0
x = 0
frame = 0

num_f = 0   # range : first num
num_l = 0   # range : last num = num_f + speed*cut
speed = 0
bottom = 0
cut = 0

delay(3)

# --- 그리기 함수
def about_draw ( num_f, num_l, speed, bottom, cut):
    frame = 0
    for x in range (num_f, num_l+1, speed):
        clear_canvas()
        moon.draw(400, 30)
        character.clip_draw(frame * 300, bottom, 300, 300, x, 190)
        update_canvas()
        frame = (frame + 1) % cut
        delay (0.1)
        get_events()

# --- no.2 action
while (action == 0):
    print(0)
    about_draw (0, 60, 3, 2700, 12)
    if(x == num_l):
        action = action+1

# --- no.4 action
while (action == 1):
    print(1)
    about_draw (60, 81, 3, 2100, 7)
    if(x == num_l):
        action = action+1

# --- no.3 action
while (action == 2):
    print(2)
    about_draw(81, 141, 5, 2400, 12)
    if(x == num_l):
        action = action+1

# --- no.5 action
while (action == 3):
    print(3)
    about_draw(141, 163, 2, 1800, 11)
    if(x == num_l):
        action = action+1

# --- no.1 action
while (action == 4):
    print(4)
    about_draw(163, 228, 5, 3000, 13)
    if(x == num_l):
        action = action+1

# --- no.7 action
while (action == 5):
    print(5)
    about_draw(228, 234, 1, 1200, 6)
    if(x == num_l):
        action = action+1

# --- no.6 action
while (action == 6):
    print(6)
    about_draw(234, 258, 2, 1500, 12)
    if(x == num_l):
        action = action+1

# --- no.8 action
while (action == 7):
    print(7)
    about_draw(258, 268, 1, 900, 10)
    if(x == num_l):
        action = action+1



# --- no.9 action
while (action == 8):
    print(8)
    about_draw(268, 343, 15, 600, 5)
    if(x == num_l):
        action = action+1

# --- no.10 action
while (action == 9):
    print(9)
    about_draw(343, 593, 25, 300, 10)
    if(x == num_l):
        action = action+1

# --- no.11 action
while (action == 10):
    print(10)
    about_draw(593, 648, 6, 0, 10)
    if(x == num_l):
        action = action+1

# --- no.1 action
while (action == 11):
    print(11)
    about_draw(648, 850, 10, 3000, 9)
    if(x == num_l):
        print('last')
        about_draw(850, 800, -10, 0, 2)
        if(x == num_l):
            end.draw_now(600, 150)
            delay(3)
            close_canvas()
