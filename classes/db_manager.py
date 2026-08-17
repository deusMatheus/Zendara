import sqlite3

class db_manager:

    def __init__(self):
        self.connection = sqlite3.connect('./data/db.db')
        self.cursor = self.connection.cursor()

    def get_columns_table(self, tableName):
        return self.cursor.execute(f'PRAGMA table_info({tableName})')
        
    def create_table (self, table_name, values_tuple):
        self.cursor.execute(f'CREATE TABLE {table_name} {values_tuple}')
        self.connection.commit()

    def insert_values(self, table_name, values_list):
        for value_string in values_list:
            self.cursor.execute(f"""INSERT INTO {table_name} VALUES {value_string}""")
        self.connection.commit()

    def delete_tables(self):
        self.cursor.execute('DROP TABLE users')
        self.cursor.execute('DROP TABLE character_sheets')
        self.cursor.execute('DROP TABLE abilities_categories')
        self.cursor.execute('DROP TABLE abilities')
        self.connection.commit()

    def select_values(self, columns_string, table_name):
        return self.cursor.execute(f'SELECT {columns_string} FROM {table_name}').fetchall()

    def select_values_where(self, columns_string, column_where, table_name, value_where):
        return self.cursor.execute(f'SELECT {columns_string} FROM {table_name} WHERE {column_where} = {value_where};').fetchall()

    def reset_all(self):
        self.delete_tables()

        self.create_table('users','(username, password, name, privilege)')

        self.create_table('character_sheets','(character_name, character_species, character_job, character_xp, max_hp, current_hp, strength_score, agility_score, logic_score, spirituality_score, movement_speed, equipment_list, weapons, armor, condition, abilities_categories_ids, abilities_ids)')

        self.create_table('abilities_categories',('(character_id, category_name)'))

        self.create_table('abilities','(character_id, ability_category_id, ability_name, ability_description)')


        # character_id = 1 > Dracorina
        # ability_category_id = 1 > Habilidades de Classe
        # ability_category_id = 2 > Habilidades de Origem
        # ability_id = 1 > Habilidade de Classe 1
        # ability_id = 2 > Habilidade de Origem 1
        # ability_id = 3 > Habilidade de Classe 2
        self.insert_values('character_sheets',[f'("Dracorina","Réptil","Artista", "1", "20", "20", "1","3","1","1","20","equip","weapons","armor","none", "1,2", "1,2,3")'])

        self.insert_values('abilities_categories',[f'("1","Habilidades de Classe")'])
        self.insert_values('abilities_categories',[f'("1","Habilidades de Origem")'])

        self.insert_values('abilities',[f'("1","1","Artista", "Vindo  do  povo  ou  de  um  berço  nobre,  artistas  enxergam  o  mundo  de  formas  diferentes  e  de  vários  aspectos.  O  poder  da  palavra  corre  em  seu coração  e  implora  para  ser  transmitido para os outros animais. Dizem que a Arte  é uma entidade que está aprisionada e triste, e toda vez que um artista tem uma inspiração, é um sonho dessa musa que foi transmitida ao artista e precisa ser transmitido para o resto do mundo.    Você  pode  escolher  2  instrumentos  musicais  ou  instrumentos  de desenho para começar a aventura com você e pode realizar apresentações ou vender seus quadros e desenhos para ganhar dinheiro Tavernas, comércios e outros artistas irão te acolher e ajudar no que precisar caso coopere com eles também.    Perspicácias custam 5 pontos a menos para aprender.")']) # Habilidade de classe

        self.insert_values('abilities',[f'("1","2","Afinidade elemental", "Em  seu  nascimento,  um  pequeno  espírito elemental o escolheu para ser sua casa. Escolha um elemento entre Fogo, água, terra ou ar. Elementais daquele tipo são a princípio amigáveis com você.  Reduz o dano recebido pelo seu personagens do elemento escolhido em 2")']) # Habilidade de origem

        self.insert_values('abilities',[f'("1","2","Olfato apurado", "Você nasceu com o olfato melhor do que o normal. Você ganha +2 de bônus em uma rolagem relacionada à olfato")']) # Habilidade de origem

        self.insert_values('abilities',[f'("1","2","Pele dura", "Seu couro, escama ou pelo é mais resistente que o normal. Você ganha um bônus de +1 de defesa.")']) # Habilidade de origem

        self.insert_values('abilities',[f'("1","2","Sangue frio", "Quando  seu  personagem  sangrar  pela  primeira  vez  em  combate,  você pode usar sua reação para realizar um ataque contra a criatura que foi a última a te atacar. Se não for possível, ataque a criatura hostil mais próxima a você. Até o final do combate você ganha um bônus de +1 de acerto.")']) # Habilidade de origem

        self.insert_values('abilities',[f'("1","2","Sensor natural", "Você nasceu com habilidades sensitivas naturais. Você  consegue  sentir  movimentações  a  até  12  metros  de  você  e  sabe exatamente a direção do movimento..")']) # Habilidade de origem

