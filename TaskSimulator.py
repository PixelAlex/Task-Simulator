#Тренажер по задачам

def end():
	print('\t\t\nВы все решили! Спасибо, что пользовались нашей программой!')

def mzadacha1():
	print('Задача 1. Чему будет равно выражение 50*(30+5).')
	answer1 = int(input())
	if answer1 == 1750:
		print('Молодец! Верно!\n')
	else:
		print('Неверно, попробуй еще раз\n')
		mzadacha1()
		
def mzadacha2():
	print('Задача 2. Напиши уравнение прямой в координатной плоскости.')
	answer2 = str(input())
	answer2 = answer2.replace(' ', '')
	if answer2 == 'y=kx+l' or answer2 == 'y=kx+b' or answer2 == 'y=k*x+l' or answer2 == 'y=k*x + b':
		print('Молодец! Верно!\n')
	else:
		print('Неверно, попробуй еще раз\n')
		mzadacha2()
		
def pzadacha1():
	print('Задача 1. Напиши закон Ома.')
	answer1 = str(input())
	answer1 = answer1.replace(' ', '')
	if answer1 == 'U/R' or answer1 == 'U:R' or answer1 == 'I=U:R' or  answer1 == 'I=U/R' or answer1 == 'U/R=I' or answer1 == 'U:R=I':
		print('Молодец! Верно!\n')
	else:
		print('Неверно, попробуй еще раз\n')
		pzadacha1()
		
def pzadacha2():
	print('Задача 2. Напиши формулу нахождения силы тока(не использовать Закон Ома).')
	answer2 = str(input())
	answer2 = answer2.replace(' ', '')
	if answer2 == 'q/t' or answer2 == 'q:t' or answer2 == 'I=q/t' or  answer2 == 'I=q:t' or answer2 == 'q/t=I' or answer2 == 'q:t=I':
		print('Молодец! Верно!\n')
	else:
		print('Неверно, попробуй еще раз\n')
		pzadacha2()		
		
def math():
	print('\nЗадачи по математике\n')
	mzadacha1()
	mzadacha2()
	print('\nЗадачи по математике закончились :(\n')
	answer = str(input('Если хочешь решить задачи по физике, введи 1, если нет, то просто введи любую букву\t'))
	answer = answer.replace(' ', '')
	if  answer == '1':
		physics()
	else:
		end()
	
def physics():
	print('\nЗадачи по физике\n')
	pzadacha1()
	pzadacha2()
	print('\nЗадачи по физике закончились :(\n')
	answer = str(input('Если хочешь решить задачи по математике, введи 1, если нет, то просто введи любую букву\t'))
	answer = answer.replace(' ', '')
	if  answer == '1':
		math()
	else:
		end()
		
def main():
	predmet = int(input('Выбери предмет! \nДля того, чтобы выбрать математику, введите 1.\nДля того, чтобы выбрать физику, введите 2\t'))
	if predmet == 1:
		math()
	elif predmet == 2:
		physics()
	else:
		print('\nВведенные вами данные не верны!\n')
		main()

	
print('\t\tТренажер по задачам!\n')
main()