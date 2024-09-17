import matplotlib.pyplot as plt

plt.style.use( 'ggplot')
x_value=range(1,1001)
y_value=[x**2 for x in x_value]


fig,ax=plt.subplots()

ax.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,s=10)

ax.plot(x_value,y_value,linewidth=3)

#set chart title and lable axes.
ax.set_title("square number",fontsize=24)
ax.set_xlabel("value",fontsize=14)
ax.set_ylabel("square of value", fontsize=14)
#set the range for each axis.
ax.axis([0,1150,0,1_100_000])
ax.ticklabel_format(style='plain')

#set size of thik labels.
ax.tick_params(labelsize=14)
plt.savefig('squars_plot.png',bbox_inches='tight')
plt.show()


'''['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 
'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 
'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
'''
