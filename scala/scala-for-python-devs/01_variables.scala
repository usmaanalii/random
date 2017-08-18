// Variables

val foo = "Apples"

val baz = foo + " and Oranges"
baz

// In Scala, vals are immutable
baz = "Only Grapes" // error: reassignment to val

// Create a var instead
var baz = "Apples and Oranges"

var one = 1
one += 1
one

// Scala also allows you to stronly type your variables, rather than lerring
// the compiler interpret the type
val foo: String = "Apples"

// Unpack rather than perform multple assignments ???
val foo, bar = Array(1, 2, 3)

// foo and bar reference a different piece of memory, changing one will not
// change the other
bar(0) = 4
bar // (4, 2, 3)
foo // (1, 2, 3)

// Scala uses the actual operator symbol rather than an alphanumeric character
val foo = 1
foo + 1

// behind the scenes
foo +(1)
