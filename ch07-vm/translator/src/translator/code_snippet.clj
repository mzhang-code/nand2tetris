(ns translator.code-snippet) 

(defn push-code 
  [seg index]
  (let 
    [assignment '("@SP" 
                  "A=M" 
                  "M=D"
                  "@SP" 
                  "M=M+1")] 
    (concat 
      (cond 
        (= seg "constant") `(~(str "@" index) 
                             "D=A")
        :else `(~(str "@" seg) 
                "D=M" 
                (str "@" index) 
                "A=D+A" 
                "D=M"))
      assignment)))

(defn pop-code 
  [seg index] 
  `(~(str "@" seg) 
    "D=M" 
    ~(str "@" index) 
    "D=D+A" 
    "@R13" 
    "M=D" 
    "@SP" 
    "AM=M-1" 
    "D=M" 
    "@R13" 
    "A=M" 
    "M=D"))

(defn unary-arith-code 
  [cmd] 
  (let 
    [access-oprand '("@SP"
                     "A=M-1")] 
    (concat access-oprand 
            (cond 
              (= cmd "not") '("M=!M") 
              (= cmd "neg") '("D=0"
                              "M=D-M"))))) 

(defn binary-arith-code 
  [cmd] 
  (let 
    [access-oprands '("@SP" 
                      "AM=M-1" 
                      "D=M"
                      "A=A-1")] 
    (concat access-oprands 
            (cond 
              (= cmd "add") '("M=M+D") 
              (= cmd "sub") '("M=M-D") 
              (= cmd "and") '("M=M&D") 
              (= cmd "or")  '("M=M|D"))))) 

(defn get-cmp-op 
  [cmp] 
  (cond 
    (= cmp "gt") "JLE" 
    (= cmp "lt") "JGE" 
    (= cmp "eq") "JNE")) 

(defn binary-cmp-code 
  [cmd index] 
  (let 
    [op (get-cmp-op cmd)] 
    `("@SP" 
      "AM=M-1"
      "D=M" 
      "A=A-1"
      "D=M-D"
      ~(str "@FALSE" index) 
      ~(str "D;" op)
      "@SP" 
      "A=M-1" 
      "M=-1"
      ~(str "@CONTINUE" index) 
      "0;JMP" 
      ~(str "(FALSE" index ")")
      "@SP" 
      "A=M-1" 
      "M=0"
      ~(str "(CONTINUE" index ")"))))

