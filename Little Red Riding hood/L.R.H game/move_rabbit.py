from pico2d import *
import move_player

# =========================== 변수 S
running = True
stage = 1
x = 800 // 2 ;   y = 90
frame = 0
bottom = 0
dir_x = 0 ;  dir_y = 0
way = 0     #이전 방향
attack = 0  # 공격 ( 물리 : 1 / 마법 : 2 )
move = 0
# =========================== 변수 E

# =========================== 키보드 입력 S

# =========================== 키보드 입력 E

# =========================== 움직임 출력 S
def draw_move_rabbit():
    global frame
    global x, y, dir_x, dir_y
    global  way
    global stage
    global move

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

    character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
    # 스테이지 3 맨 앞 오브젝트
    if stage == 3:
        tree.draw(400, 300)
    update_canvas()

    if bottom != 800:
        frame = (frame + 1) % 15
        x = dir_x*16
        y = dir_y*16

    if x == move_player.x:
        dir_x = 0
    if y == move_player.y:
        dir_y = 0

    delay(0.1)
# =========================== 움직임 출력 E

# =========================== 공격 움직임 출력 S

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
    if x < move_player.x:
        dir_x += 1
    elif x > move_player.x:
        dir_x -= 1
    elif y < move_player.y:
        dir_y += 1
    elif y > move_player.y:
        dir_y -= 1
    elif x == move_player.x and y == move_player.y:
        running = False

    draw_move_rabbit()

close_canvas()
# =========================== main E

