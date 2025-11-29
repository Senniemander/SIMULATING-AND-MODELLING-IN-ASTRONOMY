# Source - https://stackoverflow.com/a
# Posted by Andrew Clark, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-26, License - CC BY-SA 3.0

def load(self, filename="input.dat"):
    d = {"Z0": "z0", "k": "k", "g": "g", "Delta": "D", "t_end": "T"}
    FILE = open(filename)
    for line in FILE:
        name, value = line.split(":")
        value = value.strip()
        if " " in value:
            value = map(float, value.split())
        else:
            value = float(value)
        setattr(self, d[name], value)
