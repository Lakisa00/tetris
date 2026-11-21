import tkinter as tk

COLS = 10
ROWS = 20
CELL = 28
BACKGROUND = "#131b2e"
GRID = "#26334d"
SQUARE = [(0,0), (1,0), (0,1), (1,1)]

class Game:
    def __init__(self, root):
        self.root = root
        root.title("Tetris")
        self.canvas = tk.Canvas(
            root, width= COLS*CELL, height=ROWS*CELL, bg=BACKGROUND, highlightthickness=0
        )
        self.canvas.pack(padx=12,pady=12)
        self.piece = SQUARE.copy()
        self.x = COLS//2-1
        self.y = 0
        self.color = "#facc15"
        self.draw()
        
    def draw(self):
        self.canvas.delete("all")
        for y in range(ROWS):
            for x in range(COLS):
                self.draw_cell(x,y,BACKGROUND)
        for dx, dy in self.piece:
            self.draw_cell(self.x + dx, self.y + dy, self.color)
                
    def draw_cell(self,x,y,color):
        self.canvas.create_rectangle(
            x*CELL, y*CELL, (x+1)*CELL, (y+1)*CELL,
            fill=color, outline=GRID
        )
    
    
    
if __name__ == "__main__":
    window = tk.Tk()
    Game(window)
    window.mainloop()