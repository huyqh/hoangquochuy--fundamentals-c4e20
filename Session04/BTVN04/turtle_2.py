from turtle import*
speed(-1)
color("blue")
left(135)
for i in range(50):
    for j in range(4):
        forward(100-2*i)
        left(90)
    right(10)
mainloop()