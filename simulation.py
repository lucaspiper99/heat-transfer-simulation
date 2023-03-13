import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

init_temp = 90  # initial temperature inside the material 
resolution = 13  # number of cells in the simulation per inch of the material
threshold = 10  # sum of temperature differences between iterations for the simulation to end


def create_mesh(resolution: int, init_temp: float) -> np.array:
    mesh = np.pad(
        np.ones((9*resolution, math.ceil(4.5*resolution))) * init_temp,
        ((1, 1), (1, 0)),
        constant_values=((100, 32), (32, 0))
        )
    mask = np.pad(
        np.ones((9*resolution, math.ceil(4.5*resolution))) * init_temp,
        ((1, 1), (1, 0)),
        constant_values=((0, 0), (0, 0))
        )   
    mesh[:(5*resolution+1), 0] = np.arange(100, 32, (32-100)/(5*resolution+1))[:5*resolution+1]
    mesh[(3*resolution+1):(6*resolution+1), (3*resolution+1):] = 212
    mask[(3*resolution+1):(6*resolution+1), (3*resolution+1):] = 0
    return mesh, mask


def laplace_eq(m: np.array, i: int, j: int) -> float:
    if mesh.shape[0] % 2 == 0 and j == (m.shape[1]-1):
        return (m[i-1, j] + m[i+1, j] + m[i, j-1] + m[i, j])/4
    elif mesh.shape[0] % 2 != 0 and j == (m.shape[1]-1):
        return (m[i-1, j] + m[i+1, j] + m[i, j-1] + m[i, j-1])/4
    else:
        return (m[i-1, j] + m[i+1, j] + m[i, j-1] + m[i, j+1])/4


def get_full_mesh(mesh: np.array) -> np.array:
    if mesh.shape[0] % 2 == 0:
        return np.concatenate((mesh, np.flip(mesh, axis=1)), axis=1)
    else:
        return np.concatenate((mesh, np.flip(mesh[:, :-1], axis=1)), axis=1)


mesh, mask = create_mesh(resolution, init_temp)
new_mesh = mesh
iter = 0

# mpl.rcParams['toolbar'] = 'None'
fig = plt.figure("Exercise 2: Simulating and visualising temperature distribution in a material")
fig.suptitle('Temperature Distribution in a Material', fontsize=14)
plt.xlim(0., 9.)
plt.ylim(0., 9.)
plt.xlabel('Horizontal distance [in]')
plt.ylabel('Vertical distance [in]')
im = plt.imshow(get_full_mesh(mesh), extent=[0,9,0,9], animated=True, cmap='magma')
cbar = plt.colorbar()
cbar.set_label('Temperature [ºF]')


def update_fig(*args):
    global mesh, new_mesh, mask, temp_diff, iter
    temp_diff = 0
    iter += 1
    for i, j in np.ndindex(mesh.shape):
        if mask[i, j]:
            new_val = laplace_eq(mesh, i, j)
            temp_diff += abs(new_val - mesh[i, j])
            new_mesh[i, j] = new_val
    
    mesh = new_mesh
    if iter in [1, 10] or iter % 100 == 0:
        print(f'Iteration: {iter}\nTemperature difference: {temp_diff:.1f}')
    if temp_diff < threshold:
        print(f'Iteration: {iter}\nTemperature difference: {temp_diff:.1f}')
        plt.close()
    else:
        im.set_array(get_full_mesh(mesh))
    
    return im,


ani = animation.FuncAnimation(fig, update_fig, interval=10, blit=True)
plt.show()
