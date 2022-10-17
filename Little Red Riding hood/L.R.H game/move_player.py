from pico2d import *

# =========================== 변수 S
running = True
stage = 1
x = 800 // 2 ;   y = 90
frame = 0
bottom = 0
dir_x = 0 ;  dir_y = 0
way = 0     #이전 방향
attack = 0  # 공격 ( 물리 : 1 / 마법 : 2 )
# =========================== 변수 E

# =========================== 키보드 입력 S
def handle_events():
    global running
    global dir_x ; global dir_y
    global attack
    global stage

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # 키보드가 눌러짐
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
            # 공격키
            if event.key == SDLK_q:
                attack += 1
            elif event.key == SDLK_w:
                attack -= 1

        # 키보드가 올라옴
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
            if event.key == SDLK_q:
                attack -= 1
            elif event.key == SDLK_w:
                attack += 1
# =========================== 키보드 입력 E

# =========================== 움직임 출력 S
def draw_move(bottom, cut):
    global frame
    global x, y, dir_x, dir_y
    global  way ; global attack
    global stage

    clear_canvas()
    background.draw(400, 300)

    if attack == 1:
        cut = 4
        if way == 1:
            bottom = 400
        elif way == 2:
            bottom = 500
        elif way == 3:
            bottom = 600
        elif way == 4:
            bottom = 700

    elif attack == -1:
        bottom = (way-1)*100
        cut = 4

    elif attack == 0:
        return

    attack = 0

    # === 정지 모션
    if bottom == 800:
        if way == 1:
            frame = 2
        elif way == 2:
            frame = 3
        elif way == 3:
            frame = 1
        elif way == 4:
            frame = 0
        # === 정지 모션

    character.clip_draw(frame * 100, bottom * 1, 100, 100, x, y)
    # 스테이지 3 맨 앞 오브젝트
    if stage == 3:
        tree.draw(400, 300)
    update_canvas()

    handle_events()
    if bottom != 800:
        frame = (frame + 1) % cut

    if x >= 60 and x <= 740:
        x += dir_x*16
    elif x <60:
        dir_x = 0
        x = 65
    elif x>740:
        dir_x = 0
        x = 735

    if y >= 50 and y<=550:
        y += dir_y*16

    if y < 50:
        dir_y = 0
        y = 60
    if y>550:
        dir_y = 0
        y = 540

    #attack = 0
    delay(0.1)
# =========================== 움직임 출력 E

# =========================== 공격 움직임 출력 S
def draw_attack():
    global bottom ; global cut
    global  way
    global attack

    # === 공격 방향
    if attack == 1:
        cut = 4
        if way == 1:
            bottom = 400
        elif way == 2:
            bottom = 500
        elif way == 3:
            bottom = 600
        elif way == 4:
            bottom = 700

    elif attack == -1:
        bottom = (way-1)*100
        cut = 4

    elif attack == 0:
        return

    attack = 0

    print('bot_att : ', bottom)
    print('cut_att : ', cut)
    #print('bot_att : ', bottom)
    #print('cut_att : ', cut)
        # === 공격 방향
# =========================== 공격 움직임 출력 E

# =========================== 이미지 로딩 S
open_canvas()
if stage == 1:
    background = load_image('stage_1.png')
elif stage == 2:
    background = load_image('stage_2.png')
elif stage == 3:
    background = load_image('stage_3.png')
    tree = load_image('stage_3_tree.png')
elif stage == 4:
    background = load_image('stage_4.png')
character = load_image('player_all_sheet_02.png')
# =========================== 이미지 로딩 E

# =========================== main S
while running:
    if dir_x == 1:
        bottom = 900
        cut = 2
        draw_attack()
        way = 1 #오른쪽
    elif dir_x == -1:
        bottom = 1000
        cut = 2
        draw_attack()
        way = 2 # 왼쪽
    elif dir_y == 1:
        bottom = 1100
        cut = 2
        draw_attack()
        way = 3 # 위
    elif dir_y == -1:
        bottom = 1200
        cut = 2
        draw_attack()
        way = 4 # 아래
    elif dir_x == 0 or dir_y == 0:
        bottom = 800
        cut = 1
        draw_attack()

    draw_move(bottom, cut)
   # if attack == 1:
        #draw_move(400, 4)
    #if attack == 2:
        #draw_move((way-1)*100, 4)

close_canvas()
# =========================== main E

