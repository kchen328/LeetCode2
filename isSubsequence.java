class Solution {
    public boolean isSubsequence(String s, String t) {
        StringBuilder sb = new StringBuilder(s);
        
        if (sb.length() == 0)
                return true;
        
        for (char c : t.toCharArray()) {
            if (c == sb.charAt(0))
                sb.deleteCharAt(0);
            if (sb.length() == 0)
                return true;
        }
        
        return false;
    }
}
