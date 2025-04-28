class ChessTurns:
    def __init__(self):
        self.players=["white","Back"]
        self.index=0


    def __iter__(self):
        return self

    def __next__(self):

        player=self.players[self.index]
        self.index=(self.index+1)%2      #1white,1black
        return player

turns = ChessTurns() #create iterator

print(next(turns)) #white
print(next(turns))  # black
print(next(turns))  # white
print(next(turns)) #black

