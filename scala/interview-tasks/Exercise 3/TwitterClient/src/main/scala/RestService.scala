/**
  * Soda Software Labs Ltd. trading as: Hello Soda
  * www.hellosoda.com
  *
  * Programming Exercise: Software Engineer (Scala 3)
  **/
package com.hellosoda.task3
import play.api.libs.json._

object RestService {
  sealed trait Response
  object Response {
    case object ServiceUnavailable extends Response
    case class Datum (val datum : JsValue) extends Response
  }
}

trait RestService {
  def get (path : String, query : Map[String, String]) : RestService.Response
}
