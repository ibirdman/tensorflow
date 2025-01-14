import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class logistic(object):
    def __init__(self):
        self.W = None
    def train(self,X,y,learn_rate = 0.01,num_iters = 5000):
        num_train,num_feature = X.shape
        #init the weight
        self.W = 0.001*np.random.randn(num_feature,1).reshape((-1,1))
        loss = []
        
        for i in range(num_iters):
            error,dW = self.compute_loss(X,y)
            self.W += -learn_rate*dW
            
            loss.append(error)
            if i%200==0:
                print('i=%d,error=%f' %(i,error))
        return loss
    
    def compute_loss(self,X,y):
        num_train = X.shape[0]
        h = self.output(X)
        loss = -np.sum((y*np.log(h) + (1-y)*np.log((1-h))))
        loss = loss / num_train
        
        dW = X.T.dot((h-y)) / num_train
    
        return loss,dW
    
    def output(self,X):
        g = np.dot(X,self.W)
        return self.sigmod(g)
    def sigmod(self,X):
        return 1/(1+np.exp(-X))
    
    def predict(self,X_test):
        h = self.output(X_test)
        y_pred = np.where(h>=0.5,1,0)
        return y_pred


c1_x = [[1, 1], [2, 2], [3,3], [4,4]]
c1_y = [1 for i in range(len(c1_x))]
c1_x = np.transpose(c1_x)
print(c1_x)
plt.scatter(c1_x[0], c1_x[1], c = 'b', marker = 'x', edgecolor='none', s=30)

c2_x = [[1, 3], [2, 5], [3,7], [4,9]]
c2_y = [0 for i in range(len(c2_x))]
c2_x = np.transpose(c2_x)
print(c2_x)
plt.scatter(c2_x[0], c2_x[1], c = 'r', marker = 'o', edgecolor='none', s=40)

Y = np.hstack((c1_y, c2_y))

plt.show()

print(Y)
