# Python Version of The Nature of Code
# [kidult00](https://github.com/kidult00)

# "Landscape" example

class Landscape(object):
    def __init__(self, scl_, w_, h_):
        self.scl = scl_   # size of each cell: 20
        self.w = w_       # width of thingie: 800
        self.h = h_       # height of thingie: 400
        self.cols = self.w / self.scl    # number of columns: 40
        self.rows = self.h / self.scl    # number of rows: 20
        self.z = [([0.0] * self.rows) for i in range(self.cols)]   
        # Don't forget [] , otherwise z is not a list but a float
        self.zoff = 0.0
        print("len of z:{}, len of z[0]:{}".format(len(self.z),len(self.z[0])))
        
    # Calculate height values (based off a neural netork)
    def calculate(self):
        xoff = 0.0
        for row in range(self.rows): #~20
            # print("{}th cols of {}".format(col,self.cols))
            yoff = 0.0
            for col in range(self.cols): # ~40
                self.z[col][row] = map(noise(xoff, yoff, self.zoff), 0, 1, -120, 120)
                # print(i,j,self.z[j][i])
                yoff += 0.1
            xoff += 0.01
        self.zoff += 0.01
        
    # Render landscape as grid of quads
    def render(self):
    # Every cell is an individual quad
    # (could use quad_strip here, but produces funny results, investigate this)
        for x in range(len(self.z)-1):
            for y in range(len(self.z[x])-1): 
                # one quad at a time
                # each quad's color is determined by the height value at each vertex
                # (clean this part up)
                stroke(0)
                fill(100, 100)
                pushMatrix()
                beginShape(QUADS)
                translate(x * self.scl - self.w/2, y * self.scl - self.h/2, 0)
                vertex(0, 0, self.z[x][y])
                vertex(self.scl, 0, self.z[x+1][y+1])
                vertex(self.scl, self.scl, self.z[x+1][y+1])
                vertex(0, self.scl, self.z[x][y+1])
                endShape()
                popMatrix()