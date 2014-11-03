import scala.io.Source

object BasicTranslator {

  def rmComment(s: String): String = { 
    val commentPattern = """\s*//.*""".r 
    return commentPattern.replaceAllIn(s, "") 
  }

  def isEmptyLine(s: String): Boolean = { 
    return s.trim.length == 0 
  }

  def trimInput(lines: Array[String]): Array[String] = { 
    return lines.map(s => rmComment(s)).filter(s => !isEmptyLine(s)) 
  }

  def main(args: Array[String]): Unit = { 
    if (args.length == 0) { 
      println("specify a input file or dir.")
      return 
    }

    val fd = Source.fromFile(args(0))
    val lines = fd.getLines.toArray
    val exprs = trimInput(lines) 

    for (e <- exprs) { 
      println(e) 
    }
  }
}
