<?php

class Solution {

    /**
     * @param String $s
     * @return String
     */
    function reverseWords(string $s) {
        $this->normalizeWhiteSpaces($s);
        $this->reverseString($s, 0, strlen($s) - 1);

        $left = null;
        $right = null;
        for($i = 0; $i < strlen($s); $i++){
            if($s[$i] !== " "){
                if($left === null){
                    $left = $i;
                    $right = $i;
                } else {
                    $right = $i;
                }
            } else {
                if($left && $right){
                    $this->reverseString($s, $left, $right);
                    $left = null;
                    $right = null;
                }
            }
        }

        if($left && $right){
            $this->reverseString($s, $left, $right);
            $left = null;
            $right = null;
        }

        return $s;
    }

    // "   hello  you  "

    function normalizeWhiteSpaces(string &$s){
        $read = 0;
        $write = 0;
        
        while ($read < strlen($s)){
            if($s[$read] === " "){
                
                while($read < strlen($s) && $s[$read] === " "){
                    $read++;
                }
                
                $s[$write] = " ";
                $read++;
                $write++;
            } else {
                while($s[$read] !== " "){
                $s[$write] = $s[$read];
                    $read++;
                    $write++;
                }
            }
        }
    }

    function reverseString(string &$s, $start, $end){
        $left = $start;
        $right = $end;

        while($left < $right){
            [$s[$left], $s[$right]] = [$s[$right], $s[$left]];
            $left++;
            $right--;
        }
    }
}