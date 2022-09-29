from pico2d import *


def handle_events():
    global running
    global dir_x
    global dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

def draw_obj(bottom):       # bottom : 이미지 하단까지 높이
    global frame
    global x, y
    global dir_x, dir_y

    clear_canvas()
    background.draw(400, 300)
    character.clip_draw(frame * 100, bottom, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    if x > 50:
        if x < 750:
            x += dir_x * 5
    elif x == 50:
        dir_x = 0
        x = 100
    elif x == 750:
        dir_x = 0
        x = 740

    if y > 50:
        if y < 550:
            y += dir_y * 5
    elif y == 50:
        dir_y = 0
        y = 55
    elif y == 550:
        dir_y = 0
        y = 545


    print(x)
    print(y)
    # x += dir_x * 5
    # y += dir_y * 5

    delay(0.03)

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 90
frame = 0
dir_x = 0
dir_y = 0
r_or_l = 0

while running:
    #이전 좌우 방향 확인
    if r_or_l == 1:
        r_or_l = 300
    elif r_or_l == -1:
        r_or_l = 200

    #방향에 따른 clip bottom 지정
    if dir_x == 1:
        r_or_l = 1
        draw_obj(100)
    elif dir_x == -1:
        r_or_l = -1
        draw_obj(0)
    elif dir_y != 0:
        draw_obj(r_or_l)
    elif dir_x == 0:
        draw_obj(r_or_l)
    elif dir_y == 0:
        draw_obj(r_or_l)

close_canvas()
