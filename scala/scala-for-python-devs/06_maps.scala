// Maps

// Scala comes with both mutable and immutable map types, as opposed
// to Pythons Dict
val imm_fruit_count = Map("apples" -> 4, "oranges" -> 5, "bananas" -> 6)

imm_fruit_count("apples")

imm_fruit_count.contains("apples")

imm_fruit_count.getOrElse("melons", "peaches") // Any = peaches

val mut_fruit_count = scala.collection.mutable.Map[String, Int]()

mut_fruit_count("apples") = 4

mut_fruit_count += ("oranges" -> 5, "bananas" -> 6)
mut_fruit_count

mut_fruit_count -= "apples"

mut_fruit_count.keySet
mut_fruit_count.values

// Nice feature of Scala Maps: provides a default value if not specified
val defaultMap = Map("foo" -> 1, "bar" -> 2).withDefaultValue(3)
defaultMap("qux")

// Iterating over maps
val foo = ArrayBuffer[String]()

for ((k, v) <- mut_fruit_count) foo += k.toString + v.toString

foo

// SortedMap - implements a tree map, like an OrderedDict
// It is immutable
val scores = scala.collection.immutable.SortedMap("oranges" -> 5, "apples" -> 4)
