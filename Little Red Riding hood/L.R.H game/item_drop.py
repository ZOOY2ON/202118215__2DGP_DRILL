from random import randint
import stats_data

rabbitfoot = 0
rabbitborn = 0
slimex = 0
true = 0

random_num_rabbitfoot = 0
random_num_rabbitborn = 0
random_num_slimex = 0
# 아이템 : 토끼발 10개 / 뼈 3개 // 슬라임 핵의 조각 30개
# ---- 토끼 25마리 정도 잡으면 나올듯
# 토끼발 : 50퍼
# 토끼뼈 확률 : 20퍼
# ---- 슬라임 100마리 정도 잡으면 나올듯
# 슬라임 핵의 조각 : 50퍼

while true < 100:
    stats_data.rabbit[0] = 0
    stats_data.slime[0] = 0

    if stats_data.rabbit[0] == 0:
        random_num_rabbitfoot = randint(0, 2)
        random_num_rabbitborn = randint(0, 5)
        if random_num_rabbitfoot == 0:
            rabbitfoot += 1
        if random_num_rabbitborn == 0:
            rabbitborn += 1

    if stats_data.slime[0] == 0:
        random_num_slimex = randint(0, 2)
        if random_num_slimex == 0:
            slimex += 1

    print('---------------------------------------------')
    print(random_num_rabbitfoot)
    print(random_num_rabbitborn)
    print(random_num_slimex)
    print('---------------------------------------------')
    print('========================')
    print(rabbitfoot)
    print(rabbitborn)
    print(slimex)
    print('========================')

    true += 1
