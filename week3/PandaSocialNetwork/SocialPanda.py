from Panda import Panda


class PandaSocialNetwork(Panda):

    def __init__(self):
        self.panda_friends = {}
        self.network = []
        self.panda_email = []

    def __getitem__(self, index):
        return self.network[index]

    def has_panda(self, panda):
        if panda in self.panda_friends:
            return True
        return False

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise Exception("PandaAlreadyThere")
        else:
            self.panda_friends[panda] = []
            self.network.append(panda)
            self.panda_email.append(panda.email)

    def make_friends(self, panda1, panda2):
        if panda1 not in self.network:
            self.add_panda(panda1)

        if panda2 not in self.network:
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise Exception("Pandas are already friends")

        self.panda_friends[panda1] = [panda2]
        self.panda_friends[panda2] = [panda1]

    def are_friends(self, panda1, panda2):
        return panda1 in self.panda_friends[panda2] and panda2 in self.panda_friends[panda1]

    def friends_of(self, panda):
        if panda not in self.network:
            return False
        return self.panda_friends[panda]

    def connection_level(self, panda1, panda2):
        if panda1 or panda2 not in network:
            return False
        if are_friends(panda1, panda2):
            return 1
        result = 1


    def are_connected(self, panda1, panda2):
        if panda1 or panda2 not in network:
            return False

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(self.__repr__())
