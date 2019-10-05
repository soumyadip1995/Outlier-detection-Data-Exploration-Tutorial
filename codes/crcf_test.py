import numpy as np
import matplotlib.pyplot as plt


def gaussian(probs, means, covs, count=100):
	counts= np.random.multinomial(count, probs, size=1)[0] #how many points are there in each component
	#generate the data
	data= [np.random.multivariate_normal(means[i], covs[i],count) for i, count in enumerate(counts)]
	#combine the data
	data= np.concatenate(data)

	#shuffling the data
	index_new= np.arange(data.shape[0])
	np.random.shuffle(np.arange(data.shape[0]))
	data= data[index_new]
	return data


def generate(n, rate_anomaly):

	# Calculate how many data points there will be in each category
    typ_count, count_anomaly = np.random.multinomial(n, [1-rate_anomaly, rate_anomaly], size=1)[0]

    # Describe typ data with a 2 component Gaussian mixture
    typ_means = [[8, 8],      # mean of component 1
                    [-8, -8]]     # mean of component 2
    typ_covs = [[[1,0],[0,1]],  # covariance matrix of component 1
                    [[1,0],[0,1]]]  # covariance matrix of compoinent 2
    typ_probs = [0.5,              # probability of component 1
                  0.5]              # probability of component 2
    typ_data = gaussian(typ_probs, typ_means, typ_covs, count=typ_count)

    # Describe anomalous data with a 2 component Gaussian mixture
    anomalous_means = [[20, -20],            # mean of component 1
                      [0, 0]]                # mean of component 2
    anomalous_covs = [[[0.5, 0], [0, 0.5]],  # covariance of component 1
                      [[10, 0], [0, 10]]]    # covariance of component 2
    anomalous_ps = [0.1,                      # probability of component 1
                  0.9]                       # probability of component 2
    anomalous_data = gaussian(anomalous_ps, anomalous_means, anomalous_covs, count=count_anomaly)

 

  # Combine the data but preserve the labeling
    x = np.concatenate([typ_data, anomalous_data])
    y = np.concatenate([np.repeat(0, typ_count), np.repeat(1, count_anomaly)])
    new_index = np.arange(y.shape[0])
    np.random.shuffle(new_index)
    y = y[new_index]
    x = x[new_index]
    return x, y

def plot_anom(x, y):
    """ plots anomalies with red and typ with green"""
    fig, ax = plt.subplots()
    ax.scatter(x[:,0], x[:,1], s=3, 
               c=['red' if yy else 'green' for yy in y])
    fig.show()



n = 500  # number of data points to generate
rate_anomaly = 0.1  # the rate at which anomalous points occur
x, y = (n, rate_anomaly)
plot_anom(x, y)





 

