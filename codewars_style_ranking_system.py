class User:
        
    def __init__(self):
        self.ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank = self.ranks[0]
        self.progress = 0
        
    def inc_progress(self, activity_rank):
        if self.rank != 8:
            d = self.ranks.index(activity_rank) - self.ranks.index(self.rank)
            
            if d > -2:
                if d == 0:
                    progress_points = 3
                elif d == -1:
                    progress_points = 1
                else:
                    progress_points = 10 * d * d
            self.progress += progress_points
            
            if self.progress >= 100:
                n_ranks_progress = self.progress // 100
                self.progress -= n_ranks_progress * 100
                
                if self.ranks.index(self.rank) + n_ranks_progress >= 15:
                    self.rank = 8
                    self.progress = 0
                else:
                    self.rank = self.ranks[self.ranks.index(self.rank) + n_ranks_progress]
        elif activity_rank > 8 or activity_rank < -8 or activity_rank == 0:
            raise IndexError
