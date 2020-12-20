# Quantum Mechanical Systems
This generic code solves for, and plots, the eigenfunctions and eigenvalues of a particle in a one-dimensional potential, based on the finite difference method code introduced by @mholtrop. The potential array may be modified by the user. Interesting potentials are:

1. The quantum harmonic oscillator
V = x**2
2. The finite square well
# well depth
d = 5

# well width (spans one-third of the x axis range)
a = int(n/3)
b = int(2*n/3)

V = np.zeros(n)
V[0:a] = d
V[b:n] = d
3. The finite barrier
# Barrier height
h = 5

# Barrier Width (spans one-third of the x axis range)
a = int(n/3)
b = int(2*n/3)

V = np.zeros(n)
V[a:b] = h
This potential generates pairs of eigenfunctions, as the matrix method does not specify from which side the particle enters the system.

4. The sine-squared function
V = np.sin(x)**2
This potential generates eigenfunctions similar to those of a particle in the periodic potential of a lattice.
