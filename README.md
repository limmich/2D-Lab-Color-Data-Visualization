# 2D-Lab-Color-Data-Visualization

### Purpose: 
Easily and aesthetically plot and visualize L\*a\*b\* data acquired through spectrophotometer/colorimeter measurements. Specifically building the L\*a\*b\* color gamut background using matplotlib for re-use when visualizing new L\*a\*b\* data.

### Motivation:
Within the consumer electronics industry, during the product development cycle the cosmetic appearance of materials plays a large role in the material selection process. L\*a\*b\* measurements are often acquired to quantitatively characterize the cosmetic appearance of the material. Plotting these values provides the intuitive capability of comparing materials’ color

### Background:
L\*a\*b\*, also referred to as CIELAB, is a color space, or “color model”, used to quantitatively express color, similar to the RGB or CMYK systems. The difference, however, is L\*a\*b\* can display a much wider range of colors, more closely approximating the human perception of color.  L\* tracks perceptual lightness (black to white), a\* varies from green to red, and b* varies from blue to yellow. Color can often be reduced to a* and b* values since these describe hue.

### Method:
With Matplotlib’s pyplot  library, a 2D L\*a\*b\* color space representation is built by using X, Y coordinates as ‘a*’ and ‘b*’ values to express color in L\*a\*b\* space. Since Matplotlib is capable only of displaying color expressed using the RGB system, the L\*a\*b\* color is converted to RGB using the colormath library prior to plotting. Once the L\*a\*b\* color space is built, the user’s new L\*a\*b\* data can then be plotted using common Matplotlib tools.

![alt text](https://github.com/limmich/2D-Lab-Color-Data-Visualization/blob/main/LAB_Plot.png?raw=true)
