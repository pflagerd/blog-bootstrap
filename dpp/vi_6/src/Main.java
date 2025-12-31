public class Main {
    static int count = 0;

    static int sqrt(int n) {
        for (int guess = 1; guess * guess <= n; guess++) {
            count++;
            if (guess * guess == n) {
                return guess;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        for (int i = 1; i <= 1000; i++) {
            count = 0;
            System.out.println("i = " + i + " sqrt(" + i + ") == " + sqrt(i) + " count = " + count);
        }
    }
}