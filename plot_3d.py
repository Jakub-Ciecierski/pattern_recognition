import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from symbol_class import SymbolClass


class Plot:
    def __init__(self):
        pass
    def show(self, symbolClasses, numberOfDifferentClasses):
        fig = plt.figure()
        ax = Axes3D(fig)
        x,y,z, colors = [],[],[],[]
        for i in range(0, len(symbolClasses)):
            x.append(symbolClasses[i].characteristicsValues[0])
            y.append(symbolClasses[i].characteristicsValues[1])
            z.append(symbolClasses[i].characteristicsValues[2])
            colors.append(symbolClasses[i].color)
           
        ax.scatter(x,y,z,c=colors,s=4,linewidth='0',marker='o')
        ax.scatter(x[:numberOfDifferentClasses],
                   y[:numberOfDifferentClasses],
                   z[:numberOfDifferentClasses],
                   c='black',
                   s=40,
                   linewidth='0',
                   marker='o') 
        plt.show()


    def show2(self, centroids, symbolClasses, numberOfDifferentClasses):
        fig = plt.figure()
        ax = Axes3D(fig)
        x,y,z, colors = [],[],[],[]
        for i in range(0, len(symbolClasses)):
            x.append(symbolClasses[i].characteristicsValues[0])
            y.append(symbolClasses[i].characteristicsValues[1])
            z.append(symbolClasses[i].characteristicsValues[2])
            colors.append(symbolClasses[i].color)

        
        for centroid in centroids:
            ax.scatter(centroid[0],
                       centroid[1],
                       centroid[2],
                       c='black',
                       s=60,
                       linewidth='0',
                       marker='o')
        ax.scatter(x,y,z,c=colors,s=10,linewidth='0',marker='o')
        plt.show()