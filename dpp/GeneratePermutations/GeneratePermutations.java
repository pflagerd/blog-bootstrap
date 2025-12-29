import java.lang.System;

public class GeneratePermutations {

    static int factorial(int n) {
        int factorial = 1;
        if (n == 0) return factorial;
        for (int i = 0; i < n; i++) {
            factorial *= factorial;
        }
        return factorial;
    }

    static String generatePermutationCode(String input) {
        for (int i = 0; i < input.length(); i++) {
            String outString = "for (int i" + i + " = 0; i" + i + " < input.length(); i"+ i + "++) {";
            for (int j = 0; i != 0 && j < i; j++)
                outString = "  " + outString;
            System.out.println(outString);
        }
        return "";
    }

    static String generatePermutations(String input) {
        StringBuilder [] output = new StringBuilder[factorial(input.length())]; // Is StringBuffer or StringBuilder better?

        for (int i = 0; i < input.length(); i++) {
            System.out.println(input.charAt(i));
            for (int j = 0; j < input.length(); j++) {
                if (j != i)
                    System.out.println(input.charAt(j));
            }
        }

        return output.toString();
    }

    public static void main(String[] args) {
        //generatePermutations("abcd");
        generatePermutationCode("abcd");
    }
}
