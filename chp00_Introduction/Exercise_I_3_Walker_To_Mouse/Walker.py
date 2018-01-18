# Python Version of The Nature of Code
# [kidult00](https://github.com/kidult00)

# A random walker class!

class Walker(object):
    def __init__(self):
        self.x = width/2
        self.y = height/2    
    
    def render(self):
        stroke(0)
        strokeWeight(2)
        point(self.x, self.y)
    
    # Randomly move up, down, left, right, or stay in one place
    def step(self):
        
        r = random(1)
        # A 50% of moving towards the mouse
        if r < 0.5 : # r as "noise"
            xdir = mouseX - self.x
            ydir = mouseY - self.y
            if xdir != 0 :
                xdir /= abs(xdir) # turn xdir to 1 or -1
            if ydir != 0:
                ydir /= abs(ydir)
            self.x += xdir
            self.y += ydir
        else:
            xdir = int(random(-2,2)) # -1,0,1
            ydir = int(random(-2,2))
            print(xdir,ydir)
            self.x += xdir
            self.y += ydir

        # Stay on the screen
        self.x = constrain(self.x, 0, width-1)
        self.y = constrain(self.y, 0, height-1)