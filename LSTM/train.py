from pandas import read_csv,DataFrame,concat
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot

# convert series to supervised learning 
def series_to_supervised(data,n_in=1,n_out=1,dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(),list()
	# input sequence(t-n,...,t-1)
	for i in range(n_in,0,-1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1,i)) for j in range(n_vars)]

		#forcast sequence (t,t+1,...,t+n)
		for i in range(0,n_out):
			cols.append(df.shift(-i))
			if i == 0:
				names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
			else:
				names += [('var%d(t+%d)' % (j+1,i)) for j in range(n_vars)]

		#put it all together
		agg = concat(cols, axis=1)
		agg.columns = names
		#drop rows with NaN values
		if dropnan:
			agg.dropna(inplace=True)
		return agg

#load dataset
dataset = read_csv('data//4.csv',header=None)
values = dataset.values

#ensure all data is float
values = values.astype('float32')

#normalize features
scaler = MinMaxScaler(feature_range=(0,1))
scaled = scaler.fit_transform(values)

#split into train and test sets
values = scaled
n_train_num = 12000
train = values[:n_train_num,:]
test = values[n_train_num:,:]


#split into input and outputs
train_X, train_y = train[:,:-1],train[:,-1]
test_X, test_y = test[:,:-1], test[:,-1]

#reshape input to be 3D [samples,timesteps,features]
train_X = train_X.reshape((train_X.shape[0],1,train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0],1,test_X.shape[1]))
print(train_X.shape,train_y.shape,test_X.shape,test_y.shape)

from keras.models import Sequential
from keras.layers import Dense, Activation,LSTM
#design network
model = Sequential()
model.add(LSTM(50,input_shape=(train_X.shape[1],train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae',optimizer='adam')


#fit network
history = model.fit(train_X,train_y,epochs=150,batch_size=1000,validation_data=(test_X,test_y),verbose=0,shuffle=False)

#plot history
pyplot.plot(history.history['loss'],label='train')
pyplot.legend()
pyplot.show()

predict = model.predict(train_X,batch_size=50,verbose=0)
right_num = 0
max_num = 5
for i in range(12000):
	pre_label = 0
	true_label = 0
	if(predict[i]<5/max_num): pre_label=1
	if(predict[i]>=5/max_num and predict[i] <12.5/max_num):pre_label=2
	if(predict[i]>=12.5/max_num and predict[i]<20/max_num):pre_label=3
	if(predict[i]>=20/max_num and predict[i]<30/max_num):pre_label=4
	if(predict[i]>=30/max_num):pre_label=5
	if(train_y[i]<5/max_num): true_label=1
	if(train_y[i]>=5/max_num and train_y[i] <12.5/max_num):true_label=2
	if(train_y[i]>=12.5/max_num and train_y[i]<20/max_num):true_label=3
	if(train_y[i]>=20/max_num and train_y[i]<30/max_num):true_label=4
	if(train_y[i]>=30/max_num):true_label=5
	if(pre_label==true_label):right_num+=1
print (right_num/12000)
