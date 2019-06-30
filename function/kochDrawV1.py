# kochDrawV1.py
# 通过递归实现科赫曲线，即一段直线3等分切去中间的部分，再通过海龟作图补回一个三角形
import turtle
# size: 最开始每一个绘制科赫曲线的直线的长度，n: 几阶曲线（0 直线，1 一个突起...）
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle) # 确定科赫曲线的转向角度，调用小海龟转向方法转向，如此循环
            koch(size/3,n-1) # 当阶数>0的时候，小海龟的运动距离为1/3 size的长度，以形成科赫曲线
def main():
    turtle.setup(600,600)
    turtle.penup()
    # turtle.goto(-300,-50)
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('pink')
    # koch(600, 3) # 3阶科赫曲线，阶数
    level = 3 # 3阶科赫雪花
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
    turtle.done()
main()