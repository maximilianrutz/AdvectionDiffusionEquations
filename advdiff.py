#!/usr/bin/python

"""Calculate the 2D Advection Diffusion Equations"""

import scipy.integrate
import scipy.fft
import scipy.sparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Physical length of square sides
l = 12
# Number of Grid points (multiple of 2 for FFT algorithm)
m = 2 ** 8
# Total simulation time
t_end = 15
# Frames per second in animation
fps = 5


def rhs_advdiff(t, wt_vec, nu, K, K_vec, m, kx, ky):
    """ Right hand side function for integration"""
    wt = np.reshape(wt_vec, (m, m))
    psit = -wt / K
    psix = np.real(scipy.fft.ifft2(1j * kx * psit))
    psiy = np.real(scipy.fft.ifft2(1j * ky * psit))
    wx = np.real(scipy.fft.ifft2(1j * kx * wt))
    wy = np.real(scipy.fft.ifft2(1j * ky * wt))
    advt = scipy.fft.fft2(wx * psiy - wy * psix)
    advt_vec = np.reshape(advt, m ** 2)
    rhs = -nu * K_vec * wt_vec + advt_vec
    return rhs


# initial conditions
nu = 10e-4
x_center1, y_center1 = -0.2 * l, 0.05 * l
x_center2, y_center2 = 0.1 * l, -0.15 * l
x = np.linspace(-l / 2, l / 2, m + 1)[:-1]
y = np.linspace(-l / 2, l / 2, m + 1)[:-1]
xx, yy = np.meshgrid(x, y)
ww0 = np.exp(-(0.25 * (xx - x_center1) ** 2 + 2 * (yy - y_center1) ** 2)) - np.exp(
    -(0.25 * (xx - x_center2) ** 2 + 2 * (yy - y_center2) ** 2)
)
wt = scipy.fft.fft2(ww0)
wt_vec = np.reshape(wt, m ** 2)

# wave numbers for fourier transform
k = 2 * np.pi / l * np.concatenate([np.arange(0, m / 2), np.arange(-m / 2, 0)])
k[0] = 10e-6
kx, ky = np.meshgrid(k, k)
K = kx ** 2 + ky ** 2
K_vec = np.reshape(K, m ** 2)

# set arguments for ode solver
fun = rhs_advdiff
y0 = wt_vec
t_span = (0, t_end)
evals = t_end * fps
t_eval = np.linspace(0, t_end, evals)
args = [nu, K, K_vec, m, kx, ky]

# solve with scipy
sol = scipy.integrate.solve_ivp(fun=fun, t_span=t_span, y0=y0, t_eval=t_eval, args=args)

# transform for plotting
wt = np.reshape(sol.y, (m, m, evals))
ww = np.real(scipy.fft.ifft2(wt, axes=(0, 1)))

# create list of plotted images for animation
ims = []
fig = plt.figure()
plt.axis("off")
for i in range(ww.shape[2]):
    im = plt.imshow(ww[:, :, i], animated=True, cmap="bwr", aspect="auto")
    ims.append([im])

# create animation
ani = animation.ArtistAnimation(fig, ims, interval=1000 / fps, blit=True)
plt.show()
ani.save("animation.gif", writer="imagemagick", fps=fps)
