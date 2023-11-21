public class ClosedForm {

    // Method to compute Fibonacci using the closed-form formula
    public static long fibonacciClosedForm(int n) {
        double sqrt5 = Math.sqrt(5);             // Calculate the square root of 5
        double phi = (1 + sqrt5) / 2;           // Calculate the golden ratio (phi)
        return Math.round(Math.pow(phi, n) / sqrt5);  // Use the closed-form formula to calculate Fibonacci
    }

    public static void main(String[] args) {
        // Test points
        long[] testPoints = {10L, 100L, 1_000L, 10_000L, 100_000L, 1_000_000L, 10_000_000L,
                100_000_000L, 1_000_000_000L, 10_000_000_000L, 100_000_000_000L};
        int numberOfCycles = 100; // Number of cycles for averaging

        // Iterate over each test point
        for (long n : testPoints) {
            long totalTime = 0; // Total time for all cycles

            // Run the calculation 100 times to find the average time
            for (int i = 0; i < numberOfCycles; i++) {
                long startTime = System.nanoTime(); // Record start time
                fibonacciClosedForm((int) n);             // Calculate Fibonacci using closed-form
                long endTime = System.nanoTime();   // Record end time
                totalTime += (endTime - startTime); // Calculate time taken for one iteration
            }

            // Calculate the average time in seconds
            double averageTime = totalTime / 1_000_000_000.0 / numberOfCycles;

            // Print the result
            System.out.println("Average time taken to compute Fibonacci at position " + n + ": " + averageTime + " seconds");
        }
    }
}
