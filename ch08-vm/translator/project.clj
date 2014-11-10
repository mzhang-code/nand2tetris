(defproject translator "0.1.0"
  :description "The Full-Scale VM Translator."
  :url "https://github.com/my-zhang/nand2tetris/tree/master/ch07-vm/translator"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.5.1"]]
  :aot [translator.main translator.core])

