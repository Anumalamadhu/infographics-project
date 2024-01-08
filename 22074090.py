# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:26:13 2024

@author: Madhu 
"""

#importing matplotlib.pyplot and pandas libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

#reading crop_production.csv file
crop_production = pd.read_csv("ICRISAT-District Level Data.csv")

#Creating infographics for crop production in India using Gridspec
fig = plt.figure(figsize=(18, 14))
plt.axis('off')
#Giving Title and hiding axis
plt.title('Crop production in India over 4 decades', fontsize=28)

#Using GridSpec
grid = plt.GridSpec(14, 18, hspace=0.75, wspace=0.75)

#Adding Subplot for Name and Student Id
ax = fig.add_subplot(grid[0:1, :])
text = '''Name: Madhu Anumala
Student Id: 22074090'''
ax.text(0.5, 0, text, fontsize=16, ha='center')
ax.axis('off')

#getting average production for the below crops
avg_crop_production = crop_production.groupby('Year', as_index=False)[
    ['RICE PRODUCTION (1000 tons)',
     'GROUNDNUT PRODUCTION (1000 tons)',
     'WHEAT PRODUCTION (1000 tons)',
     'OILSEEDS PRODUCTION (1000 tons)',
     'SUGARCANE PRODUCTION (1000 tons)']].mean()

#lineplot
ax1 = fig.add_subplot(grid[1:4, 1:8])

ax1.plot(avg_crop_production['Year'],
         avg_crop_production['RICE PRODUCTION (1000 tons)'],
         label='RICE')
ax1.plot(avg_crop_production['Year'],
         avg_crop_production['GROUNDNUT PRODUCTION (1000 tons)'],
         label='GROUNDNUT')
ax1.plot(avg_crop_production['Year'],
         avg_crop_production['WHEAT PRODUCTION (1000 tons)'],
         label='WHEAT')
ax1.plot(avg_crop_production['Year'],
         avg_crop_production['OILSEEDS PRODUCTION (1000 tons)'],
         label='OILSEEDS')
ax1.plot(avg_crop_production['Year'],
         avg_crop_production['SUGARCANE PRODUCTION (1000 tons)'],
         label='SUGARCANE')

ax1.set_xlabel('Year')
ax1.set_ylabel('Avg crop production in tons (1000)')
ax1.set_title('Crop production in India over 4 decades')
ax1.legend()
ax1.grid()
ax1.legend(bbox_to_anchor=(0.9999, 1), loc='upper left',
           borderaxespad=0,
           title='Crop type')

#explaination for the line graph
ax2 = fig.add_subplot(grid[1:5, 9:])
text = '''
    We have demonstrated a line graph as we have data related with time.
    This line graph depicts the average production of
    5 most cultivated crops in India
    over 4 decades from 1978 to 2018.   
                                                                              
   It is observable that average production
   of Rice is recorded highest and maintained the same trend 
   throughout the 4 decades following with
   the crops Wheat, Sugarcane, whereas, cultivation of groundnut observed with 
   least following with oilseeds. 

  To conclude, in my point of view majority of people in 
 India consume Rice and wheat.
'''
ax2.text(0.5, 0, text, fontsize=13, ha='center')
ax2.axis('off')

#subplot2
#using sum function to get the sum of production crops by all states
sum_of_crop_production = crop_production.groupby('Year', as_index=False)[
    ['RICE PRODUCTION (1000 tons)',
     'GROUNDNUT PRODUCTION (1000 tons)',
     'WHEAT PRODUCTION (1000 tons)',
     'OILSEEDS PRODUCTION (1000 tons)',
     'SUGARCANE PRODUCTION (1000 tons)']].sum()

sum_of_crop_production = sum_of_crop_production.set_index('Year')
#adding a row called grand total and performed sum operation to get total production by each crop
sum_of_crop_production.loc['Grand Total'] = sum_of_crop_production.sum()

# list for exploding pie chart
e = [0.1, 0, 0, 0, 0]
label = ['RICE', 'GROUNDNUT', 'WHEAT', 'OILSEEDS', 'SUGARCANE']

# plot for pie chart
ax3 = fig.add_subplot(grid[6:10, 0:5])

ax3.pie(sum_of_crop_production.loc['Grand Total'], labels=label,
        explode=e, autopct='%.2f%%',
        shadow={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9}, startangle=90)

ax3.legend(bbox_to_anchor=(1.5, 1.5), borderaxespad=0,
           title='Crop type')
ax3.set_title('Production by each crop')

# explanation for pie chart
ax4 = fig.add_subplot(grid[7:14, 0:5])
text = '''
The above pie chart depicts the
proportions of each crop 
cultivated in India. We can notice
that Groundnut has recorded 
least with 3.64 percentage 
when compared to the other crops.
However, Rice and wheat are observed
with highest ratios with 39.84 and 33.71.
 
'''
ax4.text(0.5, 0, text, fontsize=13, ha='center')
ax4.axis('off')

# subplot3
# created a new dataframe over states and then sorted to get top states producing these crops.
crop_productions_by_states = crop_production.groupby('State Name', as_index=False)[
    ['RICE PRODUCTION (1000 tons)',
     'GROUNDNUT PRODUCTION (1000 tons)',
     'WHEAT PRODUCTION (1000 tons)',
     'OILSEEDS PRODUCTION (1000 tons)',
     'SUGARCANE PRODUCTION (1000 tons)']].sum()

# sorted the values using .sort_values function to get top 5 states producing these crops in high amount.
crop_productions_by_states = crop_productions_by_states.sort_values(by=[
    'RICE PRODUCTION (1000 tons)', 'GROUNDNUT PRODUCTION (1000 tons)',
    'WHEAT PRODUCTION (1000 tons)', 'OILSEEDS PRODUCTION (1000 tons)',
    'SUGARCANE PRODUCTION (1000 tons)'], ascending=False)

barWidth = 0.25

# stacked bar plot
ax5 = fig.add_subplot(grid[6:9, 6:10])

ax5.bar(crop_productions_by_states['State Name'][0:5],
        crop_productions_by_states['RICE PRODUCTION (1000 tons)'][0:5],
        label='RICE', width=barWidth, alpha=0.5)
ax5.bar(crop_productions_by_states['State Name'][0:5],
        crop_productions_by_states['GROUNDNUT PRODUCTION (1000 tons)'][0:5],
        label='GROUNDNUT', width=barWidth)
ax5.bar(crop_productions_by_states['State Name'][0:5],
        crop_productions_by_states['WHEAT PRODUCTION (1000 tons)'][0:5],
        label='WHEAT', width=barWidth, alpha=0.8)
ax5.bar(crop_productions_by_states['State Name'][0:5],
        crop_productions_by_states['OILSEEDS PRODUCTION (1000 tons)'][0:5],
        label='OILSEEDS', width=barWidth, alpha=0.4)
ax5.bar(crop_productions_by_states['State Name'][0:5],
        crop_productions_by_states['SUGARCANE PRODUCTION (1000 tons)'][0:5],
        label='SUGARCANE', width=barWidth, alpha=0.9)

ax5.set_xticks(crop_productions_by_states['State Name'][0:5])
ax5.set_xticklabels(crop_productions_by_states['State Name'][0:5],
                    rotation=45)
ax5.set_title('Crop production by Top 5 States ')
ax5.set_xlabel('State Names')
ax5.set_ylabel('Crop production in tons (1000)')
ax5.legend()
ax5.grid()
ax5.legend(bbox_to_anchor=(0.9999, 1), loc='upper left', borderaxespad=0,
           title='Crop type')

# explanation for the stacked bar plot.
ax6 = fig.add_subplot(grid[8:14, 7:11])
text = '''
The above stacked bar Graph illustrates the
the production of each crop by the top 5 states.

It is noticeable that Uttar Pradesh
has the highest sugarcane production. Whereas, 
Orissa and West Bengal have recorded 
with the least productions.

To conclude, the Government should focus on their
states to increase their production for 
the maximum number of crops which will 
help them to increase their revenue.
'''

ax6.text(0.5, 0, text, fontsize=13, ha='center')
ax6.axis('off')

# subplot4
# created a dataframe vegetable_area over state names to get top 7 states
vegetables_area = crop_production.groupby('State Name')[['VEGETABLES AREA (1000 ha)']].sum()

# sorted the values to get top state names
vegetables_area = vegetables_area.sort_values(by=['VEGETABLES AREA (1000 ha)'], ascending=False)

# resetting the index
vegetables_area = vegetables_area.reset_index()

# implementing horizontal bar graph
ax7 = fig.add_subplot(grid[6:9, 13:])

clr = ['red', 'orange', 'yellow', 'green', 'blue', 'skyblue', 'violet']
# assigning the bar graph to a variable container
container = plt.barh(vegetables_area['State Name'][0:7], vegetables_area['VEGETABLES AREA (1000 ha)'][0:7], color=clr)

# takes container as an input and prints the exact count on the edge of the bar
ax7.bar_label(container, label_type='center')
ax7.set_title('States with the highest Vegetable Area in India: 1978 - 2018')
ax7.set_xlabel('VEGETABLES AREA (1000 ha)')
ax7.set_ylabel('State Names')
ax7.legend()
ax7.grid()
ax7.legend(bbox_to_anchor=(0.9999, 1), loc='upper left', borderaxespad=0,
           title='Crop type')

# explanation for the horizontal bar graph
ax8 = fig.add_subplot(grid[11:15, 13:])
text = '''
The above horizontal bar graph depicts the 
top 7 states over Vegetable Area (1000 ha).

We can observe that the graph shows a 
downward trend from bottom to top.
It is noticeable that Orissa 
recorded with the highest area.
However, Tamil Nadu with the least vegetable area.
'''

ax8.text(0.5, 0, text, fontsize=13, ha='center')
ax8.axis('off')

# saving the image with 300dpi
plt.savefig('22031006.png', bbox_inches='tight', dpi=300)
