class LockPlayers:

    def __init__(self):
        """
        Constructor for the LockPlayers class
        """
        self.player_lock = 0

    def get_key(self):
        """
        Gets the current lock key
        :return: the key
        """
        return self.player_lock

    def set_key(self, num):
        """
        Sets the lock key
        :param num: the key
        """
        self.player_lock = num