################################

        self.insert_values('character_sheets',[f'("Max","Aracnídeo","Atirador de elite", "1", "20", "20", "1","3","1","1","20","equip","weapons","armor","none", "1,2", "1,2,3")'])

        self.insert_values('abilities',[f'("2","1","Atirador de Elite", "Você  masterizou  a  arte  do  ataque  a  distância.  Os  inimigos  lhe  temem somente por pensar que você pode estar por perto. Nenhum alvo está longe o suficiente dos seus projéteis, nenhum alvo é veloz demais para a sua mira, nenhum alvo é difícil demais para ser acertado.  Conhecidos pelo apelido de “Sombras assassinas”, os atiradores de elite são uma força indescritível na logística bélica de um exército. Os melhores deles são vistos apenas ao final da batalha, quando estão recolhendo sua munição da montanha de cadáveres que fizeram ser nem ao menos ter saído de sua posição.  Apenas  a  presença  de  um  deles  é  suficiente  para  causar  grande dano psicológico aos inimigos.  Você  ganha  +2  de  acerto  ao  atacar criaturas que não se moveram na última rodada.  Você pode usar sua ação bônus antes de realizar um ataque para se concentrar em  seu  alvo,  ganhando  +2  de  acerto  e  dano  (aumentando  em +2 para cada nível de graduação que você tiver)  Em  um  descanso,  você  pode  fabricar  até  5  munições  usando  apenas  1 componente de criação (pedra, madeira, ferro, etc). Você pode recarregar sua arma com uma reação.")']) # Habilidade de classe

        self.insert_values('abilities',[f'("2","2","Múltiplos Membros", "Como um aracnídeo, você pode andar em qualquer superfície sólida. Além disso, pode usar um equipamento longo/pesado e um equipamento curto ao mesmo tempo.")']) # Habilidade de origem

        self.insert_values('abilities',[f'("2","2","Estoque natural", "Seu corpo consegue se manter mesmo com poucos nutrientes. Você só precisa comer uma vez por dia.")']) # Habilidade de origem

        self.insert_values('abilities',[f'("2","2","Bolsa  de  seda", "Uma  vez  por  descanso  longo  você  pode  realizar  um ataque de teia contra um inimigo. Caso acerte, ele ficará contido. Sua velocidade base é 9 metros")']) # Habilidade de origem

        self.insert_values('abilities',[f'("2","2","Natureza venenosa ", "Você não pode ser envenenado ou receber dano de veneno.")']) # Habilidade de origem

#        print(self.cursor.execute('SELECT * FROM character_sheets').fetchall())
#        print(self.cursor.execute('SELECT * FROM abilities_categories').fetchall())
#        print(self.cursor.execute('SELECT * FROM abilities').fetchall())
#        self.insert_values('character_sheets',[f'("Max","Mamífero","Químico", "1", "20", "20", "1","2","2","1","20","equip","weapons","armor","none")'])
#        self.insert_values('workers', [f'("adm", "adm", "Administrador", "adm")'])

    def list_abilities_categories_by_character(self, characterName):
        character_id = self.cursor.execute(f'SELECT rowid FROM character_sheets WHERE character_name = "{characterName}"').fetchall()[0][0]
        list_of_categories_unformated = self.cursor.execute(f'SELECT category_name FROM abilities_categories WHERE character_id = "{character_id}"').fetchall()
        list_of_categories_formated = []
        for category in list_of_categories_unformated:
            list_of_categories_formated.append(category[0])
        return list_of_categories_formated

    def list_abilities_by_character(self, characterName):
        character_id = self.cursor.execute(f'SELECT rowid FROM character_sheets WHERE character_name = "{characterName}"').fetchall()[0][0]
        list_of_abilities_unformated = self.cursor.execute(f'SELECT ability_category_id, ability_name, ability_description FROM abilities WHERE character_id = "{character_id}"').fetchall()
        list_of_categories_ids = []
        list_of_categories_names = []
        for ability in list_of_abilities_unformated:
            if(ability[0] not in list_of_categories_ids):
                list_of_categories_ids.append(ability[0])
                list_of_categories_names.append(self.get_ability_category_by_id(ability[0]))

        list_of_abilities_formatted = []
        for i in range (len(list_of_categories_ids)):
            for ability in list_of_abilities_unformated:
                if list_of_categories_ids[i] == ability[0]:
                    ability_dict = {
                            'categoria': list_of_categories_names[i],
                            'habilidade':
                            {
                                'nome': f'{ability[1]}',
                                'desc': f'{ability[2]}'
                            }
                        }
                    list_of_abilities_formatted.append(ability_dict)

###########        print(list_of_abilities_unformated)
###########        print(list_of_categories_names)
###########        print(list_of_categories_ids)
###########        print(list_of_abilities_formatted)

#        for ability in list_of_abilities_formatted:
#            print (ability['categoria'])
#            print (ability['habilidade']['nome'])
#            print (ability['habilidade']['desc'])
        return list_of_abilities_formatted

    def get_ability_category_by_id (self, abilityCategoryId):
        return self.cursor.execute(f'SELECT category_name FROM abilities_categories WHERE rowid = {abilityCategoryId}').fetchall()[0][0]
    
    def delete_values(self,tableName, columnName, valueToDelete):
        self.cursor.execute(f'DELETE FROM {tableName} WHERE {columnName}={valueToDelete};')
        self.connection.commit()

# -------------------------------
# db_manager().reset_all()
# -------------------------------

#print(db_manager().list_abilities_categories_by_character('Dracorina'))
#db_manager().list_abilities_by_character('Dracorina')