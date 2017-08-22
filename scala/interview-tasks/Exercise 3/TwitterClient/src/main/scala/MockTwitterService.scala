/**
  * Soda Software Labs Ltd. trading as: Hello Soda
  * www.hellosoda.com
  *
  * Programming Exercise: Software Engineer (Scala 3)
  **/
package com.hellosoda.task3
import play.api.libs.json._

class MockTwitterService (
  val tweetCount : Int = 111,
  val subscriptionCount : Int = 70,
  val serviceUnavailableProbability : Double = 0.2)
    extends RestService {

  import RestService.Response

  private val random = new scala.util.Random(seed = 1)

  def get (
    path : String,
    query : Map[String, String]
  ) : Response = {
    if (random.nextDouble() < serviceUnavailableProbability) {
      return Response.ServiceUnavailable
    }

    val maxId = query.get("max_id").map(_.toInt)
    val cursor = query.get("cursor").map(_.toInt)
    val count = query.get("count").map(_.toInt)

    path match {
      case "/statuses/user_timeline" => getUserTimeline(maxId, count)
      case "/lists/subscriptions" => getSubscriptions(cursor, count)
    }
  }

  private def getUserTimeline (
    maxId : Option[Int],
    count : Option[Int]
  ) : Response = {
    val available = maxId match {
      case None =>
        userTimeline

      case Some(n) if n < 0 =>
        userTimeline

      case Some(maxId) =>
        userTimeline.filter { tweet =>
          val id = (tweet \ "id").as[Int]
          id < maxId
        }
    }

    val effectiveCount = count.getOrElse(7).max(0).min(7)
    Response.Datum(JsArray(available.take(effectiveCount)))
  }

  private def getSubscriptions (
    cursor : Option[Int],
    count  : Option[Int]
  ) : Response = {
    val available = cursor match {
      case None | Some(-1) => subscriptions
      case Some(c) => subscriptions.drop(c)
    }

    val effectiveCount = count.getOrElse(11).max(0).min(11)
    val page = available.take(effectiveCount)
    val isFinalPage = page.length == available.length
    val nextCursor =
      if (isFinalPage) Json.obj()
      else Json.obj(
        "next_cursor" -> ((0 max cursor.getOrElse(0)) + page.length))

    Response.Datum(Json.obj("lists" -> page) ++ nextCursor)
  }

  private val userTimeline : Vector[JsObject] =
    for {
      n <- Range(tweetCount, 0, -1).toVector
      t =  Json.obj(
        "id"   -> n,
        "text" -> s"Tweet $n")
    } yield t

  private val subscriptions : Vector[JsObject] =
    for {
      n <- Range(subscriptionCount, 0, -1).toVector
      s =  Json.obj(
        "id"   -> n,
        "name" -> s"List $n",
        "user" -> Json.obj(
          "name" -> s"User $n"),
        "subscriber_count" -> (n * 100))
    } yield s

}
