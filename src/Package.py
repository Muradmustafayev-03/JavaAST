class Package:
    def __init__(self, name):
        self.name = name
        self.paths = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __add__(self, other):
        package = Package(self.name + '+' + other.name)
        package.paths = self.paths + other.paths

        return package
