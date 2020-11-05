driving = input('請問你有沒有開過車？')
if driving != '有' and '沒有' :
	print('只能輸入有或沒有')
	raise SystemExit

age = input('請問你的年齡：')
age = int(age)
if driving == '有':
	if age >= 18 :
		print('通過！')
	else :
		print('你還不可以開車！')
elif driving == '沒有' :
	if age < 18:
		print('合理')
	else :
		print('是沒駕照嗎')