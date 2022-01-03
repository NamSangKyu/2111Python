import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/gulim.ttc').get_name()
matplotlib.rc('font',family=font_name)
figure = plt.figure()
axes = figure.add_subplot(111)

data = [0.18,0.3,3.33,3.75,0.38,25,0.25,2.75,0.1]
label = ['비타민 A','비타민 B1','비타민 B2','나이아신','비타민 B6','비타민 C','비타민 D','비타민 E','엽산']

axes.pie(data,labels=label,autopct='%.2f%%')
plt.show()