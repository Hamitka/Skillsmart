class HashTable:
    """
    В классе хэш-таблицы потребуются два параметра:
    размер хэш-таблицы (желательно простое число,
    для экспериментов можно например брать 17 или 19),
    и длину шага (количество слотов) для поиска следующего свободного слота (например, 3)
    """

    def __init__(self, size, step):
        self.size = size
        self.step = step
        self.slots = [None] * self.size

    def hash_fun(self, value):
        """
        - хэш-функцию hash_fun(value), которая по входному значению вычисляет индекс слота;
        """
        # в качестве value поступают строки!
        # всегда возвращает корректный индекс слота
        # return hash(value) % self.size
        return sum([ord(value[i]) * (i + 1) for i in range(len(value))]) % self.size

    def seek_slot(self, value):
        """
        - функцию поиска слота seek_slot(value),
        которая по входному значению сперва рассчитывает индекс хэш-функцией,
        а затем отыскивает подходящий слот для него с учётом коллизий,
        или возвращает None, если это не удалось;
        """
        # находит индекс пустого слота для значения, или None
        slot_candidate = self.hash_fun(value)

        while None in self.slots:
            if self.slots[slot_candidate] is None:
                return slot_candidate
            else:
                slot_candidate = (slot_candidate + self.step) % self.size
        return None

    def put(self, value):
        """
        - put(value), который помещает значение value в слот,
        вычисляемый с помощью функции поиска;
        """
        # записываем значение по хэш-функции
        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
            return slot
        return None

    def find(self, value):
        """
        - find(value), который проверяет, имеется ли в слотах указанное значение,
        и возвращает либо слот, либо None."""
        # находит индекс слота со значением, или None
        if value in self.slots:
            return self.slots.index(value)
        return None


class NativeDictionary:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        return sum([ord(key[i]) * (i + 1) for i in range(len(key))]) % self.size
        # return sum(key.encode('utf-8')) % self.size

    def is_key(self, key):
        """
        - is_key(key) - проверка, имеется ли в слотах такой ключ
        """
        # возвращает True если ключ имеется,
        # иначе False
        if key in self.slots:
            return True
        return False

    def put(self, key, value):
        """
        - put(key, value) - сохранение внутри класса ассоциативного массива
        пары ключ-значениепо описанной выше схеме;"""
        # гарантированно записываем
        # значение value по ключу key
        index = self.hash_fun(key)
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        """
        - get(key) - поиск и извлечение значения по ключу, или None, если ключ не найден.
        """
        # возвращает value для key,
        # или None если ключ не найден
        if self.is_key(key):
            return self.values[self.hash_fun(key)]
        return None


# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:

    def __init__(self):
        # ваша реализация хранилища
        self.values = []
        self.length = 0

    def size(self):
        # количество элементов в множестве
        return self.length

    def put(self, value):
        # всегда срабатывает
        i = 0
        if value not in self.values:
            if not self.values or value > self.values[-1]:
                self.values.append(value)
            else:
                while value > self.values[i] and i < self.length:
                    i += 1
                self.values.insert(i, value)
            self.length += 1

    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        if value in self.values:
            return True
        return False

    def remove(self, value):
        """
        - remove(значение) -- удаление элемента из множества;
        """
        # возвращает True если value удалено
        # иначе False
        if value in self.values:
            self.values.remove(value)
            self.length -= 1
            return True
        return False

    def intersection(self, set2):
        """
        - intersection(), в качестве параметра выступает другое множество,
        а возвращается пересечение этих множеств (множество,
        в котором есть только те элементы, которые имеются в каждом из множеств);
        """
        # пересечение текущего множества и set2
        set_intersection = PowerSet()
        [set_intersection.put(i) for i in self.values if i in set2.values]
        return set_intersection

    def union(self, set2):
        """
        - union(), в качестве параметра выступает другое множество,
        а возвращается объединение этих множеств
        (множество, в котором есть все элементы из каждого множества);
        """
        # объединение текущего множества и set2
        set_union = PowerSet()
        [set_union.put(i) for i in self.values]
        [set_union.put(i) for i in set2.values]
        return set_union

    def difference(self, set2):
        """
        - difference(), в качестве параметра выступает другое множество,
        а возвращается подмножество текущего множества из таких элементов,
        которые не входят в множество-параметр;
        """
        # разница текущего множества и set2
        set_difference = PowerSet()
        [set_difference.put(i) for i in self.values if i not in set2.values]
        return set_difference

    def issubset(self, set2):
        """
        - issubset(), в качестве параметра выступает другое множество,
        и проверяется, входят ли все его элементы в текущее множество
        (будет ли множество-параметр подмножеством текущего множества).
        """
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return all(i in self.values for i in set2.values)
