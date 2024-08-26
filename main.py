import sqlite3
import re

#  -- SINIFLAR --


# taşların koordinatlarını tutmak için
class Coordinate:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x


# taş yeme hamlelerinde en çok taş yeme hamlelerini belirlemek için
class Attack:
    def __init__(self, matrix, kill_count: int):
        self.kill_count = kill_count
        self.matrix = matrix


# oynanabilir taşları ve onların koordinatlarını bulmak gerekiyor
# durumu gönder, oynanabilir taşların koordinatlarını al
class StonesCanMove:
    def __init__(self, matrix):
        self.commander_forced_moves = []
        self.soldier_forced_moves = []
        self.commander_moves = []
        self.soldier_moves = []
        self.matrix = matrix
        self.__get_moves__()

    def __get_moves__(self):    # kendi taşlarının konumlarını alır
        #  kendi taşlarını bul
        soldiers = []
        commanders = []
        for y in range(8):
            for x in range(8):
                if self.matrix[y][x] == 'm':
                    soldiers.append(Coordinate(y, x))
                if self.matrix[y][x] == 'M':
                    commanders.append(Coordinate(y, x))
        # normal taş için zorunlu yeme hamlelerini kontrol et
        for soldier in soldiers:
            # sola doğru yeme zorunluluğu
            if soldier.x > 1 and (self.matrix[soldier.y][soldier.x-1] == 'w' or self.matrix[soldier.y][soldier.x-1] == 'W'):
                # arkası da boş olması lazım
                if self.matrix[soldier.y][soldier.x-2] == '0':
                    # print(f'solunda yem var: {soldier.y}:{soldier.x}')
                    self.soldier_forced_moves.append(soldier)
                    continue
            # sağa doğru yeme zorunluluğu, en az 1 yeme zorunlulugu kafi...
            if soldier.x < 6 and (self.matrix[soldier.y][soldier.x+1] == 'w' or self.matrix[soldier.y][soldier.x+1] == 'W'):
                # arkası da boş olması lazım
                if self.matrix[soldier.y][soldier.x+2] == '0':
                    # print(f'sağında yem var: {soldier.y}:{soldier.x}')
                    self.soldier_forced_moves.append(soldier)
                    continue
            # yukarı doğru yeme zorunluluğu en az 1 yeme zorunlulugu kafi...
            if soldier.y > 1 and (self.matrix[soldier.y-1][soldier.x] == 'w' or self.matrix[soldier.y-1][soldier.x] == 'W'):
                # arkası da boş olması lazım
                if self.matrix[soldier.y-2][soldier.x] == '0':
                    # print(f'yukarısında yem var: {soldier.y}:{soldier.x}')
                    self.soldier_forced_moves.append(soldier)
        for commander in commanders:
            # sola doğru yeme zorunluluğu
            if commander.x > 1:
                for i in range(commander.x-1, 0, -1):
                    if self.matrix[commander.y][i] == 'm' or self.matrix[commander.y][i] == 'M':
                        break
                    if self.matrix[commander.y][i] == 'w' or self.matrix[commander.y][i] == 'W':
                        if self.matrix[commander.y][i-1] == '0':
                            # print(f'solunda yem var: {commander.y}:{commander.x}')
                            self.commander_forced_moves.append(commander)
                        else:
                            break
            # sağa doğru yeme zorunluluğu
            if commander.x < 6:
                for i in range(commander.x+1, 7, 1):
                    if self.matrix[commander.y][i] == 'm' or self.matrix[commander.y][i] == 'M':
                        break
                    if self.matrix[commander.y][i] == 'w' or self.matrix[commander.y][i] == 'W':
                        if self.matrix[commander.y][i+1] == '0':
                            # print(f'sağında yem var: {commander.y}:{commander.x}')
                            self.commander_forced_moves.append(commander)
                        else:
                            break
            # yukarı doğru yeme zorunluluğu
            if commander.y > 1:
                for i in range(commander.y-1, 0, -1):
                    if self.matrix[i][commander.x] == 'm' or self.matrix[i][commander.x] == 'M':
                        break
                    if self.matrix[i][commander.x] == 'w' or self.matrix[i][commander.x] == 'W':
                        if self.matrix[i-1][commander.x] == '0':
                            # print(f'yukarısında yem var: {commander.y}:{commander.x}')
                            self.commander_forced_moves.append(commander)
                        else:
                            break
            # aşağı doğru yeme zorunluluğu
            if commander.y < 6:
                for i in range(commander.y+1, 7, 1):
                    if self.matrix[i][commander.x] == 'm' or self.matrix[i][commander.x] == 'M':
                        break
                    if self.matrix[i][commander.x] == 'w' or self.matrix[i][commander.x] == 'W':
                        if self.matrix[i+1][commander.x] == '0':
                            # print(f'aşağısında yem var: {commander.y}:{commander.x}')
                            self.commander_forced_moves.append(commander)
                        else:
                            break
        # aynı elemanları çıkartalım
        self.commander_forced_moves = list(set(self.commander_forced_moves))
        # eğer oynama zorunlulu olan hamleler varsa diğer hamleleri hesaplamaya gerek yok
        if len(self.soldier_forced_moves) > 0 or len(self.commander_forced_moves) > 0:
            return
        # eğer buraya kadar geldiysek hiç taş yenebilecek bir durum yoktur
        # dama olmayan ve hareket edebilecek taşlar...
        for soldier in soldiers:
            # sola gidebiliyor ise
            if soldier.x > 0 and self.matrix[soldier.y][soldier.x-1] == '0':
                self.soldier_moves.append(soldier)
            # sağa gidebiliyor ise
            elif soldier.x < 7 and self.matrix[soldier.y][soldier.x+1] == '0':
                self.soldier_moves.append(soldier)
            # yukarı gidebiliyor ise
            elif soldier.y > 0 and self.matrix[soldier.y-1][soldier.x] == '0':
                self.soldier_moves.append(soldier)
        # hareket edebilen damalar için de soldier + aşağı gitme durumu
        for commander in commanders:
            # sola gidebiliyor ise
            if commander.x > 0 and self.matrix[commander.y][commander.x-1] == '0':
                self.commander_moves.append(commander)
            # sağa gidebiliyor ise
            elif commander.x < 7 and self.matrix[commander.y][commander.x+1] == '0':
                self.commander_moves.append(commander)
            # yukarı gidebiliyor ise
            elif commander.y > 0 and self.matrix[commander.y-1][commander.x] == '0':
                self.commander_moves.append(commander)
            # aşağı gidebiliyor ise
            elif commander.y < 7 and self.matrix[commander.y+1][commander.x] == '0':
                self.commander_moves.append(commander)


