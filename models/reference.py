class Reference:
    def __init__(self, name, sql_table_name, fields):
        self.name = name
        self.sql_table_name = sql_table_name
        self.fields = fields
        self.get_data_query = f"SELECT {', '.join(self.fields)} FROM {sql_table_name};"