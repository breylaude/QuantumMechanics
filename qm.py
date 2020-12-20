import numpy as np
import matplotlib.pyplot as plt

hbar = 1
m = 1

# the x axis range
lim = 4
step = 0.01
x = np.arange(-lim, lim, step)
n = len(x)

# the potential function
V = x**2

# represents the double derivative operator as a matrix using the finite difference method
mdd = 1/(step**2) * (np.diag(np.ones(n-1), k=-1)
                            - 2 * np.diag(np.ones(n))
                            + np.diag(np.ones(n-1), k=1))

# sets up the hamiltonian as a matrix, and computes its eigenstuff
H = -(hbar**2)/(2.0 * m) * mdd + np.diag(V)
E, psi_t = np.linalg.eigh(H)
psi = np.transpose(psi_t)

# plotting the eigenfunctions and printing the eigenvalues
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, V, color='k')
print('Energies of the bound states:')
for i in range(len(E)):
    if E[i] < max(V):
        print('E%s = %.2f' %(i, E[i]))
        ax.plot(x, E[i] + 8*psi[i])
    else:
        break
ax.grid()
ax.set_xlabel('Position: x')
ax.set_ylabel('Energy: E')
plt.show()
