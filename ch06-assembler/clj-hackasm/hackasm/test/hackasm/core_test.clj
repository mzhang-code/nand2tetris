(ns hackasm.core-test
  (:require [clojure.test :refer :all]
            [hackasm.core :refer :all]))

(deftest a-test
  (testing "FIXME, I fail."
    (is (= 0 0))))

(deftest gen-cinst-test 
  (testing "Hi." 
    ; 0;JMP 
    (is (= "1110101010000111" (gen-cinst "0" "null" "JMP")))  
    ; M=D
    (is (= "1110001100001000" (gen-cinst "D" "M" "null"))))) 

