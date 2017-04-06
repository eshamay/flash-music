import sys

import Tkinter as tk
import mingus.extra.lilypond as LP

from PIL import Image, ImageTk

from Composer import Composer


class Canvas:
    def __init__(self, interval_millis):
        self.interval = interval_millis
        self.composer = Composer()

        self.root = tk.Tk()
        self.root.title('Some Title')

        self.image_path = "composer.png"

        self.display = tk.Canvas(bd=0, highlightthickness=0)
        self.display.grid(row=0, sticky=tk.W + tk.E + tk.N + tk.S)
        self.display.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        self.image = None

        self.root.after(1, self.new_image)
        self.root.mainloop()

    def get_image(self, path):
        image = Image.open(path)
        size = (image.width*2, image.height*2)
        resized = image.resize(size, Image.ANTIALIAS)

        return ImageTk.PhotoImage(resized)

    def update_image(self):
        self.image = self.get_image(self.image_path)

        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=tk.NW, tags="IMG")
        self.display.config(width=self.image.width(), height=self.image.height())

        self.root.after(self.interval, self.new_image)

    def new_image(self):
        composition = self.composer.compose(None)
        lily_string = LP.from_Composition(composition)
        print lily_string
        LP.to_png(lily_string, self.image_path)

        self.update_image()


def main():
    Canvas(sys.argv[1])


if __name__ == '__main__':
    main()
