/**
  * Soda Software Labs Ltd. trading as: Hello Soda
  * www.hellosoda.com
  *
  * Programming Exercise: Software Engineer (Scala 3)
  **/
package com.hellosoda.task3
import play.api.libs.json._

class TwitterRestClient (
  val service : RestService) {

  def getAllTweets () : Vector[Tweet] =
    ???

  def getAllSubscriptions () : Vector[Subscription] =
    ???
}
