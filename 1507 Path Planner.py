import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import matplotlib.image as mpimg

def main():
    # Load image
    image_path = input("Enter the path to the image: ")
    img = mpimg.imread(image_path)

    # Display image
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.gca().invert_yaxis()  # Invert y-axis to match image coordinates

    # Set up cursor
    cursor = Cursor(ax, useblit=True, color='red', linewidth=1)

    # Set the pixel scale factor (1 inch corresponds to 224 pixels)
    pixel_scale_factor = 1 / 224

    # Set the inches scale factor (0.75 inches corresponds to 57 inches in reality)
    inches_scale_factor = 57 / 0.75

    # Calculate the actual scale factor
    actual_scale_factor = 195 / 367  # Adjusted 

    # Initialize variables
    origin = None
    prev_point = None

    def onclick(event):
        nonlocal origin, prev_point
        
        x = event.xdata
        y = event.ydata

        if origin is None:
            # First point clicked is considered the origin
            origin = (x, y)
            prev_point = origin
            plt.plot(x, y, 'bo', markersize=5)  # Plot the origin point
        else:
            # Plot line from previous point to current point
            plt.plot([prev_point[0], x], [prev_point[1], y], color='blue')
            prev_point = (x, y)

        # Convert pixel coordinates to inches relative to the origin
        inches_y_pixel = (x - origin[0]) * pixel_scale_factor
        inches_x_pixel = (y - origin[1]) * pixel_scale_factor  # Swap x and y

        # Convert inches relative to the origin to inches based on the new scale factor
        inches_x = inches_x_pixel * inches_scale_factor * actual_scale_factor
        inches_y = inches_y_pixel * inches_scale_factor * actual_scale_factor

        # Flip the sign of inches_x if it's positive
        inches_x = -inches_x if inches_x > 0 else inches_x

        print(f"Inches from origin: ({inches_x:.2f}, {inches_y:.2f}) inches")

        plt.draw()

    # Connect click event to function
    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    plt.show()

if __name__ == "__main__":
    main()
