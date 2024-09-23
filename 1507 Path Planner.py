import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import math

# Function to calculate distance between two points
def calculate_distance(x0, y0, x1, y1):
    return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

class ImageDistanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Distance Calculator")

        self.canvas = tk.Canvas(root, width=7680, height=3320)
        self.canvas.pack()

        self.load_image_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_image_button.pack()

        self.reference_points = []
        self.canvas.bind("<Button-1>", self.set_point)
        
    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.image.thumbnail((7680, 3320))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def set_point(self, event):
        if not self.reference_points:
            self.reference_points.append((event.x, event.y))
            self.canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill='red')
            self.canvas.create_text(event.x, event.y - 10, text="(0,0)", fill="red")
        else:
            prev_x, prev_y = self.reference_points[-1]
            distance = calculate_distance(prev_x, prev_y, event.x, event.y)
            self.canvas.create_line(prev_x, prev_y, event.x, event.y, fill="blue")
            self.canvas.create_text(event.x, event.y, text=f"{distance:.2f}", fill="blue")
            self.reference_points.append((event.x, event.y))

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDistanceApp(root)
    root.mainloop()
