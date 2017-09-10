/**
  * Soda Software Labs Ltd. trading as: Hello Soda
  * www.hellosoda.com
  *
  * Programming Exercise: Software Engineer (Scala 2)
  **/
package com.hellosoda.task2
import scala.io.Source

class WordChainSolver {
  val startWord: String = "cat"
  val endWord: String = "dog"
  var wordChain = List[String]()
  
  val words : Set[String] =
    Source.fromFile("./src/main/resources/dictionary.txt")
          .getLines
          .flatMap(_.split(","))
          .filter(_.length == startWord.length)
          .toSet
  
  def differenceScore (firstWord: String, secondWord: String): Int = {
      val pairs = firstWord.toList zip secondWord.toList
      
      pairs.map(pair => (pair._1 == pair._2))
           .count(_ == true)
  }
  
  def getAdjacentWords (inputWord: String, words: Set[String]): Set[String] = {
      words.filter(word => 
                   differenceScore(inputWord, word) == inputWord.length - 1)
  }
  
  def endWordMatch(inputWord: String, matchWord: String): Unit = {
      if (inputWord == matchWord)
        wordChain = inputWord :: wordChain
  }
  
  /**
   * 1. Call getAdjacentWords(startWord, words) which will return Set[Strings]
   *    containing all adjacent words (with difference of one letter)
   * 2. Call endWordMatch on each word
   *        a). If true, then the word will be appended to wordChain
   *        b). If false, need to recurseively repeat 1 on each word
   *            (Need to keep track of each word that getAdjacentWords is
   *            called on i.e the "new" startWord and append both it and the
   *            endWord to wordChain, this tracking behavior will probably
   *            need to use a Map(word -> adjacentWords and could lead to
   *            nested Maps i.e Map(word -> Map(word2 -> adjacentWords)))
   */
  
  def chain (from : String, to : String) : Option[Vector[String]] =
    ???
}