# Ağaç yapısı için... direkt veri tabanı nesnesi
class NodeEntity:
    def __init__(self, id: int, state: int, depth: int, father_node_id :int, height: int, result: int):
        self.id = id
        self.state = state
        self.depth = depth
        self.father_node_id = father_node_id
        self.height = height
        self.result = result


# ram de çalışmalar için daha uygun
class Node:
    def __init__(self, state: str, state_value: int, depth: int, father_node, height: int, result: int):
        self.state = state
        self.state_value = state_value
        self.depth = depth
        self.father_node: Node
        self.father_node = father_node
        self.height = height
        self.result = result


# Node ile ilgili veri tabanı ve servis işlemleri vs.
class NodeDao:
    def __init__(self, database_connection):
        self.database_connection = database_connection
        self.cursor = database_connection.cursor()
        # veri tabanında node tablosu yoksa oluştur
        self.__create_node_table()

    def __create_node_table(self):
        first_state = '00000000wwwwwwwwwwwwwwww0000000000000000mmmmmmmmmmmmmmmm00000000'
        # first_state = '00000000m000000000000000m00ww00000000000m00mm000000000m00M000000'
        # first_state = '00000000w00w0000m00m000000000000m0000000m00000000000000000000000'
        self.cursor.execute('CREATE TABLE IF NOT EXISTS node ('
                            'id INTEGER PRIMARY KEY NOT NULL, '
                            'state CHAR(64) UNIQUE NOT NULL, '
                            'depth INTEGER NOT NULL, '
                            'father_node_id INTEGER NOT NULL, '
                            'height INTEGER NULL, '
                            'result BLOB NULL, '
                            'FOREIGN KEY(father_node_id) REFERENCES node(id))')
        try:
            self.cursor.execute('INSERT INTO node (state, depth, father_node_id) VALUES '
                            '(?, ?, ?)', (first_state, 0, 1))
        except sqlite3.IntegrityError:
            # eklemiyorsa zaten kayıtlıdır...
            pass

    def get_id_by_state(self, state: str):
        self.cursor.execute('SELECT id FROM node WHERE state = ?', (state,))
        res = self.cursor.fetchone()
        if res:
            return res[0]
        else:
            return None

    def add(self, node: Node):
        father_node_id = self.get_id_by_state(node.father_node.state)
        try:
            self.cursor.execute('INSERT INTO node '
                                '(state, depth, father_node_id, height, result) VALUES '
                                '(?, ?, ?, ?, ?)',
                                (node.state, node.depth, father_node_id, node.height, node.result))
            # self.database_connection.commit()
        except sqlite3.IntegrityError:
            # buraya ekleme yapılacak...
            pass

    def get_by_id(self, id: int):
        self.cursor.execute('SELECT * FROM node WHERE id = ?', (id,))
        res = self.cursor.fetchone()
        if res:
            node_entity = NodeEntity(*res)
            father_node = None
            self.cursor.execute('SELECT * FROM node WHERE id = ?', (node_entity.father_node_id,))
            res = self.cursor.fetchone()
            if res:
                father_dto = NodeEntity(*res)
                father_node = Node(father_dto.state, None, father_dto.depth, None, father_dto.height, father_dto.result)
            return Node(node_entity.state, None, node_entity.depth, father_node, node_entity.height, node_entity.result)
        else:
            return None

    def get_father_by_state(self, state: str):
        self.cursor.execute('SELECT * FROM node WHERE state = ?', (state,))
        res = self.cursor.fetchone()
        if res:
            node_entity = NodeEntity(*res)

            # def __init__(self, id: int, state: int, depth: int, father_node_id: int, height: int, result: int):
            self.cursor.execute('SELECT * FROM node WHERE id = ?', (node_entity.father_node_id,))
            res = self.cursor.fetchone()
            if res:
                father_entity = NodeEntity(*res)
                if father_entity.state == node_entity.state:
                    return None
                return Node(father_entity.state, None, father_entity.depth, None, father_entity.height, father_entity.result)
            else:
                return None
        else:
            return None

    def get_by_state(self, state: str):
        self.cursor.execute('SELECT * FROM node WHERE state = ?', (state,))
        res = self.cursor.fetchone()
        if res:
            node_entity = NodeEntity(*res)
            return Node(node_entity.state, None, node_entity.depth, None, node_entity.height, node_entity.result)
        else:
            return None

    def update(self, node: Node, id: int):
        self.cursor.execute("UPDATE node SET result=?, height=? WHERE id=?", (node.result, node.height, id))

    def remove_by_state(self, state: str):
        self.cursor.execute("DELETE FROM node WHERE state=?", (state,))

    def remove(self, id: int):
        # print(f'silinen satir id si = {id}')
        self.cursor.execute("DELETE FROM node WHERE id=?", (id,))
        # print(f"{self.cursor.rowcount} satır silindi.")
        # self.print_all()

    def print_all(self):
        self.cursor.execute('SELECT * FROM node')
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"[id: {row[0]}][state: {row[1]}][depth: {row[2]}][father_id: {row[3]}][height: {row[4]}][result: {row[5]}]")

    # bir çocuk daha yukarı dallara çıkabilir, bu durumda da ona ulaşmak gerekir
    def get_children_of_father(self, father_node: Node, next_nodes):
        for next_node in next_nodes:
            if self.get_id_by_state(next_node.state) is None:
                next_nodes.remove(next_node)
        return next_nodes


    # def save_experience(self, node_tree):
    #     # node_tree nin bir kısmını, büyük ağacın bir uç kısmı oalrak düşün ve direkt kaydet
    #     for i in range(game_level+1):
    #         nodes = node_tree[i]
    #         for node in nodes:
    #             if node.result is not None:
    #                 self.add(node)
    #     # bir üst düğüm için sonucu kontrol et



        # # ilk olarak veri tabanında
        # father_id = self.get_id_by_state(node.father_node.state)
        # father = self.get_by_id(father_id)
        # if father.result is None:
        #     brothers = BranchMaker.create_next_nodes(father)
        #     # ancak bütün kardeşler veri tabanında yüklü ise, babanın sonucu hesaplanabilir
        #     if father.depth % 2 == 0:
        #         # maks
        #         result = 0
        #         # herhangi bir düğümün sonucu 2 ise direkt win e gider
        #         for bro in brothers:
        #             brother = self.get_by_state(bro.state)
        #             if brother is None or brother.result is None:
        #                 return
        #             elif father.result is None or father.result < brother.result:
        #                 father.result = brother.result
        #                 father.height = brother.height + 1
        #             elif father.result == brother.result and father.height > brother.height:
        #                 father.height = brother.height + 1
        #     else:
        #         # min
        #         result = 2
        #         for bro in brothers:
        #             brother = self.get_by_state(bro.state)
        #             if brother is None or brother.result is None:
        #                 return
        #             elif father.result is None or father.result > brother.result:
        #                 father.result = brother.result
        #                 father.height = brother.height + 1
        #             elif father.result == brother.result and father.height > brother.height:
        #                 father.height = brother.height + 1
        #     self.update(father, father_id)
        # self.save_experience(father)


