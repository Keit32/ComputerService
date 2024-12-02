class Reference:
    def __init__(self, name, sql_table_name, fields, get_data_query, insert_data_query):
        self.name = name
        self.sql_table_name = sql_table_name
        self.fields = fields
        self.get_data_query = get_data_query
        self.get_data_by_id_query = f"SELECT * FROM {self.sql_table_name} WHERE id = ?"
        self.insert_data_query = insert_data_query

    def __repr__(self) -> str:
        return self.name