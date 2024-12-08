import turtle
import time

def draw_heart(pen, size, color):
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.left(50)
    pen.forward(size)
    pen.circle(size/2.5, 200)
    pen.right(140)
    pen.circle(size/2.5, 200)
    pen.forward(size)
    pen.end_fill()

window = turtle.Screen()
window.bgcolor('black')
window.title('İç İçe Kalpler')

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)  # En hızlı çizim

# Kalp renkleri
colors = ['red', 'deep pink', 'crimson', 'magenta', 'hot pink', 'purple']
size = 200  # Başlangıç boyutu

# İç içe kalpler çiz
for i in range(8):
    pen.penup()
    pen.goto(0, -size/2 + i*20)  # Her kalbi biraz yukarı kaydır
    pen.setheading(0)  # Açıyı sıfırla
    pen.pendown()
    draw_heart(pen, size - i*30, colors[i % len(colors)])  # Renkleri döngüsel kullan

# Kalplerin ortasına metni yazdır
pen.penup()
pen.goto(0, 0)  # Metni ortalamak için konumlandır
pen.color('white')  # Metin rengi
pen.write("KUTAY ASLIYI SEVİYOR", align="center", font=("Arial", 24, "bold"))  # Metni yazdır

window.mainloop()