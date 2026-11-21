import tkinter as tk

COLS = 10
ROWS = 20
CELL = 28
FALL_MS = 500
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
        root.bind("<KeyPress>", self.on_key)
        self.draw()
        self.root.after(FALL_MS, self.tick)
        
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
    def can_place(self, piece, x, y):
        for dx, dy in piece:
            board_x, board_y = x+dx, y+dy
            if not (0<=board_x<COLS and 0<=board_y<ROWS):
                return False
        return True    
    
    def move(self, dx, dy):
        if not self.can_place(self.piece, self.x+dx, self.y+dy):
            return False
        self.x+=dx
        self.y+=dy
        self.draw()
        return True
    
    def on_key(self, event):
        key = event.keysym.lower()
        if key in ("left","a"):
            self.move(-1,0)
        elif key in ("right", "d"):
            self.move(1,0)
        elif key in ("down", "s"):
            self.move(0,1)
    
    def tick(self):
        self.move(0,1)
        self.root.after(FALL_MS, self.tick)
    
    

if __name__ == "__main__":
    window = tk.Tk()
    Game(window)
    window.mainloop()