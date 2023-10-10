import tkinter as tk
import random

W = 1280  # 画面横サイズ
H = 720  # 画面縦サイズ
counter = 30  # 時間経過
scene = "title"  # シーン切り替え用
score = 0  # スコア
mouse_c = False  # マウスクリック
index = 0  # 配列用
targetX = W / 2  # ターゲットX座標
targetY = H / 2  # ターゲットY座標
targetNum = 0  # ターゲット個数確認用
targetList = []  # ターゲットリスト
targetCurrentList = []
tragetImageList = []  # ターゲット画像リスト
targetPositionList = []  # ターゲット座標リスト
isNaN = 0  # ターゲット処理確認用


# ターゲット
class Target:
    def __init__(self, name, num, score, image):
        self.name = name
        self.num = num
        self.score = score
        self.image = image


# ターゲットリスト入力
targetList = [
    Target("target1", 1, 1, "targetImageList[1]"),
    Target("target2", 2, 2, "targetImageList[2]"),
    Target("target3", 4, 16, "targetImageList[3]"),
    Target("target4", 8, 32, "targetImageList[4]"),
    Target("target5", 16, 64, "targetImageList[5]"),
]


# カウントダウンタイマー
def displayCounter():
    global counter
    counter -= 1
    cvs.delete("all")
    cvs.create_text(100, 100, text=counter, font=("Times New Roman", 24), fill="black")
    root.after(1000, displayCounter)


# スコア表示
def displayScore():
    global score
    cvs.create_text(
        W - 100, 200, text=score, font=("Times New Roman", 24), fill="black"
    )


# マウスクリック押下
def click(e):
    global scene, mouse_c
    mouse_c = True


# マウスクリック離上
def release(e):
    global mouse_c
    mouse_c = False


# メイン処理
def main():
    global scene, score, counter, mouse_c, isNaN

    if scene == "title":
        cvs.create_image(W / 2, H / 2, image=bg, tag="TITLE")
        if mouse_c == True:
            scene = "game"
            isNaN = True
            cvs.delete("TITLE")

    if scene == "game":
        displayCounter()
        displayScore()

        if isNaN == True:
            initTarget()
            if clickTarget():
                index += 1
        root.after(1000, main)


# オブジェクト初期化
def initTarget():
    global targetPositionList, targetList, targetNum, index, isNaN, targetX, targetY
    targetNum = targetList[index].num
    if index > 0:
        targetPositionList = placeTarget()
        # オブジェクト表示
        for n in targetPositionList:
            targetX = n[0]
            targetY = n[1]
            img = targetList[index].image
            cvs.create_image(targetX, targetY, image=img, tag="TAG")
    else:
        cvs.create_image(targetX, targetY, image=img1, tag="TAG")


# オブジェクトクリック判定
def clickTarget():
    global targetList, mouse_c, isNaN, targetNum
    isNaN = False

    if click == True:
        score += targetList[index].score
        cvs.delete("TAG")
        targetNum -= 1
        if targetNum <= 0:
            isNaN = True
    return isNaN


# オブジェクトの表示位置
def placeTarget():
    global targetX, targetY, targetNum, targetPositionList, index
    num = targetList[index].num
    for m in range(1, num / 2, 1):
        targetX = int(random.randint(1, W / (num / 2))) * m
        targetY = int(random.randint(1, H / (num / 2))) * m
        targetPositionList = targetX, targetY
    return targetPositionList


root = tk.Tk()
root.bind("<Button>", click)
root.bind("<ButtonRelease>", release)
root.title("go")
root.geometry("1280x720")

# ターゲット画像
img1 = tk.PhotoImage(file="PythonTest/image/obj1.png")
img2 = tk.PhotoImage(file="PythonTest/image/obj2.png")
img3 = tk.PhotoImage(file="PythonTest/image/obj3.png")
img4 = tk.PhotoImage(file="PythonTest/image/obj4.png")
img5 = tk.PhotoImage(file="PythonTest/image/obj5.png")

# ターゲット画像リスト入力
targetImageList = [img1, img2, img3, img4, img5]

bg = tk.PhotoImage(file="PythonTest/image/c1.png")
cvs = tk.Canvas(width=W, height=H, bg="white")
cvs.create_image(W / 2, H / 2, image=bg, tag="TITLE")
cvs.pack()

main()
root.mainloop()
