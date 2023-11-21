using System;
using System.Numerics;

public class Loop
{
  // Method to calculate the nth Fibonacci number using an iterative loop.
  public static BigInteger FibonacciLoop(int n)
  {
    // Base case: Return n for the first two numbers in the Fibonacci sequence.
    if (n <= 1) return new BigInteger(n);

    // Initialize the first two Fibonacci numbers.
    BigInteger fib = BigInteger.One;
    BigInteger prevFib = BigInteger.One;

    // Loop from the third Fibonacci number up to the nth.
    for (int i = 2; i < n; i++)
    {
      // Temporary variable to hold the previous Fibonacci number during update.
      BigInteger temp = fib;
      // Calculate the new Fibonacci number by adding the two previous numbers.
      fib += prevFib;
      // Update the previous Fibonacci number to the former current Fibonacci number.
      prevFib = temp;
    }

    // Return the nth Fibonacci number.
    return fib;
  }

  // Entry point of the program.
  public static void Main()
  {
    // Array containing the specific points at which to test the Fibonacci function.
    int[] testPoints = { 10, 100, 1000, 10000, 100000, 500000 };
    int numberOfRuns = 20; // Number of runs to calculate the average time.

    // Iterate over each test point.
    foreach (int n in testPoints)
    {
      long totalDuration = 0; // Sum of durations for all runs.

      // Run the Fibonacci calculation 20 times to find the average execution time.
      for (int run = 0; run < numberOfRuns; run++)
      {
        var stopwatch = System.Diagnostics.Stopwatch.StartNew();
        FibonacciLoop(n); // Compute the Fibonacci number at position n.
        stopwatch.Stop();
        totalDuration += stopwatch.ElapsedTicks; // Accumulate the duration of each run.
      }

      // Calculate the average duration in ticks, then convert to seconds.
      double averageDurationInSeconds = (totalDuration / (double)numberOfRuns) / System.Diagnostics.Stopwatch.Frequency;

      // Print out the average time taken to compute the Fibonacci number at the current test point.
      Console.WriteLine($"Average time taken to compute Fibonacci at position {n}: {averageDurationInSeconds} seconds");
    }
  }
}
