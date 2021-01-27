import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
np.random.seed(10)
total_number= 1000
image_dir ''

hour= np.random.randint(1,13,size=total_number)
minute = np.random.randint(0,60,size=total_number)
second = np.random.randint(0,60,size=total_number)
angles_h =2*pi*hour/12+2*pi*minute/(12*60)+2*second/(12*60*60)-pi/6.0
angles_m= 2*pi*minute/60+2*pi*second/(60*60)-pi/6.0
angles_s =2*pi*second/60-pi/6.0
second_list= [(angles,0.9) for angles in angles_s]
minute_list= [(angles,0.7) for angles in angles_m]
hour_list= [(angles,0.3) for angles in angles_h]
n=0
for second_hand,minute_hand,hour_hand in zip(second_list,minute_list,hour_list):
    #print(n)
    fig = plt.figure(figsize=(2.5,2.5))
    ax = fig.add_subplot(111, polar=True)
    ax.plot([second_hand[0],second_hand[0]], [0,second_hand[1]], color="black", linewidth=1)
    ax.plot([minute_hand[0],minute_hand[0]], [0,minute_hand[1]], color="black", linewidth=2)
    ax.plot([hour_hand[0],hour_hand[0]], [0,hour_hand[1]], color="black", linewidth=4)
# suppress the radial labels
    plt.setp(ax.get_yticklabels(), visible=False)
# set the circumference labels
    ax.set_xticks(np.linspace(0, 2*pi, 12, endpoint=False))
    ax.set_xticklabels(range(1,13))
# make the labels go clockwise
    ax.set_theta_direction(-1)
# place 0 at the top
    ax.set_theta_offset(1*pi/3.0)
    ax.grid(False)
    plt.ylim(0,1)
    #plt.show()
    plt.savefig(image_dir+str(n)+'_{}_{}_{}.png'.format(hour[n],minute[n],second[n]), dpi=100,bbox_inches='tight')
    n=n+1