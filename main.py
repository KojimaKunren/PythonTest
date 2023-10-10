import tkinter as tk
import random
import objectData

W = 1280
H = 720
counter = 0
scene = "title"
score = 0
mouse_c = False
objectX = 0
objectY = 0
objectNum = 0
objectPositionList = []
objectImageList = []
scoreList = []

#カウントダウンタイマー
def displayCounter():
    global counter
    counter -= 1
    cvs.delete("all")
    cvs.create_text(100,100, text=counter,font=("Times New Roman", 24), fill="white")
    root.after(1000,counter)

#スコア表示
def displayScore():
    global score
    cvs.create_text(W-100,200, text=score, font=("Times New Roman", 24), fill="white")

#マウスクリック押下  
def click(e):
    global scene,mouse_c
    mouse_c = True
    if mouse_c == True:
        scene = "game"

#マウスクリック離上
def release(e):
    global mouse_c
    mouse_c = False

#メイン処理
def main():
    global scene, score, counter, mouse_c

    if scene=="title":
        cvs.create_image(W/2,H/2,image=bg)
    

    if scene=="game":
            counter = 30
            displayCounter()
            displayScore()
            initObject()
    root.after(100, main)

#オブジェクト初期化
def initObject():
        global objectPositionList, objectImageList, objectNum, mouse_c
        objectCounter = obj1.num
        isNaN = False

        #オブジェクト表示
        for n in objectPositionList:
            objectX = n[0]
            objectY = n[1]
            img = objectList[n].image
            cvs.create_image(objectX, objectY, image=img)

        #オブジェクト1・click判定
        if click==True:
             score += obj1.score
             cvs.destroy_image()
             objectCounter -= 1
             if objectCounter <= 0:
                    isNaN = True

    #オブジェクトの表示位置
def placeObject():
    global objectX, objectY, objectNum, objectPositionList
    num = obj1.num
    for n in range(num):
        for m in range(1,num/2,1):
            objectX = (random.randint(1, W / (num/2))) * m
            objectY = (random.randint(1, H / (num/2))) * m
            objectPositionList = objectX , objectY
    return objectPositionList


root=tk.Tk()
root.bind("<Button>", click)
root.bind("<ButtonRelease>", release)
root.title("go")
root.geometry("1280x720")
cvs = tk.Canvas(width=W, height=H, bg="black")
bg = tk.PhotoImage(file="Test/wm.png")
cvs.pack()

obj = objectData()
objectList = [
    tk.PhotoImage(file="Test/image/obj1.png"),
    tk.PhotoImage(file="Test/image/obj2.png"),
    tk.PhotoImage(file="Test/image/obj3.png"),
    tk.PhotoImage(file="Test/image/obj4.png"),
    tk.PhotoImage(file="Test/image/obj5.png"),
    tk.PhotoImage(file="Test/image/obj6.png"),
    tk.PhotoImage(file="Test/image/obj7.png"),
    tk.PhotoImage(file="Test/image/obj8.png")
]

main()
root.mainloop()