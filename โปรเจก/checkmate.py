def checkmate(board):  
    rows = board.splitlines()

    # ตรวจสอบความกว้างของกระดานให้เท่ากัน
    row_length = len(rows[0])
    i = 0
    while i < len(rows):
        if len(rows[i]) != row_length:
            print("Fail")
            return
        i += 1

    # หาตำแหน่งของราชา
    king_position = None
    i = 0
    while i < len(rows):
        if 'K' in rows[i]:
            king_position = (i, rows[i].index('K'))
            break
        i += 1

    if not king_position:
        print("Error")
        return

    x, y = king_position  # ตำแหน่งของราชา

    # ฟังก์ชันตรวจสอบการโจมตี
    def check_direction(dx, dy, pieces):
        i, j = x + dx, y + dy
        while 0 <= i < len(rows) and 0 <= j < len(rows[0]):
            if rows[i][j] in pieces:
                return True
            if rows[i][j] != '.':
                break
            i += dx
            j += dy
        return False

    # ตรวจสอบเบี้ย
    if x + 1 < len(rows):
        if (y - 1 >= 0 and rows[x + 1][y - 1] == 'P') or (y + 1 < row_length and rows[x + 1][y + 1] == 'P'):
            print("Success")
            return

    # ตรวจสอบการโจมตีจากเรือ (R), ราชินี (Q) แนวตรงและแนวนอน
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    i = 0
    while i < len(directions):
        if check_direction(directions[i][0], directions[i][1], {'R', 'Q'}):
            print("Success")
            return
        i += 1

    # ตรวจสอบการโจมตีจากบิชอป (B), ราชินี (Q) แนวทแยง
    diagonals = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    i = 0
    while i < len(diagonals):
        if check_direction(diagonals[i][0], diagonals[i][1], {'B', 'Q'}):
            print("Success")
            return
        i += 1

    print("Fail")
