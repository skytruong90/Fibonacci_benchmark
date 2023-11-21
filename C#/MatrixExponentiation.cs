using System;

public class MatrixExponentiation
{
  // Function to calculate Fibonacci using matrix exponentiation
  public static long FibonacciMatrix(long n)
  {
    if (n <= 1) return n;

    // Initialize the result matrix as an identity matrix
    long[,] result = { { 1, 0 }, { 0, 1 } };
    // Initialize the Fibonacci matrix
    long[,] fibonacciMatrix = { { 1, 1 }, { 1, 0 } };

    // Perform matrix exponentiation
    while (n > 0)
    {
      if (n % 2 == 1)
      {
        // If n is odd, multiply the result by the Fibonacci matrix
        result = MultiplyMatrices(result, fibonacciMatrix);
      }
      // Divide n by 2 and square the Fibonacci matrix
      n /= 2;
      fibonacciMatrix = MultiplyMatrices(fibonacciMatrix, fibonacciMatrix);
    }

    // The Fibonacci number is in the top right corner of the result matrix
    return result[0, 1];
  }

  // Function to multiply two matrices
  private static long[,] MultiplyMatrices(long[,] a, long[,] b)
  {
    // Initialize the result matrix
    long[,] result = new long[2, 2];

    // Perform matrix multiplication
    for (int i = 0; i < 2; i++)
    {
      for (int j = 0; j < 2; j++)
      {
        result[i, j] = 0;
        for (int k = 0; k < 2; k++)
        {
          result[i, j] += a[i, k] * b[k, j];
        }
      }
    }

    return result;
  }

  public static void Main()
  {
    // Test points
    long[] testPoints = { 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000 };
    int numberOfCycles = 100; // Number of cycles for averaging

    // Iterate over each test point
    foreach (long n in testPoints)
    {
      long totalTime = 0; // Total time for all cycles

      // Run the calculation 100 times to find the average time
      for (int i = 0; i < numberOfCycles; i++)
      {
        var startTime = System.Diagnostics.Stopwatch.StartNew();
        FibonacciMatrix(n);
        startTime.Stop();
        totalTime += startTime.ElapsedTicks;
      }

      // Calculate the average time in seconds
      double averageTime = totalTime / (double)System.Diagnostics.Stopwatch.Frequency / numberOfCycles;
      // Print the average time for the current test point
      Console.WriteLine($"Average time taken to compute Fibonacci at position {n}: {averageTime} seconds");
    }
  }
}
