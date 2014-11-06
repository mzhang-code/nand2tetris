(ns translator.code-snippet-test
  (:require [clojure.test :refer :all]
            [translator.code-snippet :refer :all]))

(deftest a-test
  (testing "FIXME, I fail."
    ; (pprint (push-code "local" "1234"))
    (print (pop-code "local" "1"))
    ))

