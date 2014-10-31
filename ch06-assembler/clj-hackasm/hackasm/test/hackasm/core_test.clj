(ns hackasm.core-test
  (:require [clojure.test :refer :all]
            [clojure.java.io :as io] 
            [hackasm.core :refer :all]
            [hackasm.symbol-table :refer :all]))

(deftest remove-blank-test
  (testing "remove-blank test"
    (is (= "@1//setAto1." (remove-blank "@1      // set A to 1. \n"))))) 

(deftest remove-comment-test
  (testing "remove-comment test"
    (is (= "@1" (remove-comment "@1//setAto1."))))) 

(deftest parse-line-test 
  (testing "parse-line test" 
    (is (= "1111010011010000" (parse-line "D=D-M")))
    (is (= "1110101010000111" (parse-line "0;JMP")))
    (is (= "1110001100001000" (parse-line "M=D"))))) 

(def test-suits 
  '("Max", "MaxL" "Pong" "PongL" "Rect", "RectL", "Mult", "Fill")) 
(def test-suit-dir "test/hackasm/asm/") 

(deftest parse-test 
  (testing "" 
    (doseq [s test-suits] 
        (with-open [source (io/reader (str test-suit-dir s "._asm"))
                    target (io/reader (str test-suit-dir s ".hack"))] 
          (is (= (line-seq target) (parse (line-seq source))))))))
      
