import matplotlib.pyplot as plt
from random import choice
DIRECTIONS = [1, -1]
DISTANCES = [0, 1, 2, 3, 4]
class RandomWalk:
    '''A class to generate random walks.'''
    #all walks start at (0,0).
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]
    def get_step():
        direction=choice(DIRECTIONS)
        distance=choice(distance)
        return direction*distance
        
        
        # point in the walk
        # keep taking steps untill the walks reaches the desired length.   
    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            x_step=self.get_step()
            y_step=self.get_step()
            
            
            #decide which direction to go and how far to go , and how far to go.
           
            # reject moves that go nowhere.
            if x_step==0 and y_step==0:
                continue
            # calculate the new position.
            x=self.x_values[-1]+x_step
            y=self.y_values[-1]+y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
    def plot_walk(self):
        
        """
        Plot the points in the random walk using Matplotlib.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.x_values, self.y_values, linewidth=1)
        plt.title("Random Walk", fontsize=24)
        plt.xlabel("X", fontsize=14)
        plt.ylabel("Y", fontsize=14)
        plt.show()