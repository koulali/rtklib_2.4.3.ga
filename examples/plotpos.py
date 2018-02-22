import numpy as np 
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # read pos file
    out = np.genfromtxt('pos.out',comments='%')
    #out1 = np.genfromtxt('pos1.out',comments='%')
    
    #plt.figure()
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False,figsize=(10,8))
    ax1.plot(out[:,2],'bo')#;ax1.plot(out1[:,2],'ro')
    ax2.plot(out[:,3],'bo')#;ax2.plot(out1[:,3],'ro')
    ax3.plot(out[:,4],'bo')#;ax3.plot(out1[:,4],'ro')
    f.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
    plt.show()