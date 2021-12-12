from tkinter import*
from tkinter.messagebox import*
import random
import os
import time

class Auto(Frame):
    def __init__ (self, root):

        root.title('Memory Game')
        root.geometry('1000x700')
        super().__init__(root)
        self.rows = 3
        self.cols = 4
        self.image_path = ""
        self.grid(rows= self.rows, columns=self.cols, padx=0, pady=0)
        self.images = ['Ferrari.png', 'Mercedes.png', 'Bugatti.png', 'Dodge.png', 'Pagani.png', 'Herbie.png'] * 2
        random.shuffle(self.images)
        print(self.images)
        # same dimension as self.images
        self.selected_images = []
        self.configure(bg='blue')
        self.images_clicked = []
        self.buttons = []
        self.first_choice = []
        self.already_guessed = []
        self.slike = []
        self.fron_picture = []
        self_open = 0
        self.return_front = []
        
        self.gui()

    def gui(self):
        f = ('Times new roman', 15, 'italic')

        for i, img in enumerate(self.images):
            # load img
            img_abs_path = os.path.join(self.image_path, img)
            slika = PhotoImage(file=img_abs_path)
            self.slike.append(slika)
            self.front = PhotoImage(file = "front.png")

            row = i // self.cols * 2
            col = i % self.cols

            # create img

            btn = Button(self, image = self.front, width=200, height=200, command = lambda img=img, i=i : self.click(img, i))

            self.buttons.append(btn)
            btn.image = self.front

            btn.grid(row=row, column=col)

        self.num_correct_values = StringVar()
        self.num_correct_values.set(0)
        self.R = Label(self, textvariable = self.num_correct_values)
        self.R.grid(row = 9, column = 5)
        return

    def click(self, img, i):
        self.buttons[i].config(image = self.slike[i])

        if img in self.already_guessed:
            return

        elif self.first_choice == []:
            self.first_choice = [i, img]
            print(self.return_front)

            if (self.return_front):
                print(self.return_front[1])
                print(i)
                
                if (self.return_front[1] == i):
                    self.buttons[int(self.return_front[0])].config(image = self.front)

                else:
                    self.buttons[int(self.return_front[0])].config(image = self.front)
                    self.buttons[int(self.return_front[1])].config(image = self.front)
                
            
        elif (i != self.first_choice[0]) & (img == self.first_choice[1]):
            print("Par pronadjen")
            self.already_guessed.append(self.first_choice[1])
            print(self.already_guessed)
            self.first_choice = []
            self.return_front = []
            
        else:
            self.return_front = [self.first_choice[0], i]
            self.first_choice = []


def main():
    p = Auto(Tk())
    mainloop()


if __name__ == "__main__":
    main()
