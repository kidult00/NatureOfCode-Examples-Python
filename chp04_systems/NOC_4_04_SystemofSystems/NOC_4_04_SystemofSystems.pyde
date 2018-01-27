# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Particles are generated each cycle through draw(),
# fall with gravity and fade out over time
# A ParticleSystem object manages a variable size (ArrayList) list of particles.

from ParticleSystem import ParticleSystem

def setup():
    size(640, 360)
    global systems
    systems = []

def draw():
    background(255)
    for each in systems:
        each.run()
        each.addParticle()

    fill(0)
    text("click mouse to add particle systems", 10, height - 30)

def mousePressed():
    systems.append(ParticleSystem(1, PVector(mouseX, mouseY)))