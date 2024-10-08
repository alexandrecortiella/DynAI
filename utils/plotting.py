import matplotlib.pyplot as plt
import numpy as np

## Plotting 2D trajectories
def plot_trajectories(obs=None, times=None, trajs=None, save=None, figsize=(16, 8)):
    plt.figure(figsize=figsize)
    if obs is not None:
        if times is None:
            times = [None] * len(obs)
        for o, t in zip(obs, times):
            o, t = to_np(o), to_np(t)
            for b_i in range(o.shape[1]):
                plt.scatter(o[:, b_i, 0], o[:, b_i, 1], c=t[:, b_i, 0], cmap=cm.plasma)

    if trajs is not None: 
        #for z in trajs:
        z = trajs
        plt.plot(z[:, 0], z[:, 1], lw=1.5)
        if save is not None:
            plt.savefig(save)
    plt.show()