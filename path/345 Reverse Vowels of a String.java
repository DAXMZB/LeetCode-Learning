// we need revers all vowels, and keeping other charaters in their orighin position
// I will use Two-Pointer technique ,place one pointer at the start and another at the end
// move both pointer until hit a vowel, when both pointer hit a vowel then swap it and keep move until the pointers met
// start pointer less then end pointer
class Solution {
    public String reverseVowels(String s) {
        // through string is Immutable
        // convert string to array for swapping
        char[] c = s.toCharArray();
        // define left as start pointer, right as end
        int left = 0;
        int right = s.length() - 1;

        // define a string contain all vowels
        String vowels = "aeiouAEIOU";

        // give a whiel loop for Two-Pointer move to hit vowels
        // during while use boundary check to ensure pointer would not go out of bounds
        while (left < right) {
            // we need Two pinter keep move before hit vowel and incuding consider boundary
            // if vowel point indexOf array c equal minus 1 means not hit vowel then keep move
            while (left < right && vowels.indexOf(c[left]) == -1) {
                // keep move and left plus 1
                left ++;
            }

            while (left < right && vowels.indexOf(c[right]) == -1) {
                // keep move and right minus 1
                right --;
            }

            // when both pointer out the while loop means both hit the vowel
            // and swepping left and right charater
            // defind interger tmp to record left before swapping
            char tmp = c[left];
            c[left] = c[right];
            c[right] = tmp;

            // move pointer after swapping to avoid infinite loop
            left ++;
            right --;
        }

        // convert char array back to string
        return new String(c);
    }
}