(ns hackasm.symbol-table-test
  (:require [clojure.test :refer :all]
            [hackasm.symbol-table :refer :all]))

(deftest symbol-table-test 
  (testing "symbol table" 
    (insert-symbol-table "x") 
    (is (= (:alloc @symbol-table) (inc (query-symbol-table "x")))))) 

