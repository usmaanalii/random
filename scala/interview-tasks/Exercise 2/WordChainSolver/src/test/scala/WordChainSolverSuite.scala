/**
  * Soda Software Labs Ltd. trading as: Hello Soda
  * www.hellosoda.com
  *
  * Programming Exercise: Software Engineer (Scala 2)
  **/
package com.hellosoda.task2
import org.scalatest._

class WordChainSolverSuite
    extends FunSuite
    with    Matchers {

  val solver = new WordChainSolver

  test("warm..cold") {
    val chain = solver.chain("warm", "cold")
    info(chain.toString)
    chain.isDefined shouldBe true
    chain.get.length shouldBe 5
  }

}
