// Sequences

// There are many to choose from
//      - List (linked-lists)
//      - Vectors (immutable arrays)
//      - Arrays (mutable arrays of fixed length)
//      - ArrayBuffers(mutable arrays of varying length)

// Vector is the best default immutable sequence in Scala
val vector = Vector(1, 2, 3)

vector.map(_ + 2)
vector.count(_ == 2)

Vector(1, 2, 3, 4, 5).drop(3) // drops the first 3 elements

vector.exists(_ == 4)

vector.take(2) // creates new vector with the first 2 values

Vector(1, 20, 3, 25).reduce(_ + _)

Vector(3, 4, 4, 5, 3).distinct // unique values

Vector(1, 20, 3, 25).partition(_ > 10) // creates two vectors (tuple like??)

// creates a mapping of boolean -> Vector with true/false values
Vector("foo", "bar", "baz", "foo", "bar").groupBy(_ == "foo")

Vector(1, 20, 3, 25).groupBy(_ > 10) // map like above

vector.filter(_ != 2)

vector.max

Vector(3, 2, 1).sorted

Vector("fo", "fooooo", "foo", "foooo").sortWith(_.length > _.length)

vector.sum

Vector(Vector(1, 2, 3), Vector(4, 5, 6)).flatten

// Another way to 'flatten'
Vector.concat(Vector(1, 2, 3), Vector(4, 5, 6))

Vector(1, 2, 3).intersect(Vector(3, 4, 5))

Vector(1, 2, 3).diff(Vector(3, 4, 5))

// Array is a fixed length, so you can initialize values
val init_int = new Array[Int](10)

val init_str = new Array[String](10)

Array.tabulate(3)(a => a + 5)

Array.tabulate(3)(a => a * 5)

Array.fill(3)(10)

// ArrayBuffer is the go-to mutable sequence, and works more like Python lists
import scala.collection.mutable.ArrayBuffer

val int_arr = ArrayBuffer[Int]()
int_arr += 1
int_arr += (2, 3, 4)
int_arr ++= Array(5, 6, 7)

int_arr.count(_ == 1)

int_arr.trimEnd(5)
int_arr // removes final 5 elements

int_arr.insert(1, 5) // inserts 1 and 5
int_arr

int_arr.remove(1)

// Be more flexible with multiple inserts/removals
int_arr.insert(1, 5, 6)
int_arr

int_arr.remove(1, 2) // removes elemens at positions 1 and 2
int_arr

int_arr.reverse

int_arr.max

int_arr.min

int_arr.reverse.sorted

int_arr.clear
int_arr

// Comprehension alternative
val foo = for (x <- 0 until 10) yield x

val foo = for (x <- 0 until (10, 2)) yield x // 2 is a step count

// Scala also has a "to" operator for inclusive ranges
0 to (10, 2)

0 until (10, 2) // exclusive

// Using the "guard" clause
val foo = for (x <- Vector("foo", "bar", "baz") if x != "foo") yield x + "qux"

// Comprehension returns the type that is fed to it
val foo = for (x <- ArrayBuffer("foo", "bar", "baz") if x != "foo") yield x + "qux"

// Functional approach
Vector("foo", "bar", "baz").filter(_ != "foo").map(_ + "qux")

// Supports multidimensional arrays out of the box, no need for external
// libraries like numpy
val multdim = Array.ofDim[Int](3, 4)
multdim
