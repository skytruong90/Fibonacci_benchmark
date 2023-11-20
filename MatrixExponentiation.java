public class MatrixExponentiation {

    // Function to calculate Fibonacci using matrix exponentiation
    public static long fibonacciMatrix(int n) {
        if (n <= 1) return n;

        // Initialize the result matrix as an identity matrix
        long[][] result = {{1, 0}, {0, 1}};
        // Initialize the Fibonacci matrix
        long[][] fibonacciMatrix = {{1, 1}, {1, 0}};

        // Perform matrix exponentiation
        while (n > 0) {
            if (n % 2 == 1) {
                // If n is odd, multiply the result by the Fibonacci matrix
                result = multiplyMatrices(result, fibonacciMatrix);
            }
            // Divide n by 2 and square the Fibonacci matrix
            n /= 2;
            fibonacciMatrix = multiplyMatrices(fibonacciMatrix, fibonacciMatrix);
        }

        // The Fibonacci number is in the top right corner of the result matrix
        return result[0][1];
    }

    // Function to multiply two matrices
    private static long[][] multiplyMatrices(long[][] a, long[][] b) {
        // Initialize the result matrix
        long[][] result = new long[2][2];

        // Perform matrix multiplication
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                result[i][j] = 0;
                for (int k = 0; k < 2; k++) {
                    result[i][j] += a[i][k] * b[k][j];
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        // Test points
        int[] testPoints = {10, 100, 1000, 10000, 100000, 1000000};
        int numberOfCycles = 100; // Number of cycles for averaging

        // Iterate over each test point
        for (int n : testPoints) {
            long totalTime = 0; // Total time for all cycles

            // Run the calculation 100 times to find the average time
            for (int i = 0; i < numberOfCycles; i++) {
                long startTime = System.nanoTime();
                fibonacciMatrix(n);
                long endTime = System.nanoTime();
                totalTime += (endTime - startTime);
            }

            // Calculate the average time in seconds
            double averageTime = totalTime / 1e9 / numberOfCycles;
            // Print the average time for the current test point
            System.out.println("Average time taken to compute Fibonacci at position " + n + ": " + averageTime + " seconds");
        }
    }
}
