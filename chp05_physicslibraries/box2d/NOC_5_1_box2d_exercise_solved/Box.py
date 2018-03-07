# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

add_library('box2d_processing')
# import pybox2d

class Box(object):
    """A rectangular box"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16
        
        self.bd = box2d.BodyDef()
        self.bd.type = BodyType.DYNAMIC
        self.bd.position.set(box2d.coordPixelsToWorld(x, y))
        self.body = box2d.createBody(bd)
        
        self.ps = PolygonShape()
        self.box2dW = box2d.scalarPixelsToWorld(self.w/2)
        self.box2dH = box2d.scalarPixelsToWorld(self.h/2)
        self.ps.setAsBox(self.box2dW, self.box2dH)
        
        self.fd = FixtureDef()
        self.fd.shape = self.ps
        
        self.fd.density = 1
        self.fd.friction = 0.3
        self.fd.restitution = 0.5
        
        self.body.createFixture(self.fd)
        
    def display(self):
        pos = box2d.getBodyPixelCoord(self.body)
        a = self.body.getAngle()
        
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(-a)
        fill(127)
        stroke(0)
        strokeWeight(2)
        rectMode(CENTER)
        rect(0, 0, self.w, self.h)
        popMatrix()