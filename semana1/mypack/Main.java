package mypack;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {
    public static int[][] addNumber(int x, int y, int[][] board, int number){
        int[][] newBoard = board;
        newBoard[y][x] = number;
        return newBoard;
    }

    public static String printBoard(int[][] board){
        String boardString = "";
        for (int[] row : board){
            for (int cell : row){
                boardString += cell;
                boardString += " ";
            }
            boardString += "\n";
        }
        return boardString;
    }

    public static boolean isValidMove(int[][] board, int x, int y, int previousX, int previousY){
        System.out.println("Checking " + x + y + previousX + previousY);
        if (board[y][x] != 0 | (x == previousX && y == previousY)){
            return false;
        }
        if (x == previousX | y == previousY){
            return true;
        }
        return false;
    }

    public static boolean isDone(int[][] board, int x, int y){
        for (int i = 0; i < 6; i++){
            if (i == y){
                for (int cell: board[i]){
                    if (cell == 0){
                        return false;
                    }
                }
            }
            if (board[i][x] == 0){
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        List<List<Integer>> mainList = Arrays.asList(
            Arrays.asList(1, 2, 3),
            Arrays.asList(4, 5, 6), 
            Arrays.asList(7, 8, 9)
        );
        var array = mainList.stream().map(number -> Collections.max(number)).mapToInt(Integer::intValue).sum();
        System.out.println(array);

        Scanner myScanner = new Scanner(System.in);

        boolean hasWon = false;
        int currentNumber = 1;
        boolean player = true;
        int board[][] = new int[6][6];
        int previousX = 0;
        int previousY = 0;

        while (!hasWon) {
            System.out.println("Turno del jugador: " + (player ? "A" : "B"));
            System.out.println("Jugada anterior: " + previousX + " " + previousY);
            System.out.println("Ingresa tu jugada");
            System.out.println("X");
            Integer newX = Integer.parseInt(myScanner.nextLine());
            System.out.println("Y");
            Integer newY = Integer.parseInt(myScanner.nextLine());

            if (isValidMove(board, newX, newY, previousX, previousY) | currentNumber == 1){
                System.out.println("Jugada realizada correctamente");
                addNumber(newX, newY, board, currentNumber);
                previousX = newX;
                previousY = newY;
                currentNumber++;
                player = !player;
                hasWon = isDone(board, previousX, previousY);
            } else {
                System.out.println("Jugada invalida");
            }
            System.out.println("El tablero se ve as_:");
            System.out.println(printBoard(board));
        }
        System.out.println("Ha ganado el jugador" + !player);
        myScanner.close();
    }
}