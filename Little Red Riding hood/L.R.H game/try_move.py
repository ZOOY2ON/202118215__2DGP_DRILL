from pico2d import *

# =========================== 키보드 입력 S
def handle_events():
    global running
    global dir_x
    global dir_y

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
# =========================== 키보드 입력 E

# =========================== 움직임 출력 S
def draw_move(bottom, cut):
    global frame
    global x, y, dir_x, dir_y
    global  way

    clear_canvas()
    background.draw(400, 300)
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
    update_canvas()

    handle_events()
    if bottom != 800:
        frame = (frame + 1) % cut

    if x >= 50 and x <= 750:
        x += dir_x*8

    if x <50:
        dir_x = 0
        x = 55
    if x>750:
        dir_x = 0
        x = 745

    if y >= 50 and y<=550:
        y += dir_y*8

    if y < 50:
        dir_y = 0
        y = 60
    if y>550:
        dir_y = 0
        y = 540

    delay(0.1)
# =========================== 움직임 출력 E

# =========================== 이미지 로딩 S
open_canvas()
background = load_image('rabbit_map.png')
character = load_image('player_all_sheet_02.png')
# =========================== 이미지 로딩 E

# =========================== 변수 S
running = True
x = 800 // 2 ;   y = 90
frame = 0
dir_x = 0 ;  dir_y = 0
way = 0     #이전 방향

player = [500, 500, 10, 20]     #HP / MP / 물리딜 / 마법딜
rabbit = [50, 10]                       #HP / 공격력
slime = [100, 2]
wolf = [225, 45, 20]                #HP / 돌진 / 손톱베기
bee = [150, 20]                      #HP / 침공격
honeycomb = 50

player_fill = 500                   #포만감
# =========================== 변수 E

# =========================== main S
while running:
    if dir_x == 1:
        draw_move(900,2)
        way = 1 #오른쪽
    elif dir_x == -1:
        draw_move(1000,2)
        way = 2 # 왼쪽
    elif dir_y == 1:
        draw_move(1100,2)
        way = 3 #위
    elif dir_y == -1:
        draw_move(1200,2)
        way = 4 #아래
    elif dir_x == 0 or dir_y == 0:
        draw_move(800,1)

close_canvas()
# =========================== main E

