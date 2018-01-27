/****************************************************************************
 * the programming assignment of Algorithms, Part I
 * Week1
 * author: Bill Quan
 ****************************************************************************/
package Percolation;

import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private WeightedQuickUnionUF sites;
    private boolean[] sites_open;
    private int len;

    /**
     * create N-by-N grid, with all sites blocked
     *
     * @param N the length of side of the N-by-N grid
     * @throws java.lang.IllegalArgumentException if N <= 0
     */
    public Percolation(int N)               // 
    {
        if (N < 1)
            throw new IllegalArgumentException("N is less than 1");     //throws java.lang.IllegalArgumentException if N <= 0
        len = N;
        int num = N * N + 2;                    //create N*N+2 ids for UF, among those, id=0 is for the top, id=N^2+1(the last) is for the bottom
        sites = new WeightedQuickUnionUF(num);
        sites_open = new boolean[num];     //all the elements in site_open will be initialize to false automatically
//        for(int p=0; p<num; p++) site_open[p] = false;
    }

    /**
     * open site (row i, column j) if it is not open already, than check the site up/left/down/right to (i,j), if it exists and is open, union it with (i,j)
     *
     * @param i and j is the row and colunm the site in
     * @throws java.lang.IndexOutOfBoundsException if i and j is not between 1 and the length of the gird
     */
    public void open(int i, int j) {
        validate(i, j);
        int id = ij2id(i, j);
        if (sites_open[id])           //if the site is already opened, return
            return;

        sites_open[id] = true;
        //check the site upward
        if (i == 1)                         // if the site is in the first row, union it to the top
        {
            sites.union(id, 0);
        } else                               // else, check the site upward, if the site upward is open, union this two sites
        {
            int upid = (i - 2) * len + j;
            if (sites_open[upid])
                sites.union(id, upid);
        }

        //check the site left
        if (j > 1)                         // if the site has a left site, union this two site if the site left is open
        {
            int leftid = id - 1;
            if (sites_open[leftid])
                sites.union(id, leftid);
        }

        //check the site down
        if (i == len)                      // if the site is in the last row, union it to the bottom
        {
            sites.union(id, len * len + 1);
        } else {
            int downid = i * len + j;
            if (sites_open[downid])
                sites.union(id, downid);
        }

        //check the site right
        if (j < len)                         // if the site has a right site, union this two site if the site right is open
        {
            int rightid = id + 1;
            if (sites_open[rightid])
                sites.union(id, rightid);
        }

    }

    /**
     * check whether the site (row i, column j) is open or not
     *
     * @param i and j is the row and colunm the site in
     * @throws java.lang.IndexOutOfBoundsException if i and j is not between 1 and the length of the gird
     */
    public boolean isOpen(int i, int j) {
        validate(i, j);
        return sites_open[ij2id(i, j)];
    }

    /**
     * check whether the site (row i, column j) is full (connected to the top) or not
     *
     * @param i and j is the row and colunm the site in
     * @throws java.lang.IndexOutOfBoundsException if i and j is not between 1 and the length of the gird
     */
    public boolean isFull(int i, int j)     // is site (row i, column j) full?
    {
        validate(i, j);
        return sites.connected(ij2id(i, j), 0);
    }

    /**
     * check whether the system percolates (the top is connected to the bottom) or not
     */
    public boolean percolates() {
        return sites.connected(0, len * len + 1);
    }


    //turn the (row i, column j) to the id in the sites
    private int ij2id(int i, int j) {
        return (i - 1) * len + j;
    }

    //validate the (row i, column j) is in the grid
    private void validate(int i, int j) {
        if (i < 1 || i > len || j < 1 || j > len)
            throw new IndexOutOfBoundsException("the row or column is not between 1 and " + len);
    }

    public static void main(String[] args)   // test client (optional)
    {
//        Percolation P = new Percolation(3);
//        P.open(1,1);
//        P.open(2,2);
//        P.open(3,3);
//        P.open(1,2);
//        P.open(2,3);
//        for(int i=1; i<4; i++)
//            for(int j=1; j<4; j++)
//            {
//                 StdOut.println("(" + i + "," + j + ") Open: " + P.isOpen(i,j) + "   Full: " + P.isFull(i,j));
//            }
//        
//        StdOut.println("isPercolate:  " + P.percolates());
    }
}