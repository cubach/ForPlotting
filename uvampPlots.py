import numpy as np
import matplotlib.pyplot as plt
import matplotlib

sourcename=' '

date=" "

path=
filename=path+
Out_put_file=

#Reading in file and removing header (normally first 4 lines)
# and the bottom 3 lines of text
with open(filename,'r') as f:
    ob_data = f.readlines()[3:-3]

ob_Baseline = []
ob_baseLeft = []
ob_mJy = []
ob_sigma = []
ob_SN = []
ob_exp = []
ob_pts = []

#print ob_data

#Reading in uvamp information
for line in ob_data:
    ln = line.strip()
    
    B1,B2,Amp,Sigma,SN,exp,pts = ln.split()
    
    xx = int(pts)
    
    #Removing amplitudes with zero flux by looking at the number of pts
    if xx > 0:
        ob_Baseline.append(float((float(B1)+float(B2))/2))
        
        ob_baseLeft.append(float(B1))
        
        length = (float(B2)-float(B1))
        
        #Converting from Jy to mJy
        ob_mJy.append(round(float(Amp)*1.0E3,4))
        ob_sigma.append(round(float(Sigma)*1.0E3,4))
        ob_exp.append(round(float(exp)*1.0E3,4))
        
        ob_SN.append(float(SN))
        ob_pts.append(float(pts))

#MAX Range for x and y
XMAX = 30.0
YMAX = 0.4

#For legend: source name
positionX = XMAX-10.0
positionY = YMAX-0.05

#date of observations
positionXX = positionX-3.0
positionYY = positionY-0.03

matplotlib.rcParams.update({'font.size':18})
matplotlib.rcParams['axes.linewidth']=3

#mec - marker_edge_color; mfc - marker_face_color
#ms - marker_size; mew - marker_edge_wigth
#fmt - plot format symbol ( ' ' = only error bars)
plt.errorbar(ob_Baseline,ob_mJy,yerr=ob_sigma,
             mec='black',mfc='white',color='black',
             fmt=' ',barsabove=True, marker='D',ms=10,mew=2)


plt.bar(ob_baseLeft,ob_exp,color='white',linewidth=2,width=length)

#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')

plt.xlabel('$u-v$ distance (k$\lambda$)',fontsize=22)
plt.ylabel("Flux (mJy)",fontsize=22)
plt.ylim([0,YMAX])
plt.xlim([0,XMAX])
plt.text(positionX,positionY,sourcename)
plt.text(positionX,positionYY,date)
plt.minorticks_on()
plt.tick_params('both',length=10,width=2,which='major')
plt.tick_params('both',length=5,width=1.5,which='minor')

plt.show()
#plt.savefig(Out_put_file)





