package mypack;

import java.util.Scanner;

public class TicTacToe {

    public static String showBoard(int[][] board){
        String boardString = "";
        for(int[] row : board){
            for(int cell : row){
                boardString += cell;
                boardString += " ";
            }
            boardString += "\n";
        }
        return boardString;
    }

    public static void placePiece(int x, int y, int piece, int[][] board){
        board[x][y] = piece;
    }

    public static boolean hasWon(int[][] board){
        for (int i = 0; i < 3; i++){
            int totalRow = 0;
            for (int j = 0; j < 3; j++){
                totalRow += board[i][j];
            }
            if (totalRow == 3 | totalRow == -3){
                return true;
            }

            int totalColumn = 0;
            for (int j = 0; j < 3; j++){
                totalColumn += board[j][i];
            }
            if (totalColumn == 3 | totalColumn == -3){
                return true;
            }
        }
        int totalFirstDiagonal = board[0][0] + board[1][1] + board[2][2];
        if ( totalFirstDiagonal == 3 | totalFirstDiagonal == -3){
            return true;
        }
        int totalSecondDiagonal = board[0][2] + board[1][1] + board[2][0];
        if ( totalSecondDiagonal == 3 | totalSecondDiagonal == -3){
            return true;
        }
        return false;
    }

    public static boolean isValidMove(int x, int y, int[][] board){
        return board[x][y] == 0;
    }
    public static void main(String[] args) {
        int totalMoves = 0;
        int currentPlayer = 1;
        int[][] board = new int[3][3];

        Scanner myScanner = new Scanner(System.in);

        while (!hasWon(board) | totalMoves == 9) {
            System.out.println("El tablero se ve: ");
            System.out.println(showBoard(board));

            System.out.println("Ingrese X de su siguiente pieza");
            int nextX = Integer.parseInt(myScanner.nextLine());
            System.out.println("Ingrese Y de su siguiente pieza");
            int nextY = Integer.parseInt(myScanner.nextLine());

            if (isValidMove(nextX, nextY, board)) {
                placePiece(nextX, nextY, currentPlayer, board);
                currentPlayer *= -1;
                totalMoves += 1;
                System.out.println(showBoard(board));
            } else{
                System.out.println("No es una jugada v_alida");
            }
        }
        if (hasWon(board)){
            System.out.println("Gan_ el jugador: " + currentPlayer);
        }else{
            System.out.println("M_axima cantidad de jugadas posibles");
        }
        myScanner.close();
    }
}