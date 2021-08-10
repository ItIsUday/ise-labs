package string_handling;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter the sentence: ");
        String str = in.nextLine();
        penultimate(str);
        replace(str);
        substr(str);
    }

    private static void penultimate(String str) {
        String[] arr = str.split(" ");
        System.out.println("Words are: ");
        for (String a : arr)
            System.out.println(a + " ");

        if (arr.length >= 2)
            System.out.println("Penultimate word: " + arr[arr.length - 2]);
        else
            System.out.println("Penultimate word can't be printed");
    }

    private static void replace(String str) {
        System.out.println("Replacing \"Java\" with \"Python\" and \"Python\" with \"Java\"");
        String s = str.replaceAll("Java", "5pmQD9gn46Dm3N").
                replaceAll("Python", "Java").
                replaceAll("5pmQD9gn46Dm3N", "Python");
        System.out.println("New string : " + s);
    }

    private static void substr(String str) {
        Scanner in = new Scanner(System.in);
        String ch;
        System.out.print("Enter character based on which substrings to to be made: ");
        ch = in.nextLine();
        System.out.println("Breaking the sentence into substrings around \"ch\"");
        String[] sub = str.split(ch, 0);
        for (String a : sub)
            System.out.println(a + " ");
    }

}
