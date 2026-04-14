#Замыкание-калькулятор, накапливающее результат и поддерживающее 4 арифметичесике операции:

# 1. ДЕКОРАТОР (функция, которая принимает функцию и добавляет к ней поведение)
def decorator(func):                     # Принимает функцию calc (замыкание)
    def wrapper(x):                      # Обёртка — будет вызвана вместо calc
        old = wrapper.saved_result       # Достаём сохранённый результат
        new = func(x)                    # Вызываем оригинальную calc(x)
        print(f"{old} {wrapper.op} {x} = {new}")  # Печатаем действие
        wrapper.saved_result = new       # Обновляем сохранённый результат
        return new                       # Возвращаем новый результат
    return wrapper                       # Возвращаем обёртку вместо оригинальной функции

# 2. ФАБРИКА ЗАМЫКАНИЙ (создаёт калькулятор)
def make_calc(op, initial):              # op = "*", initial = 1
    result = initial                     # Переменная, которую "захватит" замыкание
    
    def calc(num):                       # САМО ЗАМЫКАНИЕ — видит result и op снаружи
        nonlocal result                  # Говорим: result не локальная, а из make_calc
        if op == "*":   result *= num
        elif op == "+": result += num
        elif op == "-": result -= num
        elif op == "/": result /= num
        return result                    # Возвращаем накопленный результат
    
    # 3. ПРИМЕНЯЕМ ДЕКОРАТОР
    calc = decorator(calc)               # Оборачиваем замыкание декоратором
    calc.op = op                         # Сохраняем оператор в атрибут функции
    calc.saved_result = initial          # Сохраняем начальное значение
    return calc                          # Возвращаем готовый калькулятор

# ===== ПРОВЕРКА =====
calc = make_calc("*", 1)                 # Создаём калькулятор с умножением
print(calc(5))                           # 1 * 5 = 5
print(calc(2))                           # 5 * 2 = 10