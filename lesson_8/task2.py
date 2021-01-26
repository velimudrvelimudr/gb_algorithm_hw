""" 2) Закодируйте любую строку по алгоритму Хаффмана. """
from collections import Counter, deque, namedtuple

s = r'Я помню чудное мгновенье, передо мной явилась ты, как мимолётное виденье, как гений чистой красоты.'.lower()

# Преобразуем строку сначала в словарь Counter, Потом в очередь с кортежами вида (Буква, число вхождений).
cnt = Counter(s)
sd = deque(sorted(list(cnt.items()), key=lambda x: x[1]))

Node = namedtuple('Node', 'value left right') # Делаем ноду.

def cr_tree_bag(d: deque) -> Node:
    """ Формирует бинарное дерево из отсортированной очереди """

    if not isinstance(d[0], Node):
        new_node = Node(d[0][1] + d[1][1], d[0][0], d[1][0])
        d.popleft()
        d.popleft()
        d.appendleft(new_node)
    else:
        new_node = Node(d[0].value + d[1][1], d[0], d[1][0])
        d.popleft()
        d.popleft()
        d.appendleft(new_node)

    if len(d) == 1:
        return new_node
    else:
        cr_tree(d)


""" В общем, у меня так и осталось загадкой, почему функция возвращает NoneType. Правда она обрабатывает саму переданную ей очередь, поэтому результат всё же удаётся изучить. Увы, но рекурсия для меня, это сложно... """

def cr_tree(d: deque) -> None:
    """ Пробуем циклы. """

    while len(d) >= 2:
        left_value = d.popleft()
        right_value = d.popleft()

        if not isinstance(left_value, Node) and not isinstance(right_value, Node):
            new_node = Node(left_value[1] + right_value[1], left_value[0], right_value[0])
        elif isinstance(left_value, Node) and not isinstance(right_value, Node):
            new_node = Node(left_value.value + right_value[1], left_value, right_value[0])
        elif not isinstance(left_value, Node) and isinstance(right_value, Node):
            new_node = Node(left_value[1] + right_value.value, left_value[0], right_value)
        elif isinstance(left_value, Node) and isinstance(right_value, Node):
            new_node = Node(left_value.value + right_value.value, left_value, right_value)

        for i in range(len(d)):
            # Помещаем новообразованный узел обратно в очередь, но не в начало, а перед элементом с равным или большим приоритетом.
            if isinstance(d[i], Node) and new_node.value <= d[i].value:
                d.insert(i, new_node)
                break
            elif not isinstance(d[i], Node) and new_node.value <= d[i][1]:
                d.insert(i, new_node)
                break
        else:
            d.append(new_node)

    return new_node


def create_table_code(root: Node, direction: str=''):

    s = str()
    d = direction

    if isinstance(root, str):
        s += d + root + '|'
        # print(f'{d}, {root}')
    else:
        # print(f'{d}, {root.value}')
        s += d + create_table_code(root.left, '1')
        # print(f'{d}, {root.value}')
        s += d + create_table_code(root.right, '0')

    return s

""" Возвращает строку вида набор_битовБукваРазделитель,но набор битов не соответствует пути от корня к листам. Хотя первый и третий кластер таки угадали... """

if __name__ == '__main__':
    tr = cr_tree(sd)
    print(create_table_code(tr))
