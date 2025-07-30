class StarWarsEntity:
    def __init__(self, name: str, details: dict):
        self.name = name
        self.details = details

    def to_dict(self):
        return {
            "name": self.name,
            "details": self.details
        }