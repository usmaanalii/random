// Classes
// Simple classes, but requires further investigation

// Use var to make attributes mutable
// Behind the scenes, Scala is creating getters and setters for each
class Automobile(var wheels: Int = 4, var engine: Int = 1, var lights: Int = 2) {
    
    def total_parts() = {
        // No "self" needed, and implicit return
        wheels + engine + lights
    }
    
    // Purely side-effecting function, no "=" needed
    def remove_wheels(count: Int) {
        if (wheels - count < 0) {
            throw new IllegalArgumentException("Automobile cannot have fewer than 0 wheels!")
        } else {
            wheels = wheels - count
            println(s"Auto now has $wheels wheels!")
        }
        
    }
}

val car = new Automobile()

car.wheels
car.total_parts()
car.wheels = 6
car.total_parts()
car.remove_wheels(7) // Raises Exception
car.remove_wheels(2) // Not interpolating

// If you define a constutor field as val, you get a getter not a setter
class Automobile(val wheels: Int = 4){}

val car = new Automobile()

car.wheels = 5 // error

// Using private prevents getters/setters from being generated
// allowing access only within the class, in python _ is used as a convention
// for this
class Automobile(private val wheels: Int = 4){}

val car = new Automobile()

car.wheels // cannot access error

// Static methods are handled via "companion objects", named the same of
// the clss itself
class Automobile(var name: String){}

object Automobile {
    var wheels = 4
    var lights = 2
    def print_uninst_str() = "No 'self' passed to this method, and no instantiation. It's static!"
}

Automobile.print_uninst_str
Automobile.wheels

Automobile.wheels = 5
Automobile.wheels

// Light introduction to inheritance
// Scala supports single inheritance via abstrace base classes
abstract class Automobile(val color: String, val make: String) {
    val wheels: Int = 4
    val lights: Int = 2
    val doors: Int = 4
    
    def towing_capacity: Int
    def top_speed: Int
    def print_make_color(): String = return s"$color $make"
}

class Car(color: String, make: String) extends Automobile(color, make) {
    
    override val doors = 4 // Override needed if immutable "val"
    
    def towing_capacity() = 0
    def top_speed() = 150
}

val myCar = new Car("Red", "Toyota")

myCar.print_make_color()
myCar.doors
myCar.top_speed

// Abstract classes only support single inheritance
abstract class SportPackage {}

class Car(color: String, make: String) extends Automobile(color, make) with SportPackage(){} // Error

// Only use ABC's in Scala if you need Java interop or need to pass
// constructor params to the base class, otherwise use "Traits"
// Traits act like mizins and enable multiple inheritance
trait Engine {
    var started: Boolean = false
    
    // These don't return anything, so no "=" needed
    def start() {started = true}
    def shutdown() {started = false}
}

trait Transmission {
    var fluid_level: Int = 0
    def add_fluid(amount: Int) {fluid_level = fluid_level + amount}
}

class Car(color: String, make: String) extends Automobile(color, make) with Engine with Transmission {
    
    override val doors = 4 // Override needed for immutable "val"
    
    def towing_capacity() = 0
    def top_speed = 150
}

val mycar = new Car("Red", "Toyota")

mycar.start()
mycar.started

mycar.add_fluid(50)

mycar.fluid_level
