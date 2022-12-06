field = list(range(1,10))
def draw(field):
    print('-' * 13)
    for i in range(3):
        print('|', field[0 + i*3], '|', field[1 + i*3], '|', field[2 + i*3], '|')
    print('-' * 13)

def take_input(pl_xo):
    valid = False
    while not valid:
        pl_answer = input(f'Куда поставим {pl_xo}?')
        try:
            pl_answer = int(pl_answer)
        except:
            print("Введите число.")
            continue
        if pl_answer >= 1 and pl_answer <=9:
            if str(field[pl_answer-1]) not in "X0":
                field[pl_answer-1] = pl_xo
                valid = True
            else:
                print('Эта клетка занята.')
        else:
            print('Введите число от 1 до 9.')


def chek_win(field):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))  # кортеж с выигрышными координатами
    for c in win_coord:
        if field[c[0]] == field[c[1]] == field[c[1]]:
            return field[c[0]]
    return False


def main(field):
    counter = 0
    win = False
    while not win:
        draw(field)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1
        if counter > 4:
            s = chek_win((field))
            if s:
                print(s, 'Вы выиграли!')
                win = True
                break
        if counter == 9:
            print('Ничья.')
            break

    draw(field)


main(field)
