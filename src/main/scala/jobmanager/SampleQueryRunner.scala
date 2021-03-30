// package jobmanager

import java.rmi.Naming
import scala.collection.mutable.ArrayBuffer
import jobmanager.JobManagerInterface

object SampleQueryRunner {
  def main(args: Array[String]): Unit = {
    // (map, 3), (map, 2), (reduce, 1)
    val ops = Array("map", "map", "reduce")
    val parallelisms = Array(3, 2, 1)
    val dataSize = 8000

    val jobManager =
      Naming.lookup("jobmanager").asInstanceOf[JobManagerInterface]
    val success = jobManager.runJob(ops, parallelisms, dataSize)

    if (success) {
      println("Started query sucessfully")
    } else {
      println("Job failed")
    }
  }
}
