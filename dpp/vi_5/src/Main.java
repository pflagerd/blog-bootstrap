public class Main {
    static int count = 0;

    static int sqrt(int n) {
        return sqrt_helper(n, 1, n);
    }
    static int sqrt_helper(int n, int min, int max) {
        count++;
        if (max < min) return -1;
        int guess = (min + max) / 2;
        if (guess *guess == n) {
            return guess;
        } else if (guess * guess < n) {
            return sqrt_helper(n, guess + 1, max);
        } else {
            return sqrt_helper(n, min, guess - 1);
        }
    }

    public static void main(String[] args) {
        for (int i = 1; i <= 1000; i++) {
            count = 0;
            System.out.println("i = " + i + " sqrt(" + i + ") == " + sqrt(i) + " count = " + count);
        }
    }
}