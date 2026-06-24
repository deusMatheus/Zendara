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
        self.connection.commit()

    def select_values(self, columns_string, table_name):
        return self.cursor.execute(f'SELECT {columns_string} FROM {table_name}').fetchall()

    def select_values_where(self, columns_string, column_where, table_name, value_where):
        return self.cursor.execute(f'SELECT {columns_string} FROM {table_name} WHERE {column_where} = {value_where};').fetchall()

    def reset_all(self):
        self.delete_tables()
        self.create_table('users','(username, password, name, privilege)')
        self.create_table('character_sheets','(character_name, character_species, character_job, character_xp, max_hp, current_hp, strength_score, agility_score, logic_score, spirituality_score, movement_speed, equipment_list, weapons, armor, condition)')
        self.insert_values('character_sheets',[f'("Dracorina","Réptil","Artista", "1", "20", "20", "1","3","1","1","20","equip","weapons","armor","none")'])
#        self.insert_values('character_sheets',[f'("Max","Mamífero","Químico", "1", "20", "20", "1","2","2","1","20","equip","weapons","armor","none")'])
#        self.insert_values('workers', [f'("adm", "adm", "Administrador", "adm")'])
    
    def delete_values(self,tableName, columnName, valueToDelete):
        self.cursor.execute(f'DELETE FROM {tableName} WHERE {columnName}={valueToDelete};')
        self.connection.commit()

# -------------------------------
db_manager().reset_all()
# -------------------------------