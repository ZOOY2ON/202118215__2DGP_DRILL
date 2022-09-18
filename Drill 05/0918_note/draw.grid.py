import turtle

turtle.reset()

#draw horisonal lines - 가로줄 그리기
y = -100
while y <= 400:
    turtle.penup()
    turtle.goto(0,y)
    turtle.pendown()
    turtle.goto(500,y)
    y += 100


#draw vertical lines - 세로줄 그리기
x = 0
while x<= 500:
    turtle.penup()
    turtle.goto(x,-100)
    turtle.pendown()
    turtle.goto(x,400)
    x += 100


# 코드 확인 테스트  할  때

# ** test lead time ** : 내가 확인 하고자 하는 부분까지 오기 위해 앞에 걸리는 테스트 수행 시간
# test lead time이 길수록 코드를 짜는 시간도 길어지게 된다.

# 의견 1 : 필요없는 소스 코드부분을 주석처리하기
