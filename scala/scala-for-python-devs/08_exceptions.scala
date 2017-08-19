// Exceptions
// Similar to Python

def is_apple(fruit: String) = {
    if (fruit != "apple") throw new IllegalArgumentException("Fruit is not apple!")
}

is_apple("orange")

// try/catch/finally
import java.io.IOException

def check_fruit(fruit: String) {
    try {
        is_apple(fruit)
        print("No exception raised...")
    } catch {
        case ex: IllegalArgumentException => print(ex)
        case _: IOException => print("Oh no! IOException")
    } finally {
        print("This will execute regardless of case")
    }
}

check_fruit("apple")
check_fruit("oranges")
