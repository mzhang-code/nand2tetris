(ns hackasm.core-test
  (:require [clojure.test :refer :all]
            [hackasm.core :refer :all]))

(deftest remove-blank-test
  (testing "remove-blank test"
    (is (=  "@1//setAto1." (remove-blank "@1      // set A to 1. \n"))))) 

(deftest remove-comment-test
  (testing "remove-comment test"
    (is (=  "@1" (remove-comment "@1  // :-) set A to 1! \n"))))) 

