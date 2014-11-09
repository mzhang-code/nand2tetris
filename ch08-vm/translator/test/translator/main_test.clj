(ns translator.main-test
  (:use [clojure.pprint :only [pprint]])
  (:require [clojure.test :refer :all]
            [clojure.java.io :as io]
            [translator.core :as core]
            [translator.main :refer :all]))

(def test-data-dir "test/translator/vm/") 

(deftest a-test
  (testing "FIXME, I fail."
    (with-open [rdr (io/reader (str test-data-dir "SimpleAdd.vm"))]
      (let 
        [lines (line-seq rdr)] 
        (pprint 
          (->> lines 
            (map rm-comment)
            (map trim-expr)
            (rm-empty-lines)
            (map-indexed vector) 
            (mapcat (fn [args] (apply core/translate-expr args)))
               )))))) 

