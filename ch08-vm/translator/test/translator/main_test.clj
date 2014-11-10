(ns translator.main-test
  (:use     [clojure.pprint   :only   [pprint]])
  (:require [clojure.test     :refer  :all]
            [clojure.java.io  :as     io]
            [translator.core  :as     core]
            [translator.main  :refer  :all]))

(def test-data-dir "test/translator/vm/") 

(deftest a-test
  (testing "FIXME, I fail."
    (println (translate-vm-file (str test-data-dir 
                            "FibonacciElement/Main.vm"))))) 

