class Project:
    def __init__(self, path, name):
        self.name = name
        self.path = path

        self.packages = []
        self.classes = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def parse_packages(self):
        pass
