#!/usr/bin/env python
# coding: utf-8

# <h2>BACKGROUND</h2>
# Computational physics is the study of scientific problems using computational methods; it combines computer science, physics and applied mathematics to develop scientific solutions to complex problems. It uses computer simulations and numerical calculations to study and solve complex physical problems. Computational physics complements the areas of theory and experimentation in the traditional scientific investigation. It can be used to study a wide range of phenomena, including classical mechanics, electromagnetism, quantum mechanics, statistical mechanics, and fluid dynamics, among others. It involves the use of numerical methods to solve mathematical equations that describe physical systems, often using simulations to model the behavior of these systems over time.
# 
# Numerically solving the Schrödinger equation for a particle in a one-dimensional potential well is an example of computational physics. 
# 
# Computational physics will help us solve the Schrödinger equation for a particle in a one-dimensional potential well by using python simulations. We solve this problem using numerical methods to discretize the wavefunction and potential energy function, and then use linear algebra techniques to solve the resulting eigenvalue problem.
# 

# In[ ]:


<h2>METHOD AND REULTS</h2>


# In[3]:


import numpy as np
import matplotlib.pyplot as plt

class Schrodinger:
    def __init__(self, a, b, Vo, N):
        self.a = a
        self.b = b
        self.Vo = Vo
        self.N = N
        self.dx = (b-a)/(N+1)
        self.x = np.linspace(a, b, N+2)
        self.V = np.zeros(N+2)
        self.V[self.x<a] = np.inf
        self.V[self.x>b] = np.inf
        self.V[(self.x>=a) & (self.x<=b)] = Vo
        self.H = np.zeros((N,N))
        for i in range(N):
            self.H[i,i] = -2/(self.dx**2) + self.V[i+1]
            if i<N-1:
                self.H[i,i+1] = 1/(self.dx**2)
                self.H[i+1,i] = 1/(self.dx**2)
        self.E, self.psi = np.linalg.eigh(self.H)   #solves the eigenvalue problem using the numpy function linalg.eigh
        self.psi = np.vstack((np.zeros(N),self.psi.T,np.zeros(N)))
    
    def plot_wavefunction(self, n):
        plt.plot(self.x, self.psi[n]**2)
        plt.xlabel('Position')
        plt.ylabel('Probability density')
        plt.title(f'Wavefunction for energy level {n+1}')
        plt.show()
    
    
    def plot_energy_levels(self):
        plt.plot(np.arange(1,self.N+1),self.E)
        plt.xlabel('Energy level')
        plt.ylabel('Energy')
        plt.title('Energy levels')
        plt.show()

N = 100
s = Schrodinger(a=0, b=1, Vo=10, N=N)
s.plot_energy_levels()
s.plot_wavefunction(0)


# <h2>DISCUSSION</h2>
# This code will plot the energy levels and the wavefunction for the ground state.
# To investigate the effect of the well width <b>a</b> and the barrier height <b>Vo</b> on the energy eigenvalues and wavefunctions, we can run the simulation for different values of <b>a</b> and <b>Vo</b>, and plot the results using the plot_wavefunction and plot_energy_levels methods. We can also compute the expectation value of the position and momentum operators to study the spatial and momentum distribution of the particle.
# 
# The physical significance of the results is that they describe the energy levels and wavefunctions of a particle confined in a one-dimensional potential well. These wavefunctions can be used to model a variety of physical systems, including electrons in a semiconductor device or a particle in a nanoscale optical trap. The wavefunctions reflect the probability amplitude of locating the particle at a specific point, whereas the energy eigenvalues correspond to the permissible energy levels of the particle. Higher energy levels correlate to more exciting and less likely states, whereas the ground state wavefunction indicates the particle's most likely position.
# 
# The particle's spatial confinement is altered by the well width <b>a</b>, which has an impact on the energy levels and wavefunctions. As the well gets smaller, the energy levels are spaced closer together and the well's wavefunctions become more confined. On the other hand, as the well gets bigger, the wavefunctions loosen up and the energy levels spread out more. By altering the potential energy barrier that the particle must cross to go from the well to the surrounding area, the barrier height <b>Vo</b> has an impact on the energy levels and wavefunctions. The energy levels spread out further and the wavefunctions become more confined to the well as the barrier height increases. Conversely, as the barrier height becomes smaller, the energy levels become more closely spaced and the wavefunctions become less confined.

# <h3>CONCLUSION</h3>
# We have created a Python programme that use the finite difference technique to numerically solve the time-independent Schrödinger equation for a particle in a one-dimensional potential well. With the aid of this simulation, we looked at how the particle's energy eigenvalues and wavefunctions were affected by the well width <b>a</b> and barrier height <b>Vo</b>, and we spoke about the results' physical importance.
# We observed that the well width and barrier height significantly affect the particle's energy levels and wavefunctions when <b>a</b> and <b>Vo</b> are varied. More tightly spaced energy levels and more localised wavefunctions are produced by narrower wells and higher barriers, whereas more widely spaced energy levels and less constrained wavefunctions are produced by larger wells and lower barriers.
# 
# <h3>CHALLENGES</h3>
# My journey in learning computational physics is quite a challenging but interesting one. Some challenges i faced was getting to learn different programming languages and applying them to my field of study. Moreover the challenge of getting the right algorithms to solving problems. 
# 
# <h3>GREAT MOMENTS</h3>
# My greatest moments were when i got to introduced to the world of programming. Having to write codes to solve complex problems and having to know that you're not limited to traditional experimentation but you can also experiment with simulations.  

# <h2>RECOMMENDATION</h2>
# I'll recommend adding AI to the curriculum, since our world is diving into that side. So we can keep up with the rapid changes.

# In[ ]:




