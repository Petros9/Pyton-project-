from world_elements.platform import Platform
from world_elements.flag import Flag
from world_elements.foe import Foe
from world_elements.tower import Tower

class LevelLoader:
    def __init__(self, filename):
        self.filename = filename

    def load_level(self):
        level_objects = []
        try:
            with open(self.filename, 'r') as f:
                for i, line in enumerate(f):
                    for j in range(len(line)):
                        if (line[j] == '#'):
                            level_objects += [Platform(5 * j + 5, 10 * i + 5)]
                        if(line[j] == '$'):
                            level_objects += [Flag(5 * j + 5, 10 * i + 5)]
                        if(line[j] == '*'):
                            level_objects += [Foe(5 * j + 5, 10 * i + 5)]
                        if (line[j] == '^'):
                            level_objects += [Tower(5 * j + 5, 10 * i + 5)]

        except IOError as er:
            print(f"I/O error: {er.strerror}")

        return level_objects
