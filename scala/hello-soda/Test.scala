/**
 * Soda Software Labs Ltd. trading as: Hello Soda
 * www.hellosoda.com
 *
 * Programming Exercise: Software Engineer (Scala 1)
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
/**
 *
 * Fill in all of the following expressions.
 *
 */

/** Example: find the first person in the list. **/
val firstPerson: Option[Person] =
  people.headOption

printl(firstPerson)

/** All (unique) companies. **/
val allCompanies: Set[Company] =
  ???

/** List people as "LastName, Initial" in alphabetical order. **/
val alphabeticalPeople: List[String] =
  ???

/** People with a first name of less than 4 characters. **/
val shortFirstName: Set[Person] =
  ???

/** Count the number of employees in company `c`. **/
def employeeCount(c: Company): Int =
  ???

/** Number of employees per company. **/
val employeesPerCompany: Map[Company, Int] =
  ???

/** List of people working for companies with at least one other employee. **/
val corporateEmployees: Set[Person] =
  ???

/** Companies founded before 1900. **/
val historicalCompanies: Set[Company] =
  ???

/** Titles held by at least 2 people. **/
val popularPositionTitles: Set[String] =
  ???

/** Top 5 letters in given names. **/
val givenNameLetterTop5: Vector[(Char, Int)] =
  ???

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
