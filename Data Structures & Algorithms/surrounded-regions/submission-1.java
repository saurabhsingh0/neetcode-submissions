class Solution {
    int rows;
    int cols;
    int[][] moves = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    public void solve(char[][] board) {
        rows = board.length;
        cols = board[0].length;

        //run dfs from every border 1st row and last row
        for(int i=0; i<cols; i++) {
            if(board[0][i] == 'O'){
                dfs(board, 0, i);
            }
            if(board[rows-1][i] == 'O'){
                dfs(board, rows-1, i);
            }
        }

        for(int i=0; i<rows; i++){
            if(board[i][0] == 'O'){
                dfs(board, i, 0);
            }
            if(board[i][cols-1] == 'O'){
                dfs(board, i, cols-1);
            }
        }
        // change the "O"s that are not marked as "S" to "X"s and the "S"s back to "O"s
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == 'S') {
                    board[i][j] = 'O';
                }
            }
        }
    }

    private void dfs(char[][] board, int r, int c) {
        if(r<0 || r>=rows || c<0 || c>=cols || board[r][c] != 'O') {
            return;
        }
        board[r][c] = 'S';
        for(int[] move: moves){
            int newR = r + move[0];
            int newC = c + move[1];
            dfs(board, newR, newC);
        }
    }
}
