import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.*;
import java.util.*;

/**
 * Self-contained Java class with inline tests that can run without JUnit.
 * Ideal for demos, quick verification, or environments without JUnit installed.
 */
public class P51 {

    String removeCharAt(String input, int i) {
        return input.substring(0, i) + input.substring(i + 1);
    }

    // ---------------------------------------------------
    // Production Code
    // ---------------------------------------------------

    static int j = 0;
    static int stackDepth = 0;

    void permutation(String str) {
        stackDepth++;
        permutation(str, "");
        stackDepth--;
        System.out.println(j);
    }

    void permutation(String input, String output) {
        j++;
        if (input.isEmpty()) {
            System.out.println("output == \"" + output + "\"");
        } else {
            for (int i = 0; i < input.length(); i++) {
                stackDepth++;
                permutation(removeCharAt(input, i), output + input.charAt(i));
                stackDepth--;
            }
        }
    }

    // ---------------------------------------------------
    // Custom Minimal Test Framework
    // ---------------------------------------------------

    @Retention(RetentionPolicy.RUNTIME)
    @interface Test {
    }

    @Retention(RetentionPolicy.RUNTIME)
    @interface DisplayName {
        String value();
    }

    // ---------------------------------------------------
    // Inline Test Cases
    // ---------------------------------------------------

//    @Test
//    @DisplayName("Permutation of empty string")
//    void testEmptyString() {
//        permutation("");
////        assertEqual(7, add(3, 4), "3 + 4 should equal 7");
//    }

//    @Test
//    @DisplayName("Permutation of single character string")
//    void testSingleCharacterString() {
//        permutation("a");
////        assertEqual(7, add(3, 4), "3 + 4 should equal 7");
//    }

//    @Test
//    @DisplayName("Permutations of two-character string")
//    void testTwoCharacterString() {
//        permutation("ab");
////        assertEqual(7, add(3, 4), "3 + 4 should equal 7");
//    }
//
    @Test
    @DisplayName("Permutations of three-character string")
    void testThreeCharacterString() {
        permutation("abc");
//        assertEqual(7, add(3, 4), "3 + 4 should equal 7");
    }
//
//    @Test
//    @DisplayName("Permutations of four-character string")
//    void testFourCharacterString() {
//        permutation("abcd");
////        assertEqual(7, add(3, 4), "3 + 4 should equal 7");
//    }
//
//    @Test
//    @DisplayName("Permutations of five-character string")
//    void testFiveCharacterString() {
//        permutation("abcde");
////        assertEqual(7, add(3, 4), "3 + 4 should equal 7");
//    }
//
//    @Test
//    @DisplayName("Permutations of six-character string")
//    void testSixCharacterString() {
//        permutation("abcdef");
////        assertEqual(7, add(3, 4), "3 + 4 should equal 7");
//    }
//
//    @Test
//    @DisplayName("Permutations of seven-character string")
//    void testSevenCharacterString() {
//        permutation("abcdefg");
////        assertEqual(7, add(3, 4), "3 + 4 should equal 7");
//    }
//@Test
//@DisplayName("Permutations of eight-character string")
//void testSevenCharacterString() {
//    permutation("abcdefgh");
////        assertEqual(7, add(3, 4), "3 + 4 should equal 7");
//}

    // Assertion Helpers
    private void assertEqual(Object expected, Object actual, String message) {
        if (!Objects.equals(expected, actual)) {
            throw new AssertionError(message + "\nExpected: " + expected + "\nActual: " + actual);
        }
    }

    private void assertAlmostEqual(double expected, double actual, double delta, String message) {
        if (Math.abs(expected - actual) > delta) {
            throw new AssertionError(message + "\nExpected: " + expected + "\nActual: " + actual);
        }
    }

    // ---------------------------------------------------
    // Test Runner Logic
    // ---------------------------------------------------

    public static void main(String[] args) {
        System.out.println("🚀 Running self-contained unit tests...");
        runTests(P51.class);
    }

    private static void runTests(Class<?> testClass) {
        int passed = 0;
        int failed = 0;
        long start = System.currentTimeMillis();

        try {
            Object testInstance = testClass.getDeclaredConstructor().newInstance();
            for (Method method : testClass.getDeclaredMethods()) {
                if (method.isAnnotationPresent(Test.class)) {
                    String testName = method.getName();
                    String displayName = method.isAnnotationPresent(DisplayName.class)
                            ? method.getAnnotation(DisplayName.class).value()
                            : testName;
                    try {
                        method.invoke(testInstance);
                        System.out.println("✅ " + displayName);
                        passed++;
                    } catch (InvocationTargetException e) {
                        failed++;
                        Throwable cause = e.getCause();
                        System.err.println("❌ " + displayName + " — " + cause.getMessage());
                    }
                }
            }
        } catch (Exception e) {
            System.err.println("⚠️ Error initializing tests: " + e.getMessage());
        }

        long duration = System.currentTimeMillis() - start;
        System.out.printf("\nSummary: %d passed, %d failed in %d ms%n", passed, failed, duration);
    }
}
