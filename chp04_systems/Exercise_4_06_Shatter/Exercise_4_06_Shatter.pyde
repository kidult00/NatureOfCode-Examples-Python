# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from ParticleSystem import ParticleSystem

def setup():
    size(640, 360)
    global ps
    ps = ParticleSystem(100.0, 100.0, 5.0)

def draw():
    background(255)

    ps.display()
    ps.update()


def mousePressed():
    ps.shatter()