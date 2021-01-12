import numpy as np
import matplotlib.pyplot as plt
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color

# tools to build a 2D L*a*b* color space in matplotlib over which the user can plot new L*a*b* data for rapid visualization


def lab2rgb(lab):
    _observer_angle = '2'
    _illuminant = 'd65'

    lab_color = LabColor(lab[0], lab[1], lab[2], _observer_angle, _illuminant)
    rgb_color = convert_color(lab_color, sRGBColor)
    rgb_tuple = rgb_color.get_value_tuple()

    # L*a*b* (CIELAB) colour space can express a much wider colour gamut compared to the RGB colour space
    # therefore, in some instances, the RGB values resulting from the lab2rgb conversion will exceed the \
    # model's limit, and need to be manually clipped
    rgb_vals = np.array(rgb_tuple)
    if (rgb_vals > 1).any():
        over_limit = np.argwhere(rgb_vals > 1)
        for i in over_limit: 
            rgb_vals[i] = 1.0
    
    #returns normalized rgb values between [0,1]
    return rgb_vals


def unormalize_rgb(rgb):
    return rgb * 255.


def format_plot(axes, lightness):
    ticker_min_val = -120
    ticker_max_val = 120
    num_ticks = 20
    
    data_max_val = 127
    data_min_val = -128

    #moves the x and y axes to the center of the plot
    axes.spines['top'].set_visible(False)
    axes.spines['right'].set_visible(False)
    axes.spines['left'].set_position('center')
    axes.spines['bottom'].set_position('center')

    #sets length of axis lines
    axes.spines['bottom'].set_bounds(data_min_val, data_max_val)
    axes.spines['left'].set_bounds(data_min_val, data_max_val)

    #sets ticker parameters
    axes.xaxis.set_ticks_position('bottom')
    axes.yaxis.set_ticks_position('left')
    axes.tick_params(axis='both', which='major', labelsize=8)
    axes.xaxis.set_ticks(np.arange(ticker_min_val, ticker_max_val + 1, num_ticks))
    axes.yaxis.set_ticks(np.arange(ticker_min_val, ticker_max_val + 1, num_ticks))

    #origin ticker position
    zero = 6 
    # removes 0 ticker labels
    plt.setp(axes.get_xticklabels()[zero], visible=False)
    plt.setp(axes.get_yticklabels()[zero], visible=False)
    # removes 0 ticker ticks
    plt.setp(axes.xaxis.get_major_ticks()[zero], visible=False)
    plt.setp(axes.yaxis.get_major_ticks()[zero], visible=False)

    # set axes labels
    axes.set_xlabel('Blue \n $-b^*$', labelpad= 115)
    axes.xaxis.set_label_coords(0.5, 0) #coordinates are between [-1,1]

    axes.set_ylabel('Green \n $-a^*$', rotation=0)
    axes.yaxis.set_label_coords(-0.01, 0.45) #coordinates are between [-1,1]

    axes.text(-12, 140, 'Yellow \n $+b^*$')
    axes.text(132, -12, 'Red \n $+a^*$')
    axes.text(145, 70, 'Lightness* = ' + str(lightness))

    
def plot_2D_lab_colorspace(fig, num_points, lightness):
    points = np.linspace(-128, 127, num_points)
    a = points
    b = points

    ax = fig.gca()

    for x in a:
        color_array = []
        for y in b:
            rgb_vals = lab2rgb([lightness, x, y])
            color_array.append(rgb_vals)                
        ax.scatter(x * np.ones(len(points)), b, c=color_array, cmap='rgb', s=20)
    
    format_plot(ax, lightness)
    
    return ax


if __name__ == "__main__":
    
    #Test Data
    data_values = [[50, -85, -40], [45, -30, 40], [70, 25, 20], [50, 60, 100]]
    data_labels = ['Platinum Plating', 'Paladium Plating', 'Silver Plating', 'Bronze Plating' ]
    marker_shapes = ['o', 'v', 's']

    fig = plt.figure()
    ax = plot_2D_lab_colorspace(fig, 256, 75)

    for data, labels, marker in zip(data_values, data_labels, marker_shapes):
        ax = plt.scatter(data[1], data[2], marker= marker, facecolors='none', edgecolors='black', label= labels)

    plt.legend(loc='lower left', bbox_to_anchor=(1, 0.8))
    

    fig.tight_layout()
    plt.show()

