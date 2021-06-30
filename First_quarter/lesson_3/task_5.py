import random  # импорт модуля псевдослучайных чисел

NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]  # определение словаря существительных
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]  # словарь наречий
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]  # словарь прилагательных
# upd замена переменных константами


def get_jokes(n, repeat=True):
    """Функция генерирует и возвращает
       шутки, взяв за основу словари,
       в количестве, указанном пользователем,
       поддерживает неповторяющиеся варианты."""
    nouns2 = NOUNS.copy()  # upd копии глобальных констант
    adverbs2 = ADVERBS.copy()
    adjectives2 = ADJECTIVES.copy()
    jokes = []  # upd объявление списка с шутками внутри функции
    i = 0  # счетчик шуток
    try:  # выявление исключений, мы их кажется еще не проходили, помню с видеокурса
        while i < n:  # сверка счетчика шуток с желаемым количеством
            if repeat:  # если repeat=True, слова в шутках могут повторяться
                joke = random.choice(nouns2) + " " + random.choice(adverbs2) + " " + random.choice(adjectives2)
                #  склеивание элементов шутки в строку
                jokes.append(joke)  # добавление в список шуток
                i += 1  # обновление счетчика
            else:  # если repeat=False
                noun = random.choice(nouns2)  # ввод отдельных
                adverb = random.choice(adverbs2)  # переменных для каждого
                adjective = random.choice(adjectives2)  # слова в шутке
                nouns2.remove(noun)  # исключение повторения слова в шутке
                adverbs2.remove(adverb)
                adjectives2.remove(adjective)
                joke = [noun, adverb, adjective]  # формирование
                jokes.append(" ".join(joke))  # и форматирование шутки
                i += 1
    except IndexError:  # если списки со словами пустые
        print(f"Невозможно сгенерировать {n} шуток.")
        print(f"Максимальное количество неповторяющихся шуток: {len(jokes)}")
    return jokes


print(get_jokes(int(input("Введите количество шуток: ")),  # upd возвращение результата функции без переменной
                bool(input("Оставьте строку пустой, если не хотите, чтобы шутки повторялись: "))))
