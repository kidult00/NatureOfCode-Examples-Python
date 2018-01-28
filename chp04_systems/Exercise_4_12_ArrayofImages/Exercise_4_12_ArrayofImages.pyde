# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Array of Images for particle textures

from ParticleSystem import ParticleSystem

def setup():
    size(640, 360, P2D)
    
    global imgs, ps
    
    imgs = [None] * 5
    imgs[0] = loadImage("corona.png")
    imgs[1] = loadImage("emitter.png")
    imgs[2] = loadImage("particle.png")
    imgs[3] = loadImage("texture.png")
    imgs[4] = loadImage("reflection.png")
    
    ps = ParticleSystem(imgs)

def draw():
    background(0)
    blendMode(ADD)

    up = PVector(0, -0.2)
    ps.applyForce(up)
    ps.run()
    for i in range(5):
        ps.addParticle(mouseX, mouseY)