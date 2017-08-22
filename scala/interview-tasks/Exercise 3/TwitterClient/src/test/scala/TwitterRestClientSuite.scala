/**
  * Soda Software Labs Ltd. trading as: Hello Soda
  * www.hellosoda.com
  *
  * Programming Exercise: Software Engineer (Scala 3)
  **/
package com.hellosoda.task3
import org.scalatest._

class TwitterRestClientSuite
    extends FunSuite
    with    Matchers {

  val service = new MockTwitterService(serviceUnavailableProbability = 0.2)
  val client = new TwitterRestClient(service)

  test("getAllTweets() response is non-empty") {
    client.getAllTweets().length shouldBe service.tweetCount
  }

}
