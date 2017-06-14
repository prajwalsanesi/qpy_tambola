import androidhelper
import random

droid = androidhelper.Android()

def display(num , last3 ):
	droid.dialogGetInput('Tambola','Press OK',last3)
	nn = 'next number is ' + str(num)
	droid.makeToast(nn)
	droid.ttsSpeak(num_announce(num))


def num_announce(num):
	tens = 'zero'
	if num>= 10:
		tens = int(num/10)
	units = num%10
	return str(tens)+','+str(units)+','+str(num)

board = [x for x in range(1,91)]
random.seed()
random.shuffle(board)

last3 = ''
for i in range(1,91):
	if i>3:
		last3 = str(board[i-4:i-1])[1:-1]
	display( board[i] , last3 )

