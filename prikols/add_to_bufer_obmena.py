#Импортируем pyperclip
import pyperclip
def extract_answer(text):
    return (text.strip().split()[-1])
#Делаем переменную text с информацией
text = "Congrats, you've passed the task! Copy this code as the answer for Stepik quiz: 28.13231BALLS59720265"
answer = extract_answer(text)
print(extract_answer(text))
#Делаем функцию которая принимает переменную text

pyperclip.copy((text.strip().split()[-1])) #Копирует в буфер обмена информацию


#Вызываем функцию записи в буфер обмена
print((text.strip().split()[-1]))

#Наслаждаемся результатом