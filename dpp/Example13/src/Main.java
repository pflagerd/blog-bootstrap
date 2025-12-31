//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {

    static int count = 0;

    static int fib(int n) {
        count++;
        if (n <= 0) return 0;
        else if (n == 1) return 1;
        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {
        for (int i = 0; i < 20; i++) {
            count = 0;
            System.out.println("i == " + i + " fib(" + i + ") == " + fib(i) + " count == " + count);
        }
    }
}