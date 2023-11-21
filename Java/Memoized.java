import java.util.HashMap;
import java.util.Map;

public class Memoized {

    private static Map<Integer, Long> memo = new HashMap<>();

    public static long fibonacciMemoized(int n) {
        if (n <= 1) {
            return n;
        }
        // Check if the value is already computed
        if (!memo.containsKey(n)) {
            memo.put(n, fibonacciMemoized(n - 1) + fibonacciMemoized(n - 2));
        }
        return memo.get(n);
    }

    public static void main(String[] args) {
        // Test points
        int[] testPoints = {10, 100, 500, 1_000};
        int numberOfCycles = 5; // Number of cycles for averaging

        // Iterate over each test point
        for (int n : testPoints) {
            long totalTime = 0; // Total time for all cycles

            // Run the calculation 5 times to find the average time
            for (int i = 0; i < numberOfCycles; i++) {
                long startTime = System.nanoTime();
                fibonacciMemoized(n);
                long endTime = System.nanoTime();
                totalTime += (endTime - startTime);
                // Clear memoization cache for the next run
                memo.clear();
            }

            double averageTime = totalTime / 1_000_000_000.0 / numberOfCycles; // Average time in seconds
            System.out.println("Average time taken to compute Fibonacci at position " + n + ": " + averageTime + " seconds");
        }
    }
}