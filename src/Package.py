class Package:
    def __init__(self, name):
        self.name = name
        self.classes = []
        self.paths = []
        self.subpackages = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __add__(self, other):
        package = Package(self.name + '+' + other.name)
        package.classes = self.classes + other.classes
        package.paths = self.paths + other.paths

        if other in self.subpackages:
            self.subpackages.remove(other)
        if self in other.subpackages:
            other.subpackages.remove(self)

        package.subpackages = self.subpackages + other.subpackages

        return package

    def add_class(self, class_name: str, path: str):
        self.classes.append(class_name)
        self.paths.append(path)

    def add_subpackage(self, package):
        self.subpackages.append(package)
