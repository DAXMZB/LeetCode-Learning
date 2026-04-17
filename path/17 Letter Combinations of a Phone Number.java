// we need Mapping numbers to letters and return all possible combanations that number could be represent

// I will use backTracking and Recursive Function

class Solution {
    // Declare a MAPPING array that each number represent the all letters
    //  0 and 1 does not map to any letters
    //  use final with immutability
    private static final String[] MAPPING = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        // declare List to return result combinations throgh backTrack
        List<String> result = new ArrayList<>();
        // start with a null and empty check as a part of Defensive Programing to handle invalid input safely
        if (digits == null || digits.length() == 0) {
            return result;
        }

        // use bacTracking
        backTrack(result, digits, new StringBuilder(), 0);

        return result;
    }

    // Delcare a backTrack function 
        // include List<String> to inject all possible combanation numbers,
        //         String digits about input number
        //         StringBuilder current use to append combanations leeter's in backTrack and       
                        //recursion
        //         int index means the length with digits's length and combanasion's length
    private void backTrack(List<String> result, String digits, StringBuilder current, int index) {
        // while index equal to digits's length , means find the current combinaions
        if (index == digits.length()) {
            result.add(current.toString());
            return;
        }

        // we need travel digits that current each digits represent letters
        // use charAt to find digits's represent letters from MAPPING by substracking '0', convert digits's corresponding base on ASCII values
        String letters = MAPPING[digits.charAt(index) - '0'];
        // use loop to travel each letters
        for (char c : letters.toCharArray()) {
            // during travel letters and append current letter
            current.append(c);
            // in the same time use recursion to find next posion of digits and letters
            backTrack(result, digits, current, index + 1); // index plus one menas next positions
            // when index equals digits's length and after return means finish current combinations
            //  and remove last letter to find next letter
            current.deleteCharAt(current.length() - 1); 
            // After the recursives all return, i backtrack from StringBuilder to reset the state for the next iterate
        }
    }
}