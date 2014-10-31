(ns hackasm.inst-test
  (:require [clojure.test :refer :all]
            [hackasm.inst :refer :all]))

(deftest gen-ainst-test
  (testing "gen-ainst test"
    ; @0
    (is (= "0000000000000000" (gen-ainst "0")))
    ; @1 
    (is (= "0000000000000001" (gen-ainst "1")))
    ; @14
    (is (= "0000000000001110" (gen-ainst "14"))))) 

(deftest gen-cinst-test 
  (testing "gen-cinst test" 
    ; 0;JMP 
    (is (= "1110101010000111" (gen-cinst "0" "null" "JMP")))  
    ; M=D
    (is (= "1110001100001000" (gen-cinst "D" "M" "null"))))) 

