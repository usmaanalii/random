name := "hello-soda"
version := "0.1.0"
scalaVersion := "2.12.3"

// libraryDependencies += groupID % artifactID % version % configuration
libraryDependencies += "org.scalatest" % "scalatest_2.11" % "2.2.6" % "test"

// Writing your own tasks
//      1. Define a TaskKey
//      2. Provide task definition

// val gitCommitCountTask = taskKey[String]("Prints commit count of the current branch")
// 
// gitCommitCountTask := {
//   val branch = Process("git symbolic-ref -q HEAD").lines.head.replace("refs/heads/","")
//   val commitCount = Process(s"git rev-list --count $branch").lines.head
//   println(s"total number of commits on [$branch]: $commitCount")
//   commitCount
// }