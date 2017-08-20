/**
 * Soda Software Labs Ltd. trading as: Hello Soda
 * www.hellosoda.com
 *
 * Programming Exercise: Software Engineer (Scala 1)
 */

/**
 * Notes taken from the official Scala documentation
 * https://docs.scala-lang.org/tour/
 */

/**
 * Case classes
 *      - Good for modeling immutable data
 *      - Useful in pattern matching
 *      - Doesn't need the *new* keyword in construction since case classes
 *        have an *apply* method by default, which takes care of construction
 *      - Parameters are public vals (vars are discouraged since they are
 *        designed primarily for immutable data)
 *      - Compared by structure and not by value, so two different objects
 *        with the same values would be considered equal
 */

 /**
  * Pattern Matching
  *      - Used to check a value against a pattern
  *      - Can destructure successfull matches
  *      - Match expressions take
  *             1. Value
  *             2. *match* keyword
  *             3. At least one *case* value
  *      - Case classes are useful for pattern matching
  *      - Read 'Matching on case classes' from
  *        https://docs.scala-lang.org/tour/pattern-matching.html
  *      - Pattern guards (boolean expressions) can be used to make cases more
  *        specific, just add *if <boolean expression>*
  */
case class Company(
  val name: String,
  val foundedYear: Option[Int] = None) {

  override def toString =
    name
}

case class Position(
  val title: String,
  val company: Option[Company] = None) {

  override def toString =
    company match {
      case Some(company) => s"$title at $company"
      case None => s"freelancing ($title)"
    }
}

case class Person(
  val firstName: String,
  val lastName: String,
  val position: Option[Position] = None) {

  override def toString =
    s"$firstName $lastName"
}

/**
 * Used to create a simple but complete app, so running the file in the
 * terminal with scala *file_name* (after compilation) will run this code
 */
object Test extends App {

  val people = List(
    Person("Paul", "Freeman", Some(Position("Programmer"))),
    Person("Mary", "Martyr", Some(Position("Manager", Some(Company("IBM", Some(1881)))))),
    Person("William", "Davidson", Some(Position("Engineer", Some(Company("Microsoft", Some(1973)))))),
    Person("Erik", "Erikssen", Some(Position("Director", Some(Company("Danish Shipping"))))),
    Person("Mary", "Madsen"),
    Person("Peter", "Barnes", Some(Position("Painter-Writer"))),
    Person("Stig", "Olufssen", Some(Position("Engineer", Some(Company("Danish Shipping"))))),
    Person("Martin", "Peters", Some(Position("Captain", Some(Company("Danish Shipping"))))),
    Person("Bradley", "Smith"),
    Person("Paul", "Jameson", Some(Position("Senior Manager", Some(Company("Microsoft", Some(1973)))))),
    Person("Christopher", "Bulkes", Some(Position("Director", Some(Company("Bulkes Law Office"))))),
    Person("Amy", "Adamson", Some(Position("Paralegal", Some(Company("IBM", Some(1881)))))))
}

// import scala.collection.immutable.{Map, ListMap}

/**
 *
 * Fill in all of the following expressions.
 *
 */

// Get companies that have more than 1 employee
// Get the people who work at those companies


/** Example: find the first person in the list. **/
val firstPerson: Option[Person] =
  people.headOption

/** All (unique) companies. **/
val allCompanies: Set[Company] =
    people.flatMap(_.position.flatMap(_.company)).toSet

/** List people as "LastName, Initial" in alphabetical order. **/
val alphabeticalPeople2: List[String] =
    people.sortBy(_.lastName)
          .map(person => s"${person.lastName}, ${person.firstName(0)}")

/** People with a first name of less than 4 characters. **/
val shortFirstName: Set[Person] =
    people.collect{ case person if person.firstName.length() > 4 => person }.toSet
  
/** Count the number of employees in company `c`. **/
def employeeCount(c: Company): Int =
  people.flatMap(_.position.flatMap(_.company)
        .map(company => company.name))
        .count(_ == c.name)

/** Number of employees per company. **/
val employeesPerCompany: Map[Company, Int] =
  people.flatMap(_.position.flatMap(_.company))
        .groupBy(identity)
        .mapValues(_.size)

/** List of people working for companies with at least one other employee. **/
val corporateEmployees: Set[Person] =
  ???

/** Companies founded before 1900. **/
val historicalCompanies: Set[Company] =
  people.flatMap(_.position.flatMap(_.company)).filter(_.foundedYear.getOrElse(0) < 1900).toSet

/** Titles held by at least 2 people. **/

/**
 * NOTE:
 *      - Issues with mutbale vs immutable
 *      - Solution is inefficient
 *      - Try to come up with a better solution
 */
val popularPositionTitles: Set[String] =
    people.collect{ case x if x.position.isDefined => x.position }
          .map(_.get.title) // get is okay here since because of isDefined
          .groupBy(identity)
          .mapValues(_.size)
          .filter((x) => x._2 > 1)
          .keySet

/** Top 5 letters in given names. **/
/**
 * NOTE:
 *      - I assumed since it states 'given names' that it should have been
 *        a function
 */

// val givenNameLetterTop5: Vector[(Char, Int)] =
//   ???

def givenNameLetterTop5(s: String): Vector[(Char, Int)] =
    s.groupBy(_.toChar)
     .mapValues(_.size)
     .toSeq
     .sortWith(_._2 > _._2)
     .take(5)
     .to[Vector]

/**
 * `titleOfPerson()` is a method that will return the job title
 * of a particular person. A call to this method may incur side effects
 * that are not obvious if looking at its signature.
 *
 * Briefly summarise your assessment of the method and propose changes.
 * You may want to investigate documentation of the methods involved.
 */
def titleOfPerson(person: Person): String =
  person.position.get.title

/**
 * `parsePersonFromString()` is a method that will parse a Person
 * instance from a first-last name string such as "Paul Freeman".
 * It must conform to the following criteria:
 *
 * - A valid input is of the form "{firstName} {lastName}".
 * - A person must have a non-empty first and last name.
 * - The name must have been be capitalised.
 * - The method must return an instance of Person, but this may be wrapped
 *   in another type (e.g. Vector, Option, Either, Try).
 * - The caller of the method must be able to retrieve a human-readable
 *   error message if the name is non-conformant.
 *
 * Implement the method and declare its output type. Take care to
 * demonstrate your implementation in the final section below.
 */

def parsePersonFromString(string: String): ??? =
  ???

/** Visualise all of the above results in standard output. **/

println("Results:")
println("")

print("First person in the list: ")
println(firstPerson.getOrElse("(unknown)"))
