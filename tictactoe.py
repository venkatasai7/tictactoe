def check():
    if(board[0]==board[1]==board[2]=='X' or board[0]==board[1]==board[2]=='O'):
        print(board[0]," wins!")
        return 1;
    elif(board[3]==board[4]==board[5]=='X'or board[3]==board[4]==board[5]=='O'):
        print(board[4]," wins!")
        return 1;
    elif(board[6]==board[7]==board[8]=="X" or board[6]==board[7]==board[8]=="O"):
        print(board[7]," wins!")
        return 1;
    elif(board[0]==board[4]==board[8]=='X' or board[0]==board[4]==board[8]=='O'):
        print(board[4]," wins!")
        return 1;
    elif(board[2]==board[4]==board[6]=='X' or board[2]==board[4]==board[6]=='O'):
        print(board[4]," wins!")
        return 1;
    elif(board[0]==board[3]==board[6]=='X'or board[0]==board[3]==board[6]=='O'):
        print(board[3]," wins!")
        return 1;
    elif(board[1]==board[4]==board[7]=='X' or board[1]==board[4]==board[7]=='O'):
        print(board[4]," wins!")
        return 1;
    elif(board[2]==board[5]==board[8]=='X' or board[2]==board[5]==board[8]=='X'):
        print(board[5]," wins!")
        return 1;
    else:
        return 0;
    
def display():
    count=0
    for i in board:
        count=count+1
        print(i,end="  |")
        if(count== 3 or count== 6 or count== 9 ):
            print("\n")
            
board=['_','_','_','_','_','_','_','_','_']
print("WELCOME! TO\nTIC-TAC-TOE!!")
while(1):
    turn=0
    board=['_','_','_','_','_','_','_','_','_']
    print("do you want to play game:Y or N:",end=" ")
    ch=input()
    if ch=="Y" or ch=="y":
        while(1):
            display()
            print("enter your choice:",end=" ")
            j=int(input())
            turn=turn+1
            board[j-1]='X'
            display()
            if(check()==1):
                break
            if(turn == 9):
                print("draW")
                break;
            print("enter your choice:")
            k=int(input())
            turn=turn+1
            board[k-1]='O'
            if(check()==1):
                break
    else:
        break;
