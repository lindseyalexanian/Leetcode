// leetcode 787

public class Solution {
        public int FindCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
            
            // dynamic programming array (array of integers)
            int[] dp = Enumerable.Repeat(int.MaxValue/2, n).ToArray();
            
            // initialize starting point as price of 0
            dp[src] = 0;

            // loop
            for (int x = 0; x <= K; x++) {
                
                // initialize (or re-initialize) placeholder array for price
                int[] placeholder = new int[n];
                
                // copy current dp array into placeholder array
                Array.Copy(dp, placeholder, n);

                // loop through all the flights in the input
                foreach (int[] f in flights) {
                    // if start + price is less than end, send end equal to start + price
                    if (placeholder[f[1]] > dp[f[0]]+f[2])
                        placeholder[f[1]] = dp[f[0]]+f[2];
                }

                // dp array equal to placeholder array
                dp = placeholder;
            }

            
            // if infinity, return -1
            if (dp[dst] == int.MaxValue/2) {
                return -1;
                }
            
            // otherwise, return dp[dst]
            else {
                return dp[dst];
            }
            
            //Console.WriteLine(dp[dst]);
        }
    }