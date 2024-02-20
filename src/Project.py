import os

from src.Package import Package
from src.parsers import parse_package


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

    def traverse_apply(self, func: callable):
        """
        Traverse the directory and apply the function to each java file
        Note: the function should take a single argument - path: str
        """
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if not file.endswith(".java"):
                    continue

                path = os.path.join(root, file)
                func(path)

    def parse_packages(self):
        def parse_package_from_file(path: str):
            with open(path, "r") as f:
                code = f.read()
            package_name = parse_package(code)

            if package_name is None:
                return

            candidate = [p for p in self.packages if p.name == package_name]

            if not candidate:
                package = Package(package_name)
                package.paths.append(str(path))
                self.packages.append(package)
            else:
                candidate[0].paths.append(str(path))

        self.traverse_apply(parse_package_from_file)
