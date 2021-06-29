import random  # импорт модуля псевдослучайных чисел

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]  # определение словаря существительных
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]  # словарь наречий
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]  # словарь прилагательных


def get_jokes(n, repeat=True):
    """Функция генерирует и возвращает
       шутки, взяв за основу словари,
       в количестве, указанном пользователем,
       поддерживает неповторяющиеся варианты."""
    i = 0  # счетчик шуток
    try:  # выявление исключений, мы их кажется еще не проходили, помню с видеокурса
        while i < n:  # сверка счетчика шуток с желаемым количеством
            if repeat:  # если repeat=True, слова в шутках могут повторяться
                joke = random.choice(nouns) + " " + random.choice(adverbs) + " " + random.choice(adjectives)
                #  склеивание элементов шутки в строку
                jokes.append(joke)  # добавление в список шуток
                i += 1  # обновление счетчика
            else:  # если repeat=False
                noun = random.choice(nouns)  # ввод отдельных
                adverb = random.choice(adverbs)  # переменных для каждого
                adjective = random.choice(adjectives)  # слова в шутке
                nouns.remove(noun)  # исключение повторения слова в шутке
                adverbs.remove(adverb)
                adjectives.remove(adjective)
                joke = [noun, adverb, adjective]  # формирование
                jokes.append(" ".join(joke))  # и форматирование шутки
                i += 1
    except IndexError:  # если списки со словами пустые
        print(f"Невозможно сгенерировать {n} шуток.")
        print(f"Максимальное количество неповторяющихся шуток: {len(jokes)}")
    return jokes


jokes = []
get_jokes(int(input("Введите количество шуток: ")),
          bool(input("Оставьте строку пустой, если не хотите, чтобы шутки повторялись: ")))
print(jokes)

