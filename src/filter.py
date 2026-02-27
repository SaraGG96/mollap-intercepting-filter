class Filter:
    def execucio(self, username):
        pass


class Autenticacio(Filter):
    def execucio(self, username):
        print(f"Autenticación OK para {username}")


class Autoritzacio(Filter):
    def execucio(self, username):
        print(f"Autorización OK para {username}")