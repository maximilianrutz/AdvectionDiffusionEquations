# Advection Diffusion Equations
A simple script showcasing how little code is needed to solve for the vorticity in the advection diffusion equations in 2D

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{200}&space;\begin{align*}&space;\omega_t&space;&plus;&space;[\Psi,\omega&space;]&space;&=&space;\nu\cdot\nabla^2\omega&space;\\&space;\nabla^2&space;\Psi&space;&=&space;\omega,&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{200}&space;\begin{align*}&space;\omega_t&space;&plus;&space;[\Psi,\omega&space;]&space;&=&space;\nu\cdot\nabla^2\omega&space;\\&space;\nabla^2&space;\Psi&space;&=&space;\omega,&space;\end{align*}" title="\begin{align*} \omega_t + [\Psi,\omega ] &= \nu\cdot\nabla^2\omega \\ \nabla^2 \Psi &= \omega, \end{align*}" /></a>

with fast fourier transforms from Pythons high level scipy package for scientific computing. 

![Simulation Result](https://github.com/maximilianrutz/AdvectionDiffusionEquations/blob/master/animation.gif)

## Usage
Use pipenv to install all packages,
```
cd AdvectionDiffusionEquations
pipenv install
```
then activate the environment and call the script.
```
pipenv shell
python advdiff.py
```
The script should run a couple of seconds (<30), show an animation and save it as a gif. 

## Credits
Inspired by a great lecture series on [Scientific Computing](https://www.youtube.com/playlist?list=PL2e45QSKfSj3jU4piHvVe-SIZU6CTAdve) by Nathan Kutz
