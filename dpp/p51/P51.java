import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.*;
import java.util.*;

/**
 * Self-contained Java class with inline tests that can run without JUnit.
 * Ideal for demos, quick verification, or environments without JUnit installed.
 */
public class P51 {

    // ---------------------------------------------------
    // Production Code
    // ---------------------------------------------------

    public int add(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b;
    }

    public int multiply(int a, int b) {
        return a * b;
    }

    public double divide(int a, int b) {
        if (b == 0) throw new IllegalArgumentException("Division by zero is not allowed.");
        return (double) a / b;
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

    @Test
    @DisplayName("Addition should return correct result")
    void testAddition() {
        assertEqual(7, add(3, 4), "3 + 4 should equal 7");
    }

    @Test
    @DisplayName("Subtraction should return correct result")
    void testSubtraction() {
        assertEqual(2, subtract(5, 3), "5 - 3 should equal 2");
    }

    @Test
    @DisplayName("Multiplication should return correct result")
    void testMultiplication() {
        assertEqual(15, multiply(3, 5), "3 * 5 should equal 15");
    }

    @Test
    @DisplayName("Division should return correct result")
    void testDivision() {
        assertAlmostEqual(2.5, divide(5, 2), 0.001, "5 / 2 should equal 2.5");
    }

    @Test
    @DisplayName("Division by zero should throw exception")
    void testDivideByZero() {
        try {
            divide(10, 0);
            throw new AssertionError("Expected IllegalArgumentException for division by zero.");
        } catch (IllegalArgumentException e) {
            assertEqual("Division by zero is not allowed.", e.getMessage(), "Exception message should match");
        }
    }

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
