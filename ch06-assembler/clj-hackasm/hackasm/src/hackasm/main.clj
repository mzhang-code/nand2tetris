(ns hackasm.main
  (:require [clojure.java.io :as io] 
            [clojure.string :as string] 
            [hackasm.core :as core])
  (:gen-class))

(defn -main
  [file]
  (with-open [rdr (io/reader file)] 
    (println (string/join "\n" (core/parse (line-seq rdr)))) 
    (flush))) 

