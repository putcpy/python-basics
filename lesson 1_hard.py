# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!
firstname = str(input("Ваше имя? "))
lastname = str(input("Ваша фамилия? "))
age = int(input("Ваш возраст? "))
weight = int(input("Ваш вес? "))
info = str(firstname + " " + lastname + ". Возраст: "+ str(age) + ", Вес: " + str(weight))
if age > 40 and (weight > 120 or weight < 50) :
    print(info + '. Вам срочно нужно обратиться к врачу')
elif age < 40 and weight > 120:
    print(info + '. Пора начать бегать')
elif age < 40 and weight < 50:
    print(info + '. Пора начать есть')
else:
    print(info + '. Отличная форма. Так держать')