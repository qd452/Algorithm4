package Percolation;

import edu.princeton.cs.algs4.*;

/**
 * Created by dong.qu on 21/4/2016.
 */
public class PercolationStats {
    private double[] fraction;
    private int times;

    /**
     * perform T independent experiments on an N-by-N grid
     *
     * @param N the length of side of the N-by-N grid, T is experment times
     * @throws java.lang.IllegalArgumentException if N <= 0 or T<=0
     */
    public PercolationStats(int N, int T) {
        if (N < 1 || T < 1)
            throw new IllegalArgumentException("N or T is less than 1");     //throws java.lang.IllegalArgumentException if N <= 0 or T<=0
        times = T;
        fraction = new double[T];
        for (int q = 0; q < T; q++) {
            Percolation P = new Percolation(N);
            double count = 0;
            while (!P.percolates()) {
                int i = StdRandom.uniform(1, N + 1);
                int j = StdRandom.uniform(1, N + 1);
                if (!P.isOpen(i, j)) {
                    P.open(i, j);
                    count++;
                }
            }
            fraction[q] = count / (N * N);
        }

    }

    /**
     * sample mean of percolation threshold
     */
    public double mean() {
        return StdStats.mean(fraction);
    }

    /**
     * sample standard deviation of percolation threshold
     */
    public double stddev() {
        return StdStats.stddev(fraction);
    }

    /**
     * low  endpoint of 95% confidence interval
     */
    public double confidenceLo() {
        return mean() - 1.96 * stddev() / Math.sqrt(times);
    }

    /**
     * high endpoint of 95% confidence interval
     */
    public double confidenceHi() {
        return mean() + 1.96 * stddev() / Math.sqrt(times);
    }

    public static void main(String[] args)    // test client (described below)
    {

        int N = StdIn.readInt();
        int T = StdIn.readInt();
        Stopwatch sw = new Stopwatch();
        PercolationStats PS = new PercolationStats(N, T);
        StdOut.println("mean                    = " + PS.mean());
        StdOut.println("stddev                  = " + PS.stddev());
        StdOut.println("95% confidence interval = " + PS.confidenceLo() + " " + PS.confidenceHi());
        StdOut.println(sw.elapsedTime());
    }
}