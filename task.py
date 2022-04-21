
# структура для бинарного дерева с добавлением
# процедуры сбоки кода буквы в процессе обхода

class bi_leaf:

    def __init__(self, stem=None, left_kid=None, right_kid=None, value=None, freq=0):
        self.stem = stem
        self.left_kid=left_kid
        self.right_kid=right_kid
        self.value=value
        self.freq=freq 

    def get_codes(self, code, sym, codes_dict):
        code += sym
        if self.value:
            codes_dict[self.value] = code
        else:
            self.right_kid.get_codes(code,'1', codes_dict)
            self.left_kid.get_codes(code,'0', codes_dict)


# частоты букв в слове
# возвращаются сортированным списком

def frequencies(message):
    result = {}
    for letter in message:
        if letter not in result.keys():
            result[letter] = 1
        else:
            result[letter] += 1
    return (sorted(result.items(), key=lambda item: item[1]))


# основная структура - список исходных узлов.
# список частот - дополнительная,
# введена из тех сооображений, что искать место вставки
# проще по списку частот стандартной функцией, чем по списку объектов
# писать что-то своё для поиска

def Huffman_tree(frequencies):
    
    # собираем структуры данных
    freq_list = []
    nodes_list = []
    for element in frequencies:
        nodes_list.append(bi_leaf(None, None, None, element[0], element[1]))
        freq_list.append(element[1])
    
    # собираем бинарное дерево:
    # вычисляем сумму частот двух первых узлов,
    # ищем место вставки (и обрабатываем вылеты)
    # вставляем узлы
    # убираем исходные
    while len(nodes_list) > 1:
        sum_freq = nodes_list[0].freq + nodes_list[1].freq
        if sum_freq > max(freq_list):
            insert_index = len(nodes_list)-1
            nodes_list.append(bi_leaf(nodes_list[insert_index], nodes_list[0], nodes_list[1], None, sum_freq))
            freq_list.append(sum_freq)    
        elif sum_freq in freq_list:
            insert_index = freq_list.index(sum_freq)
            nodes_list.insert(insert_index, bi_leaf(nodes_list[insert_index], nodes_list[0], nodes_list[1], None, sum_freq))
            freq_list.insert(insert_index, sum_freq)
        else:
            insert_index = sum_freq
            while insert_index not in freq_list:
                insert_index -= 1
            nodes_list.insert(insert_index, bi_leaf(nodes_list[insert_index], nodes_list[0], nodes_list[1], None, sum_freq))
            freq_list.insert(insert_index, sum_freq)
        nodes_list.pop(0)
        nodes_list.pop(0)
        freq_list.pop(0)
        freq_list.pop(0)

    # когда дерево готово, обходим его рекурсивно и собираем коды
    codes_dict = {}
    nodes_list[0].get_codes('', '', codes_dict)
    return(codes_dict)

def cypher(message, codes):
    result = ''
    for letter in message:
        result = result + codes[letter]
    return result

def decypher(digest, codes):
    result = ''
    while not digest == '':
        for key, value in codes.items():
            if digest.startswith(value):
                result+= key
                digest = digest.replace(value, '', 1)
    return result


message = "Pepperoni Pizza"
dict_of_codes = Huffman_tree(frequencies(message))
digest = (cypher(message, dict_of_codes))
print(message, end='   кодируется в   ')
print(digest)
print('Словарь кодов: ', dict_of_codes)
print('Декодируем: ', decypher(digest, dict_of_codes))