from operator import itemgetter

class StudentGroup:
    """Студенческая группа"""
    def __init__(self, id, name, students_count, kafedra_id):
        self.id = id
        self.name = name
        self.students_count = students_count
        self.kafedra_id = kafedra_id

class Kafedra:
    """Кафедра"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class GroupKafedra:
    """Студенческие группы кафедры для реализации связи многие-ко-многим"""
    def __init__(self, kafedra_id, group_id):
        self.kafedra_id = kafedra_id
        self.group_id = group_id

def main():
    # Кафедры
    kafedras = [
        Kafedra(1, 'ИУ5 (Системы обработки информации и управления)'),
        Kafedra(2, 'ИУ6 (Компьютерные системы и сети)'),
        Kafedra(3, 'РК6 (САПР)')
    ]
    
    # Студенческие группы 
    groups = [
        StudentGroup(1, 'Бакалавров', 25, 1),
        StudentGroup(2, 'Магистров', 15, 1),
        StudentGroup(3, 'Специалистов', 20, 2),
        StudentGroup(4, 'Аспирантов', 5, 2),
        StudentGroup(5, 'ИУ5-11Б', 30, 3)
    ]
    
    # Связи многие-ко-многим
    groups_kafedras = [
        GroupKafedra(1, 1),
        GroupKafedra(1, 2),
        GroupKafedra(2, 3),
        GroupKafedra(2, 4),
        GroupKafedra(3, 5),
        GroupKafedra(3, 1),
        GroupKafedra(1, 5)
    ]

    # Соединение данных один-ко-многим
    one_to_many = [(g.name, g.students_count, k.name)
                   for k in kafedras
                   for g in groups
                   if g.kafedra_id == k.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(k.name, gk.kafedra_id, gk.group_id)
                         for k in kafedras
                         for gk in groups_kafedras
                         if k.id == gk.kafedra_id]
                         
    many_to_many = [(g.name, g.students_count, kafedra_name)
                    for kafedra_name, kafedra_id, group_id in many_to_many_temp
                    for g in groups if g.id == group_id]

    print('Задание Б1')
    # Сортировка по студенческим группам
    res_1 = sorted(one_to_many, key=itemgetter(0))
    for r in res_1:
        print(r)

    print('\nЗадание Б2')
    res_2_unsorted = []
    # Перебираем все кафедры
    for k in kafedras:
        # Список групп кафедры
        k_groups = list(filter(lambda i: i[2] == k.name, one_to_many))
        if len(k_groups) > 0:
            res_2_unsorted.append((k.name, len(k_groups)))
            
    # Сортировка по количеству групп (по убыванию)
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    for r in res_2:
        print(r)

    print('\nЗадание Б3')
    res_3 = {}
    # Перебираем все группы
    for g in groups:
        # Условие: название заканчивается на "ов"
        if g.name.endswith('ов'):
            g_kafedras = list(filter(lambda i: i[0] == g.name, many_to_many))
            g_kafedras_names = [x[2] for x in g_kafedras]
            res_3[g.name] = g_kafedras_names
            
    print(res_3)

if __name__ == '__main__':
    main()
