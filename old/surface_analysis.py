import os
import numpy as np
from kapascan.plot import plot
from kapascan.sensor import SENSORS
import analysis
import shelve

datadir = "data"
basefilename = "surface"

with shelve.open(os.path.join(datadir, basefilename + "_measurement")) as file:
    settings= file['settings']

background = np.load(os.path.join(datadir, basefilename + "_background_z.npy"))
background2 = np.load(os.path.join(datadir, basefilename + "_background2_z.npy"))
sample = np.load(os.path.join(datadir, basefilename + "_z.npy"))

x = np.load(os.path.join(datadir, basefilename + "_x.npy"))
y = np.load(os.path.join(datadir, basefilename + "_y.npy"))
z = 0.5 * background + 0.5 * background2 - sample

noise = (background2 - background) * 0.00005
noise -= noise.mean()

diameter = SENSORS[settings['sensor']]['diameter']
stepsize = x[1] - x[0]
diameter_pixel = int(diameter / stepsize + 0.5)
sensor = analysis.sensor_function(diameter_pixel)
z_reconstructed = analysis.wiener(z, sensor, noise)
plot(x, y, z_reconstructed)
