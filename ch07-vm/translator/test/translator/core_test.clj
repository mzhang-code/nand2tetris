(ns translator.core-test
  (:use [clojure.pprint :only [pprint]])
  (:require [clojure.test :refer :all]
            [translator.core :refer :all]))

(deftest a-test
  (testing "FIXME, I fail."
    (pprint (translate-expr 0 "add"))
    (print (translate-expr 0 "push constant 1024"))
    ))

