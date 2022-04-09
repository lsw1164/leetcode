public class Solution {
    public int MaximalSquare(char[][] matrix) {

        int m = matrix.Length, n = matrix[0].Length;
        var squareMat = new int[m][];
        for (int i = 0; i < m; i++) {
            squareMat[i] = new int[n];
            for (int j = 0; j < n; j++) {
                squareMat[i][j] = matrix[i][j] == '0' ? 0 : -1;
            }
        }

        int MaxSquareLen(int r, int c) {

            if (r < 0 || r >= squareMat.Length || c < 0 || c >= squareMat[0].Length) {
                return 0;
            }

            if (squareMat[r][c] != -1) {
                return squareMat[r][c];
            }

            int minValue = int.MaxValue;
            minValue = Math.Min(minValue, MaxSquareLen(r, c + 1));
            minValue = Math.Min(minValue, MaxSquareLen(r + 1, c));
            minValue = Math.Min(minValue, MaxSquareLen(r + 1, c + 1));
            squareMat[r][c] = minValue + 1;
            return squareMat[r][c];
        }


        int maxLen = int.MinValue;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                maxLen = Math.Max(maxLen, MaxSquareLen(i, j));
            }
        }

        return maxLen * maxLen;
    }
}