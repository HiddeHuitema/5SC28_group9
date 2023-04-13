import numpy as np

out = np.load('training-data.npz')
th_train = out['th'] #th[0],th[1],th[2],th[3],...
u_train = out['u'] #u[0],u[1],u[2],u[3],...

data = np.loadtxt('test-prediction-submission-file.csv',delimiter=',')
upast_test = data[:,:15] #N by u[k-15],u[k-14],...,u[k-1]
thpast_test = data[:,15:30] #N by y[k-15],y[k-14],...,y[k-1]
thpred = data[:,30] #all zeros


def create_IO_data(u,y,na,nb):
    X = []
    Y = []
    for k in range(max(na,nb), len(y)):
        X.append(np.concatenate([u[k-nb:k],y[k-na:k]]))
        Y.append(y[k])
    return np.array(X), np.array(Y)

na = 5
nb = 5
Xtrain, Ytrain = create_IO_data(u_train, th_train, na, nb)

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(Xtrain,Ytrain)

Ytrain_pred = reg.predict(Xtrain)
print('train prediction errors:')
print('RMS:', np.mean((Ytrain_pred-Ytrain)**2)**0.5,'radians')
print('RMS:', np.mean((Ytrain_pred-Ytrain)**2)**0.5/(2*np.pi)*360,'degrees')
print('NRMS:', np.mean((Ytrain_pred-Ytrain)**2)**0.5/Ytrain.std()*100,'%')

 #only select the ones that are used in the example
Xtest = np.concatenate([upast_test[:,15-nb:], thpast_test[:,15-na:]],axis=1)

Ypredict = reg.predict(Xtest)

#put solution in the array:
data[:,-1] = Ypredict

data = np.loadtxt('test-prediction-submission-file.csv',delimiter=',')

#copy header:
with open('test-prediction-submission-file.csv') as f:
    header = f.readline()[2:-1]
np.savetxt('test-prediction-submission-file-2.csv', data, header=header, delimiter=',')