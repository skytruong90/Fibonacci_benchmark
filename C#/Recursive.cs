using System;

public class Recursive
{
  public static long FibonacciRecursive(int n)
  {
    if (n <= 1)
    {
      return n;
    }
    return FibonacciRecursive(n - 1) + FibonacciRecursive(n - 2);
  }

  public static void Main()
  {
    // Test points
    int[] testPoints = { 10, 20, 30, 40 };
    int numberOfCycles = 20; // Number of cycles for averaging

    // Iterate over each test point
    foreach (int n in testPoints)
    {
      long totalTime = 0; // Total time for all cycles

      // Run the calculation 20 times to find the average time
      for (int i = 0; i < numberOfCycles; i++)
      {
        var stopwatch = System.Diagnostics.Stopwatch.StartNew();
        FibonacciRecursive(n);
        stopwatch.Stop();
        totalTime += stopwatch.ElapsedTicks;
      }

      double averageTime = totalTime / (double)System.Diagnostics.Stopwatch.Frequency / numberOfCycles; // Average time in seconds
      Console.WriteLine($"Average time taken to compute Fibonacci at position {n}: {averageTime} seconds");
    }
  }
}
