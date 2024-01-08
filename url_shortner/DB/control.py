from typing import Any
from url_shortner.DB.tables import UrlsCodes, db_session


class DataBaseOperations:
    def __init__(self) -> None:
        self.db_connection = db_session
    
    def insert_url_code(self, url: str, url_code: str):
        insert_data = UrlsCodes(url=url, code=url_code)
        self.db_connection.add(insert_data)
        self.db_connection.commit()

    def get_url_by_code(self, url_code: str) -> str: 
        row = self.db_connection.query(UrlsCodes).filter(UrlsCodes.code == url_code).first()
        return row.url 