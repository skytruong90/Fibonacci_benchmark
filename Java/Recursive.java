public class Recursive {

    public static long fibonacciRecursive(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
    }

    public static void main(String[] args) {
        // Test points 
        int[] testPoints = {10, 20, 30, 40};
        int numberOfCycles = 20; // Number of cycles for averaging

        // Iterate over each test point
        for (int n : testPoints) {
            long totalTime = 0; // Total time for all cycles

            // Run the calculation 20 times to find the average time
            for (int i = 0; i < numberOfCycles; i++) {
                long startTime = System.nanoTime();
                fibonacciRecursive(n);
                long endTime = System.nanoTime();
                totalTime += (endTime - startTime);
            }

            double averageTime = totalTime / 1_000_000_000.0 / numberOfCycles; // Average time in seconds
            System.out.println("Average time taken to compute Fibonacci at position " + n + ": " + averageTime + " seconds");
        }
    }
}
