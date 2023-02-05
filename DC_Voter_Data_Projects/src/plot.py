import json
import matplotlib.pyplot as plt
import pandas as pd
import math
from descartes import PolygonPatch
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

RESULTS_DIRECTORY='../results/'
DATA_DIRECTORY='../data/'
SMD_GEOJSON_2023 = f'{DATA_DIRECTORY}2023_SMDs.geojson'
GRAPH_TITLE = '2022 General Election Turnout by SMD'
SMD_TURNOUT = f'{RESULTS_DIRECTORY}SMD_turnout.csv'

with open(SMD_GEOJSON_2023) as f:
    data = json.load(f)

smd_turnout_df = pd.read_csv(SMD_TURNOUT)

# Calculate the lowest and highest turnout SMDs. Round the number to the nearest five (ceiling for lowest and floor for highest)
# to make difference more obvious
lowest_turnout = smd_turnout_df['votes_2022'].min()
lowest_turnout_round_to_5 = round(math.ceil(lowest_turnout/5))*5-5
highest_turnout = smd_turnout_df['votes_2022'].max()
highest_turnout_round_to_5 = round(math.floor(highest_turnout/5))*5

# create a dictionary to map the "SMD_ID" to the second column value
color_values = {row[0]:row[1] for row in smd_turnout_df.values}

# create the plots
fig, ax = plt.subplots()
fig.set_size_inches(10,10)

# Draw all features and fill in the colors
for feature in data['features']:
    smd_id = feature['properties']['SMD_ID']
    color_value = color_values.get(smd_id, 0) # setting a default value for the cases when not found.
    color = plt.cm.RdYlGn((color_value-lowest_turnout_round_to_5)/(highest_turnout_round_to_5-lowest_turnout_round_to_5)) # You can use any colormap from matplotlib
    ax.add_patch(PolygonPatch(feature['geometry'], fc=color, ec='#6699cc', alpha=0.5))

# add the color scale
norm = Normalize(vmin=lowest_turnout_round_to_5, vmax=highest_turnout_round_to_5)
sm = ScalarMappable(norm=norm, cmap='RdYlGn')
sm.set_clim(lowest_turnout_round_to_5,highest_turnout_round_to_5)
sm.set_array([])

# Set ticks for color scale
cbar = plt.colorbar(sm, ax=ax, orientation='vertical')

def get_tick_array(min_val,max_val):
    tick_array=[min_val]
    for tick_counter in range(1,5):
        tick_array.append(int(tick_counter*(max_val-min_val)/5.0+min_val))
    tick_array.append(max_val)
    return tick_array

tick_array = get_tick_array(lowest_turnout_round_to_5,highest_turnout_round_to_5)
cbar.set_ticks(tick_array)
cbar.set_ticklabels(tick_array)

#cbar.ax.set_yticklabels()
cbar.ax.set_position((0.2,0.25,0.2,0.25))

title = ax.set_title(GRAPH_TITLE, fontsize=14, fontweight='bold',x=0.68,y=0.5)
title.set_rotation(-38)
ax.axis('scaled')
ax.set_frame_on(False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

plt.savefig(f'{RESULTS_DIRECTORY}{GRAPH_TITLE}.png')