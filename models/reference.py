class Reference:
    def __init__(self, name, sql_table_name, fields):
        self.name = name
        self.sql_table_name = sql_table_name
        self.fields = fields
        self.get_data_query = f"SELECT {', '.join(self.fields.keys())} FROM {sql_table_name};"

    def __repr__(self) -> str:
        return self.name