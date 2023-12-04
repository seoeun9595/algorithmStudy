def solution(keyinput, board):
    xlimit = board[0] // 2
    ylimit = board[1] // 2
    x, y = 0, 0
    for i in keyinput:
        if i == "left" and x > -(board[0] // 2):
            x -= 1
        elif i == "right" and x < (board[0] // 2):
            x += 1
        elif i == "up" and y < (board[1] // 2):
            y += 1
        elif i == "down" and y > -(board[1] // 2):
            y -= 1
    return [x, y]
            
            