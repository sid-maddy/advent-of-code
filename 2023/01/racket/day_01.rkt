#lang typed/racket

(define digit-prefix?
  (λ ([s : String])
    (regexp-match #rx"^([0-9]|zero|one|two|three|four|five|six|seven|eight|nine)" s)))

(define string->digit
  (λ ([string : String]) : Char
    (define make-string-prefix?
      (λ ([prefix : String]) : (-> String Boolean)
        (λ ([s : String]) : Boolean (string-prefix? s prefix))))

    (match string
      [(regexp #rx"^[0-9]") (string-ref string 0)]
      [(? (make-string-prefix? "zero")) #\0]
      [(? (make-string-prefix? "one")) #\1]
      [(? (make-string-prefix? "two")) #\2]
      [(? (make-string-prefix? "three")) #\3]
      [(? (make-string-prefix? "four")) #\4]
      [(? (make-string-prefix? "five")) #\5]
      [(? (make-string-prefix? "six")) #\6]
      [(? (make-string-prefix? "seven")) #\7]
      [(? (make-string-prefix? "eight")) #\8]
      [(? (make-string-prefix? "nine")) #\9]
      [_ (raise-argument-error 'string->digit "digit?" string)])))

(define digits : (-> String (Listof Char))
  (λ ([line : String]) : (Listof Char)
    (cond
      [(not (non-empty-string? line)) '()]
      [(match (digit-prefix? line)
         [#f (digits (substring line 1))]
         [(cons s _)
          (append (list (string->digit s)) (digits (substring line 1)))])])))

(define calibrate
  (λ ([line : String]) : (U Zero Positive-Byte)
    (cond
      [(not (non-empty-string? line)) 0]
      [(let* ([ds (digits line)]
              [f (first ds)]
              [l (last ds)])
         (cast (string->number (string f l)) Positive-Byte))])))

(define solve
  (λ ()
    (for/sum : (U Zero Positive-Integer)
      ([line (in-lines)])
      (calibrate line))))

(with-input-from-file "../input.txt" solve)
