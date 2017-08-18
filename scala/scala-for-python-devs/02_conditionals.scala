// Conditional Expressions

val x = 0

// Inline: variable assignment expression
val foo = if (x > 0) 1 else -1

var baz = 1

// REPL paste mode use :paste to enter and ^D to exit

// keep simple expressions to one line
if (x == 0) baz = 6
baz

if (foo.isInstanceOf[String]) {
    print("Foo is a string!")
} else if (foo.isInstanceOf[Int]) {
    print("Foo is an int!")
} else {
    print("I dont know what foo is")
}

// Handle above with comprehensions
var n = 0

// ArrayBuffer is a mutable array that acts like Python lists
import scala.collection.mutable.ArrayBuffer

var nlist = ArrayBuffer[Int]()

while (n < 5) {
    nlist += n
    n += 1
}

nlist

// Scala supports a for (variable <- expression) syntax
val foo = "Apple"
var n = 0

for (x <- foo) {
    n += 1
}

n

// Better expressed in a single line
n = 0
for (x <- foo) n += 1
n

// Python supports comprehensions with the yield syntax
for (f <- Array(1, 2, 3, 4, 5)) yield f + 1

// Using multiple generators to replicate the python zip
val foo = Array(1, 2, 3)
val bar = Array("a", "b", "c")

import scala.collection.mutable.Map

// Specify types
var foobars = Map[String, Int]()

for (f <- foo; b <- bar) foobars += (b -> f)
foobars

// We're not limited to two iterables
val baz = Array("apple", "orange", "banana")
val mapped = Map[String, (Int, String)]()

for (f <- foo; b <- bar; z <- baz) mapped += (z -> (f, b))
mapped

// Scala also has an implicit zip method
val arr1 = Array(1, 2, 3)
val arr2 = Array(4, 5, 6)

arr1.zip(arr2)

// zipWithIndex is like enumerate
for ((y, x) <- Array("foo", "bar", "baz").zipWithIndex) yield (x, y)

// Simply calling zipWithIndex will return the same but in reversed order
Array("foo", "bar", "baz").zipWithIndex

// Expression "guards", similar to control flow expressions
val foo = Array(1, 2, 3, 4, 5, 6)
var bar = ArrayBuffer[Int]()

for (f <- foo if f != 3) bar += f
bar

// Stack guards
for (x <- (1 to 5).toArray if x != 2 if x != 3) yield x

// Using map instead of a for-comprehension
for (c <- Array(1, 2, 3)) yield c + 2
Array(1, 2, 3).map(_ + 2)