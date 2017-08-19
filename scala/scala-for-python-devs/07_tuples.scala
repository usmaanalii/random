// Tuples
// Good way of destrucuring vals/vars
val foo = (1, 2.5, "three")

// Accessors are named by position
foo._1
foo._2

// Destructurint
val (a, b, c) = foo

val bar = (4, 5.5, "six")

// zip function
val pairs = Array(1, 2, 3).zip(Array("four", "five", "six"))

for ((k, v) <- pairs) yield k.toString + v

