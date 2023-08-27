import random
import sys


def main():
    sys.stdout.buffer.write(b'Guess-the-number-game Start!\n')
    
    # 最小値(n) を入力する
    sys.stdout.buffer.write(b'Please enter a minimum value (n) : ')
    sys.stdout.flush()
    n = int(sys.stdin.buffer.readline())

    # 最大値(m) を入力する
    sys.stdout.buffer.write(b'Please enter a maximum value (m) : ')
    sys.stdout.flush()
    m = int(sys.stdin.buffer.readline())

    if n > m:
        return sys.stdout.buffer.write(b'Minimum (n) exceeds maximum (m)!\nExiting game...')

    # 難易度を選択する
    sys.stdout.buffer.write(b'Choose a difficulty level between 0 and 2\neasy  (Input : 0)\nmedium(Input : 1)\nhard  (Input : 2)\nInput : ')
    sys.stdout.flush()
    selectMode = int(sys.stdin.buffer.readline())

    if(selectMode == 0):
        numberOfAttempts = 15
    elif(selectMode == 1):
        numberOfAttempts = 10
    elif(selectMode == 2):
        numberOfAttempts = 5
    else:
        return sys.stdout.buffer.write(b'Could not set difficulty...\nExiting game')

    randomNum = random.randint(n,m)

    for i in range(numberOfAttempts):
        s1 = 'Time : ' + str(i+1) + '/' + str(numberOfAttempts) + '\n'
        sys.stdout.buffer.write(bytes(s1,'utf-8'))
        
        # 数字を推測する
        s2 = 'Enter a number between ' + str(n) + ' and ' + str(m) + ' : '
        sys.stdout.buffer.write(bytes(s2,'utf-8'))
        sys.stdout.flush()
        answerNum = int(sys.stdin.buffer.readline())
        
        if randomNum == answerNum:
            return sys.stdout.buffer.write(b"That's correct!\nEnd the game")
        sys.stdout.buffer.write(b"That's Incorrect\n")
    s3 = 'Game over\nThe correct answer was ' + str(randomNum) + '\n'
    return sys.stdout.buffer.write(bytes(s3,'utf-8'))


if __name__ == '__main__':
    main()