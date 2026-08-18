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
        self.create_table('character_sheets','(character_name, character_species, character_job, character_xp, max_hp, current_hp, strength_score, agility_score, logic_score, spirituality_score, movement_speed, equipment_list, weapons, armor, condition)')
        self.create_table('abilities_categories',('(character_id, category_name)'))
        self.create_table('abilities','(character_id, ability_category_id, ability_name, ability_description)')

    def list_abilities_categories_by_character(self, characterName):
        character_id = self.cursor.execute(f'SELECT rowid FROM character_sheets WHERE character_name = "{characterName}"').fetchall()[0][0]
        list_of_categories_unformated = self.cursor.execute(f'SELECT category_name FROM abilities_categories WHERE character_id = "{character_id}"').fetchall()
        list_of_categories_formated = []
        for category in list_of_categories_unformated:
            list_of_categories_formated.append(category[0])
        return list_of_categories_formated

    def list_abilities_categories_by_character(self, characterName):
        character_id = self.get_character_id_by_name(characterName)
        return self.cursor.execute(f'SELECT category_name FROM abilities_categories WHERE character_id = "{character_id}"').fetchall()

    def list_abilities_by_character(self, characterName):
        character_id = self.get_character_id_by_name(characterName)
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

    def get_ability_category_id_by_name (self,abilityCategoryName):
        return self.cursor.execute(f'SELECT rowid FROM abilities_categories WHERE category_name = "{abilityCategoryName}"').fetchall()[0][0]

    def get_character_id_by_name (self, characterName):
        return self.cursor.execute(f'SELECT rowid FROM character_sheets WHERE character_name = "{characterName}"').fetchall()[0][0]

    def create_character (self, characterName, characterSpecies, characterJob, maxHP, strengthScore, agilityScore, logicScore, spiritualityScore, movementSpeed):
        self.insert_values('character_sheets',[f'("{characterName}","{characterSpecies}","{characterJob}", "0", "{maxHP}", "{maxHP}", "{strengthScore}","{agilityScore}","{logicScore}","{spiritualityScore}","{movementSpeed}","empty","empty","empty","none")'])
        character_id = self.get_character_id_by_name(characterName)
        self.insert_values('abilities_categories',[f'("{character_id}","Habilidades de Vocação")'])
        self.insert_values('abilities_categories',[f'("{character_id}","Habilidades de Espécie")'])

    def create_ability (self, abilityName, abilityDesc, abilityCateg, characterName):
        character_id = self.get_character_id_by_name(characterName)
        ability_category_id = self.get_ability_category_id_by_name(abilityCateg)
        self.insert_values('abilities',[f'("{character_id}","{ability_category_id}","{abilityName}","{abilityDesc}")'])

    def delete_values(self,tableName, columnName, valueToDelete):
        self.cursor.execute(f'DELETE FROM {tableName} WHERE {columnName}={valueToDelete};')
        self.connection.commit()

# -------------------------------
# db_manager().reset_all()
#db_manager().create_character('Bob','Ave','Químico','20','0','0','5','1','20')
#db_manager().insert_values('abilities',[f'("3","5","Ability Name Test","Ability Description Test")'])
# # -------------------------------

#print(db_manager().list_abilities_categories_by_character('Dracorina'))
#db_manager().list_abilities_by_character('Dracorina')

