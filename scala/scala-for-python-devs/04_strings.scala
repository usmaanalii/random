// Strings
val foo = "bar"

foo(1)
foo.length
foo + 1.toString
foo.split("a")
"fooo   ".trim
"String here: %s, Int here: %d".format("foo", 1)

// Mapping over strings
foo.map(_.toUpper)

// String interpolation
val fruit = "apple"
val apple_count = 5
val veg = "broccoli"
val broc_count = 10

s"I have $apple_count $fruit and $broc_count $veg. In total I have ${apple_count + broc_count} fruit and veg"

// Iterating over individual characters in a String
for (c <- foo) println(c)

// Multiline strings
"""
This is
a multiline string
"""

