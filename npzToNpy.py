import numpy as np

data = np.load('./video5131024-rgb.npz')

for name in data.files:
    print(name)
    if (name == 'feature'):
        print(data[name].shape)
        np.save('./video5131024-rgb' + name + '.npy', data[name])