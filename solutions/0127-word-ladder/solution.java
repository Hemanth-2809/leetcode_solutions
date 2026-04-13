import java.util.*;

class Pair {
    String word;
    int steps;

    Pair(String word, int steps) {
        this.word = word;
        this.steps = steps;
    }
}

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {

        Set<String> set = new HashSet<>(wordList);

        if (!set.contains(endWord)) return 0;

        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(beginWord, 1));

        set.remove(beginWord);

        while (!q.isEmpty()) {
            
            String word = q.peek().word;
            int steps = q.peek().steps;
            q.remove();

            if (word.equals(endWord)) {
                return steps;
            }

            for (int i = 0; i < word.length(); i++) {
                char[] arr = word.toCharArray();

                for (char ch = 'a'; ch <= 'z'; ch++) {
                    arr[i] = ch;
                    String newWord = new String(arr);

                    if (set.contains(newWord)) {
                        q.add(new Pair(newWord, steps + 1));
                        set.remove(newWord);
                    }
                }
            }
        }

        return 0;
    }
}
