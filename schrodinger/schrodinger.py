# -*- coding: utf-8 -*-
def schrodinger(V_0 , c, n_basis_set, fxn, fl, d_0 , d_1):
    import scipy.ndimage.filters as snf
    import numpy as np
    import scipy.integrate as integrate
    from numpy.polynomial import Polynomial, Legendre
    from numpy import polyder as deriv
    ## crs = open(file_name, "r")
    x = np.linspace(d_0,d_1,1000)
    ## fps = []
    ## for columns in (raw.strip().split() for raw in crs):
        ## fps.append(float(columns[2]))
        ## x.append(float(columns[1]))
    fxn_x = fxn(x)
    ai=[]
    h=[]
    if fl == 'f':
        for i in list(range((n_basis_set))):
            ## b.append(np.exp(1j*2*np.pi*i*x))
            ai.append(integrate.quad(lambda x:fxn(x)*np.exp(1j*2*np.pi*i*x),d_0,d_1  )[0])
            h.append([])
        for i in list(range((n_basis_set))):
            for z in list(range((n_basis_set))):
                h[i].append(integrate.quad(lambda x:(float(-c*-i**2*np.pi**2*np.exp(1j*2*np.pi*i*x)+V_0*np.exp(1j*2*np.pi*i*x))*np.exp(1j*2*np.pi*z*x)),d_0,d_1  )[0])
        ai = np.matrix(ai)
        h = np.matrix(h)
        coeff = h*ai.transpose()
    if fl == 'l':
        delt = snf.laplace(fxn_x)
        grid = []
        for i in list(range(len(delt))):
            grid.append(-c*delt[i]+V_0*fxn_x[i])
        coeefficients = np.polynomial.legendre.legfit(x,grid,n_basis_set)
        coeff = []
        for i in list(range(n_basis_set)):
            coeff.append(coeefficients[i])    
    return coeff
