# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from ParticleSystem import ParticleSystem

def setup():
    size(640, 360)
    global ps
    ps = ParticleSystem(PVector(width / 2, 50))

def draw():
    background(255)

    # Option #1 (move the Particle System origin)
    ps.origin.set(mouseX, mouseY)
    ps.addParticle()
    ps.run()

    # Option #2 (move the Particle System origin)
    # ps.addParticle(mouseX, mouseY)
