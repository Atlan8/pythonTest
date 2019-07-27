# digitalTube 数码管
import turtle, time
# 添加间隔
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):
    # 在开始和结束之前添加间隔
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigital(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,4,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    # 从中间的一段开始画，画完一圈刚好是0
    # 然后调整方向，从左边往上画
    '''
    |一|
    '''
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)

    # 完成一个数字，然后向左旋转180度，准备画下一个数字
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawData(data):
    '''
    for i in data:
        drawDigital(eval(i))
    '''
    # data为日期，格式为 ’%Y-%m=%d+‘
    turtle.pencolor('red')
    for i in data:
        if i == '-':
            turtle.write('年',font=('Arial', 18, 'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=('Arial', 18, 'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=('Arial', 18, 'normal'))
        else:
            drawDigital(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-330)
    turtle.pensize(5)
    # drawData('20190619')
    drawData(time.strftime('%Y-%m=%d+', time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()