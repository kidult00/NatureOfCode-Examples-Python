# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Smoke Particle System

# This example demonstrates a "glow" like effect using
# additive blending with a Particle system.  By playing
# with colors, textures, etc. you can achieve a variety of looks.

from ParticleSystem import ParticleSystem

def setup():
    size(640, 360, P2D)
    global ps, img
    img = loadImage("texture.png") # Create an alpha masked image to be applied as the particle's texture
    ps = ParticleSystem(PVector(width / 2, 50), img)

def draw():
    blendMode(ADD) # Additive blending!
    background(0)

    ps.run()
    for i in range(10): ps.addParticle()