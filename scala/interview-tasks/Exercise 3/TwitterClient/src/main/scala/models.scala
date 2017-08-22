/**
  * Soda Software Labs Ltd. trading as: Hello Soda
  * www.hellosoda.com
  *
  * Programming Exercise: Software Engineer (Scala 3)
  **/
package com.hellosoda.task3
import play.api.libs.json._

/** Define this domain model by inspection of MockTwitterservice.scala! **/
case class Tweet ()

object Tweet {
  implicit val format : OFormat[Tweet] =
    Json.format[Tweet]
}

/** Define this domain model by inspection of MockTwitterservice.scala! **/
case class User ()

object User {
  implicit val format : OFormat[User] =
    Json.format[User]
}

/** Define this domain model by inspection of MockTwitterservice.scala! **/
case class Subscription (
  val user : User)

object Subscription {
  implicit val format : OFormat[Subscription] =
    Json.format[Subscription]
}
