import random

def main():
    print('Guess the number game をスタートします')
    n = int(input('最小値(n)を入力してください : '))
    m = int(input('最大値(m)を入力してください : '))
    if n > m:
        return print('最小値(n)が最大値(m)を超えています!\nゲームを終了します...')

    selectMode = int(input('難易度を 0 から 2 の間で選択してください\neasy  (入力 : 0)\nmedium(入力 : 1)\nhard  (入力 : 2)\n入力 : '))

    if(selectMode == 0):
        numberOfAttempts = 15
    elif(selectMode == 1):
        numberOfAttempts = 10
    elif(selectMode == 2):
        numberOfAttempts = 5
    else:
        return print('難易度を設定できませんでした...\nゲームを終了します')

    randomNum = random.randint(n,m)

    for i in range(numberOfAttempts):
        print(str(i+1) + '/' + str(numberOfAttempts) + '回目')
        answerNum = int(input(str(n) + ' から ' + str(m) + ' の間で数字を入力してください : '))
        if randomNum == answerNum:
            return print('正解です!\nゲームを終了します〜')
        print('違います\n')
    return print('ゲームオーバー\n正解は' + str(randomNum) + 'でした〜')


if __name__ == '__main__':
    main()