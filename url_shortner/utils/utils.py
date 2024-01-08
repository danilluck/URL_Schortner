import secrets
from dotenv import dotenv_values
from url_shortner.DB.control import DataBaseOperations


config = dotenv_values('config.env')

class Schortner:
    def __init__(self, url) -> None:
        self.url = url
        self.db = DataBaseOperations()


    def generate_code(self, length=16):
        return secrets.token_hex(length // 2)


    def make_url_schorter(self):
        generated_code = self.generate_code()
        self.db.insert_url_code(url=self.url, url_code = generated_code)
        url = f"{config['host']}/{generated_code}"
        return url
    

class Meta:
    def __init__(self) -> None:
        self.db = DataBaseOperations()

    def get_url(self, code: str):

        url = self.db.get_url_by_code(url_code=code)

        return url 