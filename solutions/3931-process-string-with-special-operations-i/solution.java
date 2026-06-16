class Solution {

    public StringBuilder reverse(StringBuilder s) {
        int n = s.length();

        for (int i = 0; i < n / 2; i++) {
            char l = s.charAt(i);
            char r = s.charAt(n - 1 - i);

            s.setCharAt(i, r);
            s.setCharAt(n - 1 - i, l);
        }

        return s;
    }

    public String processStr(String s) {
        int n = s.length();
        StringBuilder res = new StringBuilder();

        for (int i = 0; i < n; i++) {
            char curr = s.charAt(i);

            if (curr == '#') {
                res.append(res.toString());
            }
            else if (curr == '*') {
                if (res.length() > 0) {
                    res.deleteCharAt(res.length() - 1);
                }
            }
            else if (curr == '%') {
                reverse(res);
            }
            else {
                res.append(curr);
            }
        }

        return res.toString();
    }
}
