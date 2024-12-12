import turtle
import math

class Planet:
    def __init__(self, name, mass, size, x_pos, y_pos, x_vel, y_vel, color="blue"):
        self.name = name
        self.mass = mass
        self.size = size
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color

    def move(self, dt, sun):

        dx = sun.x_pos - self.x_pos
        dy = sun.y_pos - self.y_pos
        distance = math.sqrt(dx**2 + dy**2)


        gravitational_constant = 1
        force = gravitational_constant * sun.mass / (distance**2)
        acc_x = force * dx / distance
        acc_y = force * dy / distance


        self.x_vel += acc_x * dt
        self.y_vel += acc_y * dt


        self.x_pos += self.x_vel * dt
        self.y_pos += self.y_vel * dt


class Sun:
    def __init__(self, name, mass, size, x_pos, y_pos):
        self.name = name
        self.mass = mass
        self.size = size
        self.x_pos = x_pos
        self.y_pos = y_pos


class SolarSystem:
    def __init__(self):
        self.planets = []
        self.sun = None

    def add_sun(self, sun):
        self.sun = sun

    def add_planet(self, planet):
        self.planets.append(planet)

    def move_planets(self, dt):
        for planet in self.planets:
            planet.move(dt, self.sun)



class SolarSystemVisualizer:
    def __init__(self, solar_system, width=800, height=800, scale=100):
        self.solar_system = solar_system
        self.scale = scale
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.bgcolor("black")
        self.bodies = {}

    def setup(self):

        sun = turtle.Turtle()
        sun.shape("circle")
        sun.color("yellow")
        sun.penup()
        sun.goto(self.solar_system.sun.x_pos * self.scale, self.solar_system.sun.y_pos * self.scale)
        sun.shapesize(self.solar_system.sun.size)  # Larger sun
        self.bodies["sun"] = sun


        for planet in self.solar_system.planets:
            planet_turtle = turtle.Turtle()
            planet_turtle.shape("circle")
            planet_turtle.color(planet.color)
            planet_turtle.penup()
            planet_turtle.goto(planet.x_pos * self.scale, planet.y_pos * self.scale)
            planet_turtle.shapesize(planet.size)
            self.bodies[planet.name] = planet_turtle

    def update(self):
        for planet in self.solar_system.planets:
            planet_turtle = self.bodies[planet.name]
            planet_turtle.goto(planet.x_pos * self.scale, planet.y_pos * self.scale)


class Simulation:
    def __init__(self, solar_system, duration, step_size):
        self.solar_system = solar_system
        self.duration = duration
        self.step_size = step_size
        self.visualizer = SolarSystemVisualizer(solar_system)

    def run(self):
        self.visualizer.setup()
        time = 0
        while time < self.duration:
            self.solar_system.move_planets(self.step_size)
            self.visualizer.update()
            time += self.step_size



if __name__ == "__main__":

    solar_system = SolarSystem()

    the_sun = Sun("Sun", mass=1000, size=3, x_pos=0, y_pos=0)
    solar_system.add_sun(the_sun)

    earth = Planet(
        "Earth",
        mass=1,
        size=1.5,
        x_pos=2,
        y_pos=0,
        x_vel=0,
        y_vel=math.sqrt(1 * the_sun.mass / 2),
        color="blue",
    )
    mars = Planet(
        "Mars",
        mass=0.1,
        size=1.2,
        x_pos=3,
        y_pos=0,
        x_vel=0,
        y_vel=math.sqrt(1 * the_sun.mass / 3),
        color="red",
    )
    solar_system.add_planet(earth)
    solar_system.add_planet(mars)

    simulation = Simulation(solar_system, duration=100, step_size=0.01)
    simulation.run()