# Bir düğüm alacak ve bu düğümden oluşabilecek düğümlerin listesi verecek
class BranchMaker:
    soldier_kill_count = 0
    commander_kill_count = 0
    matrix = None

    #
    @staticmethod
    def create_next_nodes(node: Node):
        BranchMaker.soldier_kill_count = 0
        BranchMaker.commander_kill_count = 0
        # ilk önce durumu(string) matrise çevir
        BranchMaker.matrix = BranchMaker.__string_to_matrix(node.state)
        # hamle yapabilen taşları çek...
        stones_can_move = StonesCanMove(BranchMaker.matrix)
        # zorunlu yapman gereken hamleler varsa onları yap yoksa normal hamle yap
        if stones_can_move.commander_forced_moves or stones_can_move.soldier_forced_moves:
            commander_attack_result = BranchMaker.__commander_attacks(BranchMaker.matrix, stones_can_move.commander_forced_moves)
            soldier_attack_result = BranchMaker.__soldier_attacks(BranchMaker.matrix, stones_can_move.soldier_forced_moves)
            # en çok taş yenecek hamleleri çek
            if BranchMaker.commander_kill_count > BranchMaker.soldier_kill_count:
                # print('commander')
                return BranchMaker.__create_node_list(commander_attack_result, node)
            elif BranchMaker.commander_kill_count < BranchMaker.soldier_kill_count:
                # print('soldier')
                return BranchMaker.__create_node_list(soldier_attack_result, node)
            else:
                # print('commander + soldier')
                return BranchMaker.__create_node_list(commander_attack_result + soldier_attack_result, node)
        else:
            # yapılabilecek hamleleri bul
            soldier_moves_result = BranchMaker.__soldier_moves(BranchMaker.matrix, stones_can_move.soldier_moves)
            commander_moves_result = BranchMaker.__commander_moves(BranchMaker.matrix, stones_can_move.commander_moves)
            return BranchMaker.__create_node_list(soldier_moves_result + commander_moves_result, node)

    # durum listesi oluşturur, win/lose/draw durumlarını da hesaplar.
    def __create_node_list(matrix_list, father_node):
        node_list = []
        global move_count
        global state_dict
        for matrix in matrix_list:
            state = ''
            m_count = 0
            w_count = 0
            for y in range(7, -1, -1):
                for x in range(7, -1, -1):
                    state = state + state_dict[matrix[y][x]]
                    if matrix[y][x] == 'm' or matrix[y][x] == 'M':
                        m_count = m_count + 1
                    elif matrix[y][x] != '0':
                        w_count = w_count + 1
            if w_count == 0:
                if father_node.depth % 2 == 0:
                    # M win e ulaştı...
                    new_node = Node(state, 10000, father_node.depth + 1, father_node, 0, 2)
                    node_list.append(new_node)
                else:
                    # W win e ulaştı
                    node_list.append(Node(state, -10000, father_node.depth + 1, father_node, 0, 0))
            elif w_count == 1 and m_count == 1:
                # beraberlik
                node_list.append(Node(state, 0, father_node.depth + 1, father_node, 0, 1))
            else:
                node_list.append(Node(state, None, father_node.depth + 1, father_node, None, None))
        return node_list

    def __string_to_matrix(string=''):
        # print(str)
        char_array = list(string)
        matrix = [['' for _ in range(8)] for _ in range(8)]
        for y in range(8):
            for x in range(8):
                matrix[y][x] = char_array[y * 8 + x]
        return matrix

    def __soldier_move(matrix, old_coordinate, new_coordinate):
        new_matrix = BranchMaker.__create_new_matrix(matrix)
        # dama olma durumu
        if new_coordinate.y == 0:
            new_matrix[new_coordinate.y][new_coordinate.x] = 'M'
        else:
            new_matrix[new_coordinate.y][new_coordinate.x] = 'm'
        new_matrix[old_coordinate.y][old_coordinate.x] = '0'
        return new_matrix

    # hareket edebilen, dama olmayan taşların listesini alıp, yeni durumların listesini döndürür
    def __soldier_moves(matrix, stones):
        matrix_list = []
        for stone in stones:
            # sola hamle yap
            if stone.x > 0 and matrix[stone.y][stone.x - 1] == '0':
                matrix_list.append(BranchMaker.__soldier_move(matrix, stone, Coordinate(stone.y, stone.x - 1)))
            # yukarı hamle yap
            if stone.y > 0 and matrix[stone.y - 1][stone.x] == '0':
                matrix_list.append(BranchMaker.__soldier_move(matrix, stone, Coordinate(stone.y - 1, stone.x)))
            # sağa hamle yap
            if stone.x < 7 and matrix[stone.y][stone.x + 1] == '0':
                matrix_list.append(BranchMaker.__soldier_move(matrix, stone, Coordinate(stone.y, stone.x + 1)))
        return matrix_list

    def __commander_move(matrix, old_coordinate, new_coordinate):
        new_matrix = BranchMaker.__create_new_matrix(matrix)
        new_matrix[new_coordinate.y][new_coordinate.x] = 'M'
        new_matrix[old_coordinate.y][old_coordinate.x] = '0'
        return new_matrix

    # hareket edebilen dama taşların listesini alıp, yeni durumların listesini döndürür
    def __commander_moves(matrix, stones):
        matrix_list = []
        for stone in stones:
            # sola hamle yap
            if stone.x > 0:
                for i in range(stone.x - 1, -1, -1):
                    if matrix[stone.y][i] == '0':
                        matrix_list.append(BranchMaker.__commander_move(matrix, stone, Coordinate(stone.y, i)))
                    else:
                        break
            # yukarı hamle yap
            if stone.y > 0:
                for i in range(stone.y - 1, -1, -1):
                    if matrix[i][stone.x] == '0':
                        matrix_list.append(BranchMaker.__commander_move(matrix, stone, Coordinate(i, stone.x)))
                    else:
                        break
            # sağa hamle yap
            if stone.x < 7:
                for i in range(stone.x + 1, 8, 1):
                    if matrix[stone.y][i] == '0':
                        matrix_list.append(BranchMaker.__commander_move(matrix, stone, Coordinate(stone.y, i)))
                    else:
                        break
            # aşağı hamle yap
            if stone.y < 7:
                for i in range(stone.y + 1, 8, 1):
                    if matrix[i][stone.x] == '0':
                        matrix_list.append(BranchMaker.__commander_move(matrix, stone, Coordinate(i, stone.x)))
                    else:
                        break
        return matrix_list

    def __soldier_attack(matrix, stone, attack_list, kill_count):
        # sola saldırı
        if stone.x > 1 and (matrix[stone.y][stone.x - 1] == 'w' or matrix[stone.y][stone.x - 1] == 'W'):
            if matrix[stone.y][stone.x - 2] == '0':
                new_matrix = BranchMaker.__create_new_matrix(matrix)
                new_matrix[stone.y][stone.x - 2] = new_matrix[stone.y][stone.x]
                new_matrix[stone.y][stone.x - 1] = '0'
                new_matrix[stone.y][stone.x] = '0'
                attack_list.append(Attack(new_matrix, kill_count))
                BranchMaker.__soldier_attack(new_matrix, Coordinate(stone.y, stone.x - 2), attack_list, kill_count + 1)
        # sağa saldırı
        if stone.x < 6 and (matrix[stone.y][stone.x + 1] == 'w' or matrix[stone.y][stone.x + 1] == 'W'):
            if matrix[stone.y][stone.x + 2] == '0':
                new_matrix = BranchMaker.__create_new_matrix(matrix)
                new_matrix[stone.y][stone.x + 2] = new_matrix[stone.y][stone.x]
                new_matrix[stone.y][stone.x + 1] = '0'
                new_matrix[stone.y][stone.x] = '0'
                attack_list.append(Attack(new_matrix, kill_count))
                BranchMaker.__soldier_attack(new_matrix, Coordinate(stone.y, stone.x + 2), attack_list, kill_count + 1)
        # yukarı saldırı
        if stone.y > 1 and (matrix[stone.y - 1][stone.x] == 'w' or matrix[stone.y - 1][stone.x] == 'W'):
            if matrix[stone.y - 2][stone.x] == '0':
                new_matrix = BranchMaker.__create_new_matrix(matrix)
                new_matrix[stone.y][stone.x] = '0'
                new_matrix[stone.y - 1][stone.x] = '0'
                if stone.y == 2:
                    new_matrix[0][stone.x] = 'M'
                else:
                    new_matrix[stone.y - 2][stone.x] = 'm'
                attack_list.append(Attack(new_matrix, kill_count))
                BranchMaker.__soldier_attack(new_matrix, Coordinate(stone.y - 2, stone.x), attack_list, kill_count + 1)
        return attack_list

    def __soldier_attacks(matrix, stones):
        matrix_list = []
        max_kill_count = 0
        all_moves = []
        for soldier in stones:
            attack_list = BranchMaker.__soldier_attack(matrix, soldier, [], 1)
            all_moves.append(attack_list)
            for attack in attack_list:
                if attack.kill_count > max_kill_count:
                    max_kill_count = attack.kill_count
        for attack_list in all_moves:
            for attack in attack_list:
                if attack.kill_count == max_kill_count:
                    matrix_list.append(attack.matrix)
        BranchMaker.soldier_kill_count = max_kill_count
        return matrix_list

    def __commander_attack(matrix, stone, attack_list, kill_count):
        # sola saldırılar
        if stone.x > 1:
            for i in range(stone.x - 1, 0, -1):
                if matrix[stone.y][i] == 'w' or matrix[stone.y][i] == 'W':
                    if matrix[stone.y][i - 1] == '0':
                        new_matrix = BranchMaker.__create_new_matrix(matrix)
                        new_matrix[stone.y][stone.x] = '0'
                        new_matrix[stone.y][i] = '0'
                        new_matrix[stone.y][i - 1] = 'M'
                        attack_list.append(Attack(new_matrix, kill_count))
                        BranchMaker.__commander_attack(new_matrix, Coordinate(stone.y, i - 1), attack_list, kill_count + 1)
                        for j in range(i - 2, -1, -1):
                            if matrix[stone.y][j] == '0':
                                new_matrix = BranchMaker.__create_new_matrix(matrix)
                                new_matrix[stone.y][stone.x] = '0'
                                new_matrix[stone.y][i] = '0'
                                new_matrix[stone.y][j] = 'M'
                                attack_list.append(Attack(new_matrix, kill_count))
                                BranchMaker.__commander_attack(new_matrix, Coordinate(stone.y, j), attack_list, kill_count + 1)
                            else:
                                break
                        break
                    else:
                        break
                elif matrix[stone.y][i] != '0':
                    break

        # sağa saldırılar
        if stone.x < 6:
            for i in range(stone.x + 1, 7, 1):
                if matrix[stone.y][i] == 'w' or matrix[stone.y][i] == 'W':
                    if matrix[stone.y][i + 1] == '0':
                        new_matrix = BranchMaker.__create_new_matrix(matrix)
                        new_matrix[stone.y][stone.x] = '0'
                        new_matrix[stone.y][i] = '0'
                        new_matrix[stone.y][i + 1] = 'M'
                        attack_list.append(Attack(new_matrix, kill_count))
                        BranchMaker.__commander_attack(new_matrix, Coordinate(stone.y, i + 1), attack_list, kill_count + 1)
                        for j in range(i + 2, 8, 1):
                            if matrix[stone.y][j] == '0':
                                new_matrix = BranchMaker.__create_new_matrix(matrix)
                                new_matrix[stone.y][stone.x] = '0'
                                new_matrix[stone.y][i] = '0'
                                new_matrix[stone.y][j] = 'M'
                                attack_list.append(Attack(new_matrix, kill_count))
                                BranchMaker.__commander_attack(new_matrix, Coordinate(stone.y, j), attack_list, kill_count + 1)
                            else:
                                break
                        break
                    else:
                        break
                elif matrix[stone.y][i] != '0':
                    break

        # yukarı saldırılar
        if stone.y > 1:
            for i in range(stone.y - 1, 0, -1):
                if matrix[i][stone.x] == 'w' or matrix[i][stone.x] == 'W':
                    if matrix[i - 1][stone.x] == '0':
                        new_matrix = BranchMaker.__create_new_matrix(matrix)
                        new_matrix[stone.y][stone.x] = '0'
                        new_matrix[i][stone.x] = '0'
                        new_matrix[i - 1][stone.x] = 'M'
                        attack_list.append(Attack(new_matrix, kill_count))
                        BranchMaker.__commander_attack(new_matrix, Coordinate(i - 1, stone.x), attack_list, kill_count + 1)
                        for j in range(i - 2, -1, -1):
                            if matrix[j][stone.x] == '0':
                                new_matrix = BranchMaker.__create_new_matrix(matrix)
                                new_matrix[stone.y][stone.x] = '0'
                                new_matrix[i][stone.x] = '0'
                                new_matrix[j][stone.x] = 'M'
                                attack_list.append(Attack(new_matrix, kill_count))
                                BranchMaker.__commander_attack(new_matrix, Coordinate(j, stone.x), attack_list, kill_count + 1)
                            else:
                                break
                        break
                    else:
                        break
                elif matrix[i][stone.x] != '0':
                    break

        # aşağı saldırılar
        if stone.y < 6:
            for i in range(stone.y + 1, 7, 1):
                if matrix[i][stone.x] == 'w' or matrix[i][stone.x] == 'W':
                    if matrix[i + 1][stone.x] == '0':
                        new_matrix = BranchMaker.__create_new_matrix(matrix)
                        new_matrix[stone.y][stone.x] = '0'
                        new_matrix[i][stone.x] = '0'
                        new_matrix[i + 1][stone.x] = 'M'
                        attack_list.append(Attack(new_matrix, kill_count))
                        BranchMaker.__commander_attack(new_matrix, Coordinate(i + 1, stone.x), attack_list, kill_count + 1)
                        for j in range(i + 2, 8, 1):
                            if matrix[j][stone.x] == '0':
                                new_matrix = BranchMaker.__create_new_matrix(matrix)
                                new_matrix[stone.y][stone.x] = '0'
                                new_matrix[i][stone.x] = '0'
                                new_matrix[j][stone.x] = 'M'
                                attack_list.append(Attack(new_matrix, kill_count))
                                BranchMaker.__commander_attack(new_matrix, Coordinate(j, stone.x), attack_list, kill_count + 1)
                            else:
                                break
                        break
                    else:
                        break
                elif matrix[i][stone.x] != '0':
                    break

        return attack_list

    def __commander_attacks(matrix, stones):
        matrix_list = []
        max_kill_count = 0
        all_moves = []
        for commander in stones:
            attack_list = BranchMaker.__commander_attack(matrix, commander, [], 1)
            all_moves.append(attack_list)
            for attack in attack_list:
                if attack.kill_count > max_kill_count:
                    max_kill_count = attack.kill_count
        for attack_list in all_moves:
            for attack in attack_list:
                if attack.kill_count == max_kill_count:
                    matrix_list.append(attack.matrix)

        # aynı matrixler oluşabilir, bunu exception handler ile düzelt
        BranchMaker.commander_kill_count = max_kill_count
        return matrix_list

    def __create_new_matrix(matrix):
        new_matrix = [['' for _ in range(8)] for _ in range(8)]
        for y in range(8):
            for x in range(8):
                new_matrix[y][x] = matrix[y][x]
        return new_matrix


