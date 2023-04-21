


class lock_players:
        
    #player_lock = 0 # 0 means that key is not in use 

    def __init__(self):
        self.player_lock =0

    def get_key(self):
        return self.player_lock

    def set_key(self,num):
        self.player_lock = num





