package collections;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> arrayList = new ArrayList<>();
        System.out.println("Arraylist before adding colors: " + arrayList);

        arrayList.add("Red");
        arrayList.add("Green");
        arrayList.add("Blue");
        System.out.println("Arraylist after adding colors: " + arrayList);

        List<String> list = new ArrayList<>();
        list.add("Orange");
        list.add("Violet");
        list.add("Yellow");

        System.out.print("Adding list " + list + " to list " + arrayList);
        arrayList.addAll(list);
        System.out.println(" gives " + arrayList);

        System.out.print("Copying list " + arrayList + " to an array");
        String[] arr = new String[arrayList.size()];
        arr = arrayList.toArray(arr);
        System.out.print(" gives ");
        System.out.println(Arrays.toString(arr));

        System.out.print("Reversing the array list gives ");
        Collections.reverse(arrayList);
        System.out.println(arrayList);

        List<String> list2 = arrayList.subList(1, 4);
        System.out.println("Sublist of " + arrayList + " from index 1 to 4 is " + list2);
        Collections.sort(arrayList);

        System.out.println("Sorted array list is " + arrayList);
        ArrayList<String> arrayList2 = (ArrayList<String>) arrayList.clone();
        System.out.println("Cloned array list is " + arrayList2);
    }
}
