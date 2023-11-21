//this is used to handle large numbers without overflow
import java.math.BigInteger;

// Name the class Loop because it uses the loop algorithm for Fibonacci numbers.
public class Loop {

    // Method to calculate the nth Fibonacci number using an iterative loop.
    public static BigInteger fibonacciLoop(int n) {
        // Base case: Return n for the first two numbers in the Fibonacci sequence.
        if (n <= 1) return BigInteger.valueOf(n);

        // Initialize the first two Fibonacci numbers.
        BigInteger fib = BigInteger.ONE;
        BigInteger prevFib = BigInteger.ONE;

        // Loop from the third Fibonacci number up to the nth.
        for (int i = 2; i < n; i++) {
            // Temporary variable to hold the previous Fibonacci number during update.
            BigInteger temp = fib;
            // Calculate the new Fibonacci number by adding the two previous numbers.
            fib = fib.add(prevFib);
            // Update the previous Fibonacci number to the former current Fibonacci number.
            prevFib = temp;
        }

        // Return the nth Fibonacci number.
        return fib;
    }

    // Entry point of the program.
    public static void main(String[] args) {
        // Array containing the specific points at which to test the Fibonacci function.
        int[] testPoints = {10, 100, 1_000, 10_000, 100_000, 500_000};
        int numberOfRuns = 20; // Number of runs to calculate the average time.

        // Iterate over each test point.
        for (int n : testPoints) {
            long totalDuration = 0; // Sum of durations for all runs.

            // Run the Fibonacci calculation 100 times to find the average execution time.
            for (int run = 0; run < numberOfRuns; run++) {
                long startTime = System.nanoTime();
                fibonacciLoop(n); // Compute the Fibonacci number at position n.
                long endTime = System.nanoTime();
                totalDuration += (endTime - startTime); // Accumulate the duration of each run.
            }

            // Calculate the average duration in nanoseconds, then convert to seconds.
            double averageDurationInSeconds = (totalDuration / (double) numberOfRuns) / 1_000_000_000.0;

            // Print out the average time taken to compute the Fibonacci number at the current test point.
            System.out.println("Average time taken to compute Fibonacci at position " + n + ": " + averageDurationInSeconds + " seconds");
        }
    }
}