#  -- FONKSİYONLAR --

def select_turn():
    while True:
        user_input = input("İlk başlamak için 1, ikinci başlamak için 2 giriniz: ")
        if user_input == "1":
            return 0
        elif user_input == "2":
            global play_in_opposite
            play_in_opposite = True
            return 1
        else:
            print("Lütfen 1 veya 2 giriniz.")


def select_level():
    while True:
        try:
            user_input = input("1 ile 5 arasında bir zorluk seviyesi griniz:")
            game_level = int(user_input)
            if game_level < 1 or game_level > 5:
                print("Girilen sayı 1 ile 5 arasında olmalıdır. 1 ve 5 dahildir.")
            else:
                return int(user_input)
        except ValueError:
            print("[-] Bir tam sayı girmelisiniz.")


def get_reverse_of_state(state: str):
    state_array = list(state)
    new_state = ""
    global state_dict
    for y in range(7, -1, -1):
        for x in range(7, -1, -1):
            new_state = new_state + state_dict[state_array[y * 8 + x]]
    return new_state


def print_table(state: str):
    if play_in_opposite:
        state_array = list(get_reverse_of_state(state))
        for y in range(8):
            print(f"{8-y} | ", end=" ")
            for x in range(8):
                print(state_array[y*8+x], end=" ")
            print()
    else:
        state_array = list(state)
        for y in range(8):
            print(f"{8-y} | ", end=" ")
            for x in range(8):
                print(state_array[y*8+x], end=" ")
            print()
    print("--|-----------------")
    print("  |  A B C D E F G H\n")


def show_player_can_move(current_node: Node, next_nodes: []):
    global play_in_opposite
    current_matrix = list(get_reverse_of_state(current_node.state))
    for next_node in next_nodes:
        message_forced_moves = ''
        cmd = ""
        next_matrix = list(next_node.state)
        x1 = ''
        x2 = ''
        y1 = ''
        y2 = ''
        for y in range(8):
            for x in range(8):
                if next_matrix[y*8+x] != current_matrix[y*8+x]:
                    if next_matrix[y*8+x] == '0':
                        # taş yenme durumu var...
                        if current_matrix[y*8+x] == 'm' or current_matrix[y*8+x] == 'M':
                            message_forced_moves = f"{message_forced_moves}({chr(72 - x)}{chr(49 + y)}) "
                        # kendi taşını oynatmalı
                        else:
                            y1 = chr(49 + y)
                            x1 = chr(72 - x)
                    # hedef koordinat
                    else:
                        y2 = chr(49 + y)
                        x2 = chr(72 - x)
        cmd = f"{x1}{y1} {x2}{y2}"
        if play_in_opposite:
            cmd = cmd_reverser(cmd)
        if message_forced_moves != "":
            if play_in_opposite:
                message_forced_moves = cmd_reverser(message_forced_moves)
            print(f"Yapılabilecek hamleler: ({cmd})")
            print(f"Yenilmesi gereken taşlar: {message_forced_moves}")


def cmd_reverser(cmd: str):
    chars = list(cmd)
    reversed_cmd = ''
    global cmd_reverser_dct
    for char in chars:
        reversed_cmd = reversed_cmd + cmd_reverser_dct[char]
    return reversed_cmd


# kullanıcının seçtiği hamle taş yeme hamlesimi? öyleyse hangisi...
def player_kills_computer(input: str, current_node: Node, next_nodes: []):
    current_matrix = list(get_reverse_of_state(current_node.state))
    for next_node in next_nodes:
        next_matrix = list(next_node.state)
        x1 = ''
        x2 = ''
        y1 = ''
        y2 = ''
        attack_string = ''
        for y in range(8):
            for x in range(8):
                if next_matrix[y*8+x] != current_matrix[y*8+x]:
                    if next_matrix[y*8+x] == '0':
                        # taş yenme durumu var...
                        if current_matrix[y*8+x] == 'w' or current_matrix[y*8+x] == 'W':
                            y1 = chr(49 + y)
                            x1 = chr(72 - x)
                    # hedef koordinat
                    else:
                        y2 = chr(49 + y)
                        x2 = chr(72 - x)
        attack_string = f"{x1}{y1} {x2}{y2}"
        if attack_string == input:
            return next_node
    return None


# kullanıcıya hamle yaptırır
def player_move(current_node: Node):
    while True:
        user_input = input("Bir hamle yapınız: ").upper()
        try:
            match = re.findall(r'[A-H][0-8]\s[A-H][0-8]', user_input)[0]
            if match == user_input:
                # emir tipi doğru, hame yapılabilir mi kontrol et
                if play_in_opposite:
                    user_input = cmd_reverser(user_input)
                user_input_array = list(user_input)
                state_array = list(current_node.state)
                # koordinatları çevir.
                y1 = 8 - int(user_input_array[1])
                y2 = 8 - int(user_input_array[4])
                x1 = ord(user_input_array[0]) - 65
                x2 = ord(user_input_array[3]) - 65
                if y1 == y2 and x1 == x2:
                    print("[!] Hedef koordinat ile kaynak koordinat aynı olamaz.")
                else:
                    if state_array[y1*8+x1] != 'm' and state_array[y1*8+x1] != 'M':
                        print("[!] Kaynak koordinatda kendi taşınız olmalıdır.")
                    else:
                        if state_array[y2*8+x2] != '0':
                            print("[!] Hedef koordinat boş olmalıdır.")
                        else:
                            state_array[y2 * 8 + x2] = state_array[y1*8+x1]
                            state_array[y1 * 8 + x1] = '0'
                            new_state = ''
                            global state_dict
                            for y in range(7, -1, -1):
                                for x in range(7, -1, -1):
                                    new_state = new_state + state_dict[state_array[y*8+x]]
                            nodes = BranchMaker.create_next_nodes(current_node)
                            for node in nodes:
                                if node.state == new_state:
                                    return node
                            # yeme durumlarını kontrol et.
                            kill_move = player_kills_computer(user_input, current_node, nodes)
                            if kill_move is None:
                                print("[!] Bu hamle yapılamaz.")
                                show_player_can_move(current_node, nodes)
                            else:
                                return kill_move
            else:
                print("[!] Lütfen uygun formatta hamle yapnız.")
                print("Uygun format örnekleri:\n'A2 A3' veya 'g2 h2' veya 'G1 f1' gibi...")
        except IndexError:
            print("[-] Hamleniz uygun formatta değildir.")
            print("Uygun format örnekleri:\n'A2 A3' veya 'g2 h2' veya 'G1 f1' gibi...")


# bir düğümün durum değerini hesaplar
def state_value_calculator(node: Node):
    if node.result != None:
        return
    matrix = list(node.state)
    state_value = 0
    corners = [0, 7, 56, 63]
    edges = [1, 2, 3, 4, 5, 6, 8, 16, 24, 32, 40, 48, 15, 23, 31, 39, 47, 55, 57, 58, 59, 60, 61, 62]
    # köşelerdeki dama taşlar
    for i in corners:
        if matrix[i] == 'M':
            state_value = state_value - 64
        elif matrix[i] == 'W':
            state_value = state_value + 64
    # kenarlardaki dama taşlar
    for i in edges:
        if matrix[i] == 'M':
            state_value = state_value - 48
        elif matrix[i] == 'W':
            state_value = state_value + 48
    # orta alandaki tüm taşlar
    for y in range(1, 7, 1):
        for x in range(1, 7, 1):
            if matrix[y*8+x] == 'M':
                state_value = state_value - 32
            if matrix[y*8+x] == 'W':
                state_value = state_value + 32
            if matrix[y*8+x] == 'm':
                state_value = state_value - 22 + (2 * y)
            if matrix[y*8+x] == 'w':
                state_value = state_value + (2 * y + 8)
    # sağ ve sol kenarlardaki 'm' ve 'w' lar
    for y in range(1, 7, 1):
        if matrix[y*8] == 'm':
            state_value = state_value - 33 + (3 * y)
        elif matrix[y*8] == 'w':
            state_value = state_value + (3 * y + 12)
        if matrix[y*8+7] == 'm':
            state_value = state_value - 33 + (3 * y)
        elif matrix[y*8+7] == 'w':
            state_value = state_value + (3 * y + 12)
    if node.depth % 2 == 0:
        node.state_value = state_value * -1
    else:
        node.state_value = state_value


# dipten yukarıya doğru durum değerlerini aktarır (min/max)
def calculate_tree(state_tree):
    global game_level
    global move_count
    deepest_nodes = state_tree[game_level]
    for deepest_node in deepest_nodes:
        state_value_calculator(deepest_node)
    for i in range(game_level, 0, -1):
        nodes = state_tree[i]
        # min
        if (move_count + i) % 2 == 0:
            for node in nodes:
                if node.father_node.state_value is None:
                    node.father_node.state_value = node.state_value
                    node.father_node.result = node.result
                    if node.height is not None:
                        node.father_node.height = node.height + 1
                elif node.state_value < node.father_node.state_value:
                    node.father_node.state_value = node.state_value
                    node.father_node.result = node.result
                    if node.height is not None:
                        node.father_node.height = node.height + 1
        # maks
        else:
            for node in nodes:
                if node.father_node.state_value is None:
                    node.father_node.state_value = node.state_value
                    node.father_node.result = node.result
                    if node.height is not None:
                        node.father_node.height = node.height + 1
                elif node.state_value > node.father_node.state_value:
                    node.father_node.state_value = node.state_value
                    node.father_node.result = node.result
                    if node.height is not None:
                        node.father_node.height = node.height + 1


# # bir çocuk daha yukarı dallara çıkabilir, bu durumda da ona ulaşmak gerekir
# def get_children_of_father(father_node: Node):
#     next_nodes = BranchMaker.create_next_nodes(father_node)
#     global node_dao
#     for next_node in next_nodes:
#         if node_dao.get_id_by_state(next_node.state) is None:
#             next_nodes.remove(next_node)
#     return next_nodes


# bilgisayarın yapabileceği en iyi hamleyi hesaplar
def computer_move_calculator(root_node):
    # ilk önce veri tabanındaki ağaçtan öğrenilmiş hamle varsa çek
    global node_dao
    id = node_dao.get_id_by_state(root_node.state)
    if id is not None:
        root_node = node_dao.get_by_id(id)
        if root_node.result is not None:
            global user_turn
            win = user_turn * 2
            # node_dao.print_all()
            next_nodes = BranchMaker.create_next_nodes(root_node)
            child_nodes = node_dao.get_children_of_father(root_node, next_nodes)
            # kazama durumu
            if root_node.result == win:
                print("Artık kazanamazsınız.")
            # beraberlik ise ?? ama oyuncu bilgisayar değil, kötü hamleler yapabilir...
            elif root_node.result == 1:
                print("güzel oynarsanız berabere bitebilir.")
            # kaybtme durumu -> rehberlik teklif etsin.
            else:
                print("güzel oynarsanız kazanabilirsiniz.")
            child_nodes = sorted(child_nodes, key=lambda x: x.height)
            for child_node in child_nodes:
                if child_node.result == root_node.result:
                    return child_node

    # öğrenilmiş bir hamle yok...
    global game_level
    state_tree = {0: [root_node]}
    for i in range(game_level):
        current_nodes = state_tree[i]
        next_nodes = []
        for current_node in current_nodes:
            if current_node.result is None:
                next_nodes = next_nodes + BranchMaker.create_next_nodes(current_node)
        state_tree[i + 1] = next_nodes
    # ağacı oluşturduk... en iyi hamleye ulaşmamız lazım
    calculate_tree(state_tree)
    next_nodes = state_tree[1]
    # oyun sona ulaşıyor mu kontrol et ve tecrubeleri kaydet
    if root_node.result is not None:
        save_experience(state_tree)
    global state_list
    # bilgisayar max ise küçükten büyüğe doğru sırala
    if root_node.depth % 2 == 0:
        next_nodes = sorted(next_nodes, key=lambda x: x.state_value, reverse=True)
    # bilgisayar min ise büyükten küçüğe doğru sırala
    else:
        next_nodes = sorted(next_nodes, key=lambda x: x.state_value)
    for next_node in next_nodes:
        # ilk en iyi hamleden başlayarak en iyi hamleyi yap
        if next_node.state not in state_list:
            return next_node
    # bu noktaya geldiysek tüm hamleler yapılmıştır o zaman en iyi hamleyi döndür
    return next_node[0]


