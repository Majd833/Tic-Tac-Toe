theboard={1:" ",2:" ",3:" ",
          4:" ",5:" ",6:" ",
          7:" ",8:" ",9:" "}
board_keys=[]
for key in theboard:
    board_keys.append(key)
def printboard():
    print(theboard["7"]+"|"+theboard["8"]+"|"+theboard["9"])
    print("-"+"+"+"-"+"+"+"-")
    print(theboard["4"]+"|"+theboard["5"]+"|"+theboard["6"])
    print("-"+"+"+"-"+"+"+"-")
    print(theboard["1"]+"|"+theboard["2"]+"|"+theboard["3"])
def game():
    turn="X"
    count="O"
    for i in range(10):
        print("It's your turn",turn)
        printboard(theboard)
        move=input()
        if theboard[turn]