using System;

public class ClosedForm
{
  // Method to compute Fibonacci using the closed-form formula (Binet's formula)
  public static long FibonacciClosedForm(int n)
  {
    double sqrt5 = Math.Sqrt(5);          // Calculate the square root of 5
    double phi = (1 + sqrt5) / 2;         // Calculate the golden ratio (phi)
    return (long)Math.Round(Math.Pow(phi, n) / sqrt5);  // Use the closed-form formula to calculate Fibonacci
  }

  public static void Main(string[] args)
  {
    // Test points
    long[] testPoints = {10L, 100L, 1_000L, 10_000L, 100_000L, 1_000_000L, 10_000_000L,
                             100_000_000L, 1_000_000_000L, 10_000_000_000L, 100_000_000_000L};
    int numberOfCycles = 100; // Number of cycles for averaging

    // Iterate over each test point
    foreach (long n in testPoints)
    {
      long totalTime = 0; // Total time for all cycles
      var stopwatch = new System.Diagnostics.Stopwatch();

      // Run the calculation 100 times to find the average time
      for (int i = 0; i < numberOfCycles; i++)
      {
        stopwatch.Start(); // Start the stopwatch
        FibonacciClosedForm((int)n); // Calculate Fibonacci using closed-form
        stopwatch.Stop(); // Stop the stopwatch

        totalTime += stopwatch.ElapsedTicks;
        stopwatch.Reset(); // Reset the stopwatch for the next iteration
      }

      // Calculate the average time in ticks and convert to seconds
      double averageTime = totalTime / (double)System.Diagnostics.Stopwatch.Frequency / numberOfCycles;

      // Print the result
      Console.WriteLine($"Average time taken to compute Fibonacci at position {n}: {averageTime} seconds");
    }
  }
}
