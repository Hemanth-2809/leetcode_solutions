class Solution {
    public boolean isPalindrome(String s) {
        String newstring = "";
        for(int i=0;i<s.length();i++){
            if (Character.isLetterOrDigit(s.charAt(i))){
                newstring+=Character.toLowerCase(s.charAt(i));
            }
        }
        int i =0;
        int j = newstring.length()-1;
        while (i<j){
            if (newstring.charAt(i)!=newstring.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
        
    }
}
