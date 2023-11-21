using System;
using System.Collections.Generic;

public class Memoized
{
  private static Dictionary<int, long> memo = new Dictionary<int, long>();

  public static long FibonacciMemoized(int n)
  {
    if (n <= 1)
    {
      return n;
    }

    // Check if the value is already computed
    if (!memo.ContainsKey(n))
    {
      memo[n] = FibonacciMemoized(n - 1) + FibonacciMemoized(n - 2);
    }

    return memo[n];
  }

  public static void Main()
  {
    // Test points
    int[] testPoints = { 10, 100, 500, 1000 };
    int numberOfCycles = 5; // Number of cycles for averaging

    // Iterate over each test point
    foreach (int n in testPoints)
    {
      long totalTime = 0; // Total time for all cycles

      // Run the calculation 5 times to find the average time
      for (int i = 0; i < numberOfCycles; i++)
      {
        var stopwatch = System.Diagnostics.Stopwatch.StartNew();
        FibonacciMemoized(n);
        stopwatch.Stop();
        totalTime += stopwatch.ElapsedTicks;
        // Clear memoization cache for the next run
        memo.Clear();
      }

      double averageTime = totalTime / (double)System.Diagnostics.Stopwatch.Frequency / numberOfCycles; // Average time in seconds
      Console.WriteLine($"Average time taken to compute Fibonacci at position {n}: {averageTime} seconds");
    }
  }
}