def update_father_result(node):
    global node_dao
    father_node = node_dao.get_father_by_state(node.state)
    if father_node is None:
        res = node_dao.get_id_by_state(node.state)
        if node_dao.get_id_by_state(node.state) == 1:
            node_dao.update(node, 1)
        return
    if father_node.result is not None:
        update_father_result(father_node)
        return
    # win kaydetme
    if (node.result == 2 and father_node.depth % 2 == 0) or (node.result == 0 and father_node.depth % 2 == 1):
        father_node.result = node.result
        father_node.height = node.height + 1
        father_node_id = node_dao.get_id_by_state(father_node.state)
        node_dao.update(father_node, father_node_id)
        update_father_result(father_node)
        return
    brothers = BranchMaker.create_next_nodes(father_node)
    max_result = 0
    for brother in brothers:
        bro = node_dao.get_by_state(brother.state)
        if bro is not None:
            brother = bro
        if brother.result is None:
            return
    # draw kaydetme
    if node.result == 1:
        father_node.result = node.result
        father_node.height = node.height + 1
        father_node_id = node_dao.get_id_by_state(father_node.state)
        node_dao.update(father_node, father_node_id)
        update_father_result(father_node)
        return    # lose kaydetme
    if (node.result == 0 and father_node.depth % 2 == 0) or (node.result == 2 and father_node.depth % 2 == 1):
        father_node.result = node.result
        father_node.height = node.height + 1
        father_node_id = node_dao.get_id_by_state(father_node.state)
        node_dao.update(father_node, father_node_id)
        update_father_result(father_node)
        return


def save_experience(node_tree):
    # node_tree nin bir kısmını, büyük ağacın bir uç kısmı oalrak düşün ve direkt kaydet
    global node_dao
    for i in range(game_level+1):
        nodes = node_tree[i]
        for node in nodes:
            if node.result is not None:
                node_dao.add(node)
    # bir üst düğüm için sonucu kontrol et
    root_l = node_tree[0]
    root = root_l[0]
    update_father_result(root)


# bilgisayarın yaptığı hamlenin komutunu çeker
def get_computer_move_command(first_node: Node, next_node: Node):
    first_state = get_reverse_of_state(first_node.state)
    first_array = list(first_state)
    next_array = list(next_node.state)
    x1: int
    x2: int
    y1: int
    y2: int
    for y in range(8):
        for x in range(8):
            if first_array[y*8+x] != next_array[y*8+x]:
                # başlangıç noktası
                if first_array[y*8+x] == 'w' or first_array[y*8+x] == 'W':
                    y1 = y
                    x1 = x
                # bitiş noktası
                elif next_array[y*8+x] == 'w' or next_array[y*8+x] == 'W':
                    y2 = y
                    x2 = x
    cmd = f"{chr(x1+65)}{chr(56-y1)} {chr(x2+65)}{chr(56-y2)}"
    if play_in_opposite:
        return cmd_reverser(cmd)
    else:
        return cmd


# bilgisayara hamle yaptırıp, o hamlenin komutunu yazdırır
def computer_move(root_node):
    next_node = computer_move_calculator(root_node)
    cmd = get_computer_move_command(root_node, next_node)
    print(f"Bilgisayarın hamlesi: {cmd}")
    return next_node


def check_game_over(current_node):
    w_count = current_node.state.count('m')
    w_count = w_count + current_node.state.count('M')
    global game_over
    if w_count == 0:
        game_over = True
    elif w_count == 1:
        m_count = current_node.state.count('w')
        m_count = m_count + current_node.state.count('W')
        if m_count == 1:
            game_over = True


#  -- MAIN --  MAIN --  MAIN --  MAIN --  MAIN --  MAIN --  MAIN --  MAIN --  MAIN --  MAIN --  MAIN --  MAIN --  MAIN --

# veri tabanı bağlantısı
db_connection = sqlite3.connect('dama.db')
db_connection.cursor().execute('drop table if exists node')

# global değişkenler
state_list = []
move_list = []
state_dict = {'m': 'w', 'M': 'W', '0': '0', 'w': 'm', 'W': 'M'}
move_count = 0
node_depth = 0
game_over = False
node_dao = NodeDao(db_connection)
play_in_opposite = False
cmd_reverser_dct = {'A': 'H', 'B': 'G', 'C': 'F', 'D': 'E', 'E': 'D', 'F': 'C', 'G': 'B', 'H': 'A', '(': '(', ')': ')',
                    '1': '8', '2': '7', '3': '6', '4': '5', '5': '4', '6': '3', '7': '2', '8': '1', ' ': ' '}

# başlangıç hazırlıkları
current_node = node_dao.get_by_id(1)
# current_node.state = "000000000000ww000000w000w0000wm000m00m0wmm0mm0000000000000000000"  #buglu durum, yeme kuralını görmüyor... OK
# current_node.state = "000000000w000000w0000m0ww0000000mmM0000wm000m000m0mm00000000000W"  #ata notda problem vardı... OK
# current_node.state = "00000000000w00000w000000000000000w0m0000000000000M00000000000000"  #sona yakın bir durum
user_turn = select_turn()
game_level = select_level()

# sahne...
while not game_over:
    move_list.append(current_node)
    state_list.append(current_node.state)
    if move_count % 2 == user_turn:
        print_table(current_node.state)
        current_node = player_move(current_node)
    else:
        print_table(current_node.state)
        current_node = computer_move(current_node)
    check_game_over(current_node)
    move_count = move_count + 1
    node_dao.add(current_node)


print("Oyun bitti.")
if current_node.result == 1:
    print("Oyun Berabere Bitti.")
elif move_count % 2 == user_turn:
    print("Maalesef Kaybettiniz.")
else:
    print("Tebrikler Kazandınız.")

# veri tabanındaki düğümleri yazdır
node_dao.print_all()

db_connection.commit()
db_connection.close()

