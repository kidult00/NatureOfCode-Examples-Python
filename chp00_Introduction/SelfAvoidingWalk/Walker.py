# Python Version of The Nature of Code
# [kidult00](https://github.com/kidult00)

# A random walker class!

class Walker(object):
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.grid = [([False] * width) for i in range(height+1)]
    
    def render(self):
        stroke(0)
        point(self.x, self.y)
    
    # Randomly move up, down, left, right, or stay in one place
    def step(self):
        ok = False
        helpme = 0
        
        while(not ok):
            choice = int(random(4))
            saveX = int(self.x)
            saveY = int(self.y)
            
            if choice == 0:
                self.x += 1
            elif choice == 1:
                self.x -= 1
            elif choice == 2:
                self.y += 1
            else:
                self.y -= 1

            self.x = constrain(self.x, 0, width-1)
            self.y = constrain(self.y, 0, height-1)
            
            if self.grid[self.x][self.y] == False:
                ok = True
                self.grid[self.x][self.y] = True
            else:
                self.x = saveX
                self.y = saveY
                
            helpme += 1
            
            if helpme > 1000:
                print('STUCK')
                noLoop()
                ok = True
        
        