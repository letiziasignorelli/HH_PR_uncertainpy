import uncertainpy as un
import numpy as np
import matplotlib.pyplot as plt
import prettyplot as prplt

data = un.Data()
data.load(filename='soma.h5')
soma = data['soma']
new_index = np.zeros(5)
for i in range(5):
    new_index[i] = np.average(a=soma['sobol_total'][i,:], weights=np.sqrt(soma['variance']))
width = 0.2
index = np.arange(1, len(data.uncertain_parameters)+1)*width
prplt.prettyBar(new_index,
                  title='Weighted average of total Sobol indices for soma',
                  palette="husl",
                  xlabels=data.uncertain_parameters,
                  index=index,
                  style="seaborn-darkgrid")
plt.ylim([0, 1])
plt.tight_layout()
plt.savefig('weighted_average_soma')
