# xiaozhupeiqi.py
# 画一个小猪佩奇
import turtle as t
# 鼻子
def nose(x,y):
    t.color((255,155,192), 'pink')
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(-30) # 将小乌龟的方向设置为to_angle/数字 （0-东、90-北、180-西、270-南）
    t.begin_fill() # 准备开始填充图形
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i <90:
            a = a + 0.08
            t.left(3)
            t.forward(a) # 向前走a的步长
        else:
            a = a - 0.08
            t.left(3)
            t.forward(a)
    t.end_fill() # 填充完成

    t.penup()
    t.setheading(90)
    t.forward(25)
    t.setheading(0)
    t.forward(10)
    t.pendown()
    t.pencolor(255,155,192)
    t.setheading(10)
    t.begin_fill()
    t.circle(5)
    t.color(160,82,45)
    t.end_fill()

    t.penup()
    t.setheading(0)
    t.forward(20)
    t.pendown()
    t.pencolor(255,155,192)
    t.setheading(10)
    t.begin_fill()
    t.circle(5)
    t.color(160,82,45)
    t.end_fill()

# 头
def head(x,y):
    t.color((255,155,192), 'pink')
    t.penup()
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.setheading(180)
    t.circle(300, -30)
    t.circle(100, -60)
    t.circle(80, -100)
    t.circle(150, -20)
    t.circle(60, -95)
    t.setheading(161)
    t.circle(-300, 15)
    t.penup()
    t.setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i <30 or 60 <= i <90:
            a = a + 0.08
            t.left(3)
            t.forward(a)
        else:
            a = a - 0.08
            t.left(3)
            t.forward(a)
    t.end_fill()

# 耳朵
def ears(x,y):
    t.color((255,155,192), 'pink')
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.setheading(100)
    t.circle(-50,50)
    t.circle(-10,120)
    t.circle(-50,54)
    t.end_fill()

    t.penup()
    t.setheading(90)
    t.forward(-12)
    t.setheading(0)
    t.forward(30)
    t.pendown()
    t.begin_fill()
    t.setheading(100)
    t.circle(-50,50)
    t.circle(-10,120)
    t.circle(-50,56)
    t.end_fill()

# 眼睛
def eyes(x,y):
    t.color((255,155,192), 'white')
    t.penup()
    t.setheading(90)
    t.fd(-20)
    t.setheading(0)
    t.fd(-95)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.color('black')
    t.penup()
    t.setheading(90)
    t.fd(12)
    t.setheading(0)
    t.fd(-3)
    t.pendown()
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    t.color((255,155,192),'white')
    t.penup()
    t.seth(90)
    t.fd(-25)
    t.seth(0)
    t.fd(40)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.color('black')
    t.penup()
    t.seth(90)
    t.fd(12)
    t.seth(0)
    t.fd(-3)
    t.pendown()
    t.begin_fill()
    t.circle(3)
    t.end_fill()

# 腮
def cheek(x,y):
    t.color((255,155,192))
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.seth(0)
    t.begin_fill()
    t.circle(30)
    t.end_fill()

# 嘴巴
def mouth(x,y):
    t.color(239,69,19)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.seth(-80)
    t.circle(30,40)
    t.circle(40,80)

# 身体
def body(x,y):
    t.color('red',(255,99,71))
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.seth(-130)
    t.circle(100,10)
    t.circle(300,30)
    t.seth(0)
    t.fd(230)
    t.seth(90)
    t.circle(300,30)
    t.circle(100,3)
    t.color((255,155,192), (255,100,100))
    t.seth(-135)
    t.circle(-80,63)
    t.circle(-150,24)
    t.end_fill()

# 手
def hands(x,y):
    t.color((255,155,192))
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.seth(-160)
    t.circle(300,15)
    t.penup()
    t.seth(90)
    t.fd(15)
    t.seth(0)
    t.fd(0)
    t.pendown()
    t.seth(-10)
    t.circle(-20,90)

    t.penup()
    t.seth(90)
    t.fd(30)
    t.seth(0)
    t.fd(237)
    t.pendown()
    t.seth(-20)
    t.circle(-300,15)
    t.penup()
    t.seth(90)
    t.fd(20)
    t.seth(0)
    t.fd(0)
    t.pendown()
    t.seth(-170)
    t.circle(20,90)

# 脚
def foot(x,y):
    t.pensize(10)
    t.color((240,128,128))
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.seth(-90)
    t.fd(40)
    t.seth(-180)
    t.color('black')
    t.pensize(15)
    t.fd(20)

    t.pensize(10)
    t.color((240,128,128))
    t.penup()
    t.seth(90)
    t.fd(40)
    t.seth(0)
    t.fd(90)
    t.pendown()
    t.seth(-90)
    t.fd(40)
    t.seth(-180)
    t.color('black')
    t.pensize(15)
    t.fd(20)

# 尾巴
def tail(x,y):
    t.pensize(4)
    t.color((255,155,192))
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.seth(0)
    t.circle(70,20)
    t.circle(10,330)
    t.circle(70,30)

# 参数设置
def setting():
    t.pensize(4)
    t.hideturtle()
    t.colormode(255) # 将其设置为1.0或255，随后颜色三元组的rgb值必须在0...cmode范围内
    t.color((255,255,192),'pink')
    t.setup(840,500)
    # t.sleep(10)

# main
def main():
    setting()
    nose(-100,100)
    head(-69,167)
    ears(0,160)
    eyes(0,140)
    cheek(80,10)
    mouth(-20,30)
    body(-32,-8)
    hands(-56,-45)
    foot(2,-177)
    tail(148,-155)
    t.done()

main()