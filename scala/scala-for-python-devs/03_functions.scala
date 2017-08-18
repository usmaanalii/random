// Functions
// refers to => and def function definitons

def concat_num_str(x: Int, y: String ) = x.toString + y
concat_num_str(1, "string")

// Passing the incorrect type...
concat_num_str("string", num) // type mismatch

// Use a bracketed block, if using multiple expressions
import scala.collection.mutable.Map

val str_arr = Array("apple", "orange", "grape")

def len_to_map(arr: Array[String]) = {
    var lenmap: Map[String, Int] = Map()
    for (a <- arr) lenmap += (a -> a.length)
    lenmap
}

len_to_map(str_arr)

// You can specify return types (and need to do in recursive funcs)
def factorial(n: Int): Int = if (n <= 0) 1 else n * factorial(n - 1)
factorial(5)

// Do it, it's best practice
def spec_type(x: Int, y: Double): Int = x + y.toInt
spec_type(1, 3.4)

// Default and named arguments
def make_arr(x: String, y: String, fruit: String = "apple", drink: String = "water") = Array(x, y, fruit, drink)

make_arr("orange", "banana")
make_arr("orange", "banana", "melon")
make_arr("orange", "banana", drink="coffee")

// Need to specify non-named parameters before named ones
make_arr("orange", drink="coffee", "banana") // error

// less flexible than *args

def sum_args(args:Int*) = args.sum
sum_args(1, 2, 3, 4, 5)

// Passing in a sequence, needs destructuring
sum_args([1, 2, 3]) // error

sum_args(*[1, 2, 3])

def proc_func(x: String, y: String) {print(x + y)}
proc_func("x", "y")

// Anonymous functions (like lambda)
val concat_fruit = (x: String, y: String) => x + y
concat_fruit("apple", "orange")

// Functions are first class citizens, so can be passed to higher order functions
def ApplyToArgs(func: (String, String) => String, arg1: String, arg2: String): String = func(arg1, arg2)

applyToArgs(concat_fruit, "apple", "banana")

    
def applySingleArgFunc(func: (Int) => Int, arg1: Int): Int = func(arg1)

applySingleArgFunc((x: Int) => x + 5, 1)

// Currying
def concat_curried(fruit: String)(veg: String): String = fruit + veg

val curried = concat_curried("apple")_

curried("spinach")
curried("carrot")

