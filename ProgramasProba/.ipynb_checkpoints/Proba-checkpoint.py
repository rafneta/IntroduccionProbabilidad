
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np 
from scipy.integrate import quad


# In[ ]:


def gfdvac(Intervalo,f,titulo='Funcion de densidad de probabilidad $f(x)$',          guardar=False):
    fig=plt.figure(figsize=(8,4))#
    ax=plt.axes()
    x=np.linspace(Intervalo[0],Intervalo[1],300)
    y=f(x)
    ax.plot(x,y,c='r',lw=3,label=r'Grafica de $f(x)$')
    ax.grid()
    ax.set_xlabel('Valores de la variable aleatoria $X$',fontsize=15)
    ax.set_ylabel('Valores de $f(x)$',fontsize=15)
    ax.set_title('Funcion de densidad de probabilidad $f(x)$',fontsize=20)
    leg = plt.legend(loc='best', shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.9)
    ax.xaxis.set_label_coords(0.5, -0.05)
    ax.yaxis.set_label_coords(-0.08,0.5)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    xlim=ax.get_xlim()
    ylim=ax.get_ylim()
    ax.set_xlim(min(xlim[0]*(0.9),xlim[0]*(1.1)),max(xlim[1]*1.1,xlim[1]*0.9))
    ax.set_ylim(-0.2,max(ylim[1]*1.1,ylim[1]*0.9))
    if guardar:
        plt.savefig("fvac.png")# Se puede guardar solo en el formato deseado
        plt.savefig("fvac.pdf")#
        plt.savefig("fvac.jpg")#
    plt.show()



# In[ ]:


def gFdfvac(Intervalo,f,titulo='Funcion de distribución $F(x)$',          guardar=False):
    
    x=np.linspace(Intervalo[0],Intervalo[1],300)

    def Fdef(x,f):
        F=quad(f, -np.inf,x, full_output=1)
        return F[0]
    
    Fdefvectorizada=np.vectorize(Fdef)
    
    
    fig=plt.figure(figsize=(8,4))#
    ax=plt.axes()
    
    y=Fdefvectorizada(x,f)

    ax.plot(x,y,c='r',lw=3,label=r'Grafica de $F(x)$')
    ax.grid()
    ax.set_xlabel('Valores de la variable aleatoria $X$',fontsize=15)
    ax.set_ylabel('Valores de $F(x)$',fontsize=15)
    ax.set_title('Funcion de distribucion $F(x)$',fontsize=20)
    leg = plt.legend(loc='best', shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.9)
    ax.xaxis.set_label_coords(0.5, -0.05)
    ax.yaxis.set_label_coords(-0.08,0.5)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    xlim=ax.get_xlim()
    ylim=ax.get_ylim()
    ax.set_xlim(min(xlim[0]*(0.9),xlim[0]*(1.1)),max(xlim[1]*1.1,xlim[1]*0.9))
    ax.set_ylim(-0.2,max(ylim[1]*1.1,ylim[1]*0.9))
    if guardar:
        plt.savefig("Fvac.png")# Se puede guardar solo en el formato deseado
        plt.savefig("Fvac.pdf")#
        plt.savefig("Fvac.jpg")#
    plt.show()


# In[2]:


def gfpvad(x,f,          titulo='Funcion de probabilidad $f(x)$',guardar=False,etiquetas=True):
    tam_marcador=12
    fig=plt.figure(figsize=(8,4))#
    ax=plt.axes()
    ax.plot(x,f,'bo',ms=tam_marcador,label=r'Grafica de $f(x)$')
    ax.vlines(x, [0], f,colors='b', lw=5, alpha=0.3)
    x=np.concatenate([np.array([x[0]-1]),x,np.array([x[-1]+1])])
    
    if etiquetas:
        plt.xticks(x)
        plt.yticks(f)
    
    ax.grid()
    ax.set_xlabel('Valores de la variable aleatoria $X$',fontsize=15)
    ax.set_ylabel('Probabilidad $f(x)$',fontsize=15)
    ax.set_title('Funcion de probabilidad $f(x)$',fontsize=20,color='r')
    #leg = plt.legend(loc='best', shadow=True, fancybox=True)
    #leg.get_frame().set_alpha(0.9)
    ax.xaxis.set_label_coords(0.5, -0.05)
    ax.yaxis.set_label_coords(-0.08,0.5)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    xlim=ax.get_xlim()
    ylim=ax.get_ylim()
    ax.set_xlim(min(xlim[0]*(0.9),xlim[0]*(1.1)),max(xlim[1]*1.1,xlim[1]*0.9))
    ax.set_ylim(-0.01,max(ylim[1]*1.1,ylim[1]*0.9))
    if guardar:
        plt.savefig("fvad.png")# Se puede guardar solo en el formato deseado
        plt.savefig("fvad.pdf")#
        plt.savefig("fvad.jpg")#
    
    plt.show()


# In[ ]:


def gFdfvad(x,f,          titulo='Funcion de distribucion $F(x)$',guardar=False, etiquetas=True):
    tam_marcador=12
    
    x1=np.concatenate([np.array([x[0]-1]),x,np.array([x[-1]+1])])
    f1=np.concatenate([np.array([0]),f,np.array([0])])
    a=x1.shape
    fig=plt.figure(figsize=(8,4))#
    ax=plt.axes()
    b=0
    for i in range(a[0]-1):
        b=b+f1[i]
        ax.hlines(b,x1[i],x1[i+1],colors='b', lw=5, alpha=0.3)
    
    a=f.shape
    for i in range(1,a[0]):
        f[i]=f[i]+f[i-1]
        
    ax.plot(x,f,'bo',ms=tam_marcador)
    x=np.concatenate([np.array([x[0]-1]),x,np.array([x[-1]+1])])
    
    if etiquetas:
        plt.xticks(x)
        plt.yticks(f)
    ax.grid()
    ax.set_xlabel('Valores de la variable aleatoria $X$',fontsize=15, color='b')
    ax.set_ylabel(' $F(x)$',fontsize=15,color='b')
    ax.set_title(titulo,fontsize=20,color='b')
    #leg = plt.legend(loc='best', shadow=True, fancybox=True)
    #leg.get_frame().set_alpha(0.9)
    ax.xaxis.set_label_coords(0.5, -0.05)
    ax.yaxis.set_label_coords(-0.05,0.5)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    xlim=ax.get_xlim()
    ylim=ax.get_ylim()
    ax.set_xlim(min(xlim[0]*(0.9),xlim[0]*(1.1)),max(xlim[1]*1.1,xlim[1]*0.9))
    ax.set_ylim(-0.01,max(ylim[1]*1.1,ylim[1]*0.9))
    if guardar:
        plt.savefig("Fvad.png")# Se puede guardar solo en el formato deseado
        plt.savefig("Fvad.pdf")#
        plt.savefig("Fvad.jpg")#
    
    plt.show()

