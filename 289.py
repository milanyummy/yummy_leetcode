import copy
def gameOfLife(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    #非原地算法
    # width = len(board[0])
    # height = len(board)

    # board_padding = copy.deepcopy(board)#采用补零解决边界问题
    # board_padding.insert(0, [0]*(width+2))
    # board_padding.append([0]*(width+2))
    # for i in range(1, height+1):
    #     board_padding[i].insert(0, 0)
    #     board_padding[i].append(0)
    
    # for i in range(height):
    #     for j in range(width):
    #         now = board[i][j]
    #         alive = sum( map(sum, [board_padding[i][j:j+3], board_padding[i+1][j:j+3], board_padding[i+2][j:j+3]] ) )#获取周围八格（包括自身）的细胞存活情况
    #         if now == 0:
    #             if alive == 3:
    #                 board[i][j] = 1
    #         else:
    #             alive -= 1
    #             if alive < 2:
    #                 board[i][j] = 0
    #             elif alive >3:
    #                 board[i][j] = 0
    
    #原地算法，官方思路
    width = len(board[0])
    height = len(board)  
    neighbors = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]#方向数组，八个方向
    for i in range(height):
        for j in range (width):
            alive = 0
            # 对于每一个细胞统计其八个相邻位置里的活细胞数量
            for neighbor in neighbors:
                #相邻位置的坐标
                r = i + neighbor[0]
                c = j + neighbor[1]
                if (r >= 0 and r < height) and (c >=0 and c < width) and abs(board[r][c]) == 1:
                    alive += 1
             
            if board[i][j] == 0:
                if alive == 3:
                    board[i][j] = 2 #规则4；    2 代表这个细胞过去是死的现在活了
            else:
                if alive < 2 or alive >3 :
                    board[i][j] = -1 #规则1，规则3；    -1 代表这个细胞过去是活的现在死了
    for i in range(height):
       for j in range (width):
            if board[i][j] > 0:
               board[i][j] = 1
            else:
                board[i][j] = 0
    
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
gameOfLife(board)
print(board)