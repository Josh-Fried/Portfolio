import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class WordSorter {

    public static void main(String[] args) {
        // List<String> words = readWordsFromFile("words.txt");
        List<String> words = new ArrayList<>();

        words.addAll(readWordsFromFile("wordscapesDictionary.txt"));

        // List<String> sortedWords = sortAndRemoveNumbers(words);
        List<String> sortedWords = sortList(words);

        writeSortedWordsToFile(sortedWords, "test.txt");
        //printWords(sortedWords);
    }

    // Read words from the "words.txt" file
    private static List<String> readWordsFromFile(String fileName) {
        List<String> words = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                words.add(line.trim());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return words;
    }

    // Sort words alphabetically and remove numbers at the end
    private static List<String> sortAndRemoveNumbers(List<String> words) {
        List<String> sortedWords = new ArrayList<>();
        for (String word : words) {
            String cleanedWord = word.replaceAll("\\d+$", ""); // Remove numbers at the end
            sortedWords.add(cleanedWord);
        }
        Collections.sort(sortedWords); // Sort the words alphabetically
        return sortedWords;
    }

    // Sort words alphabetically
    private static List<String> sortList(List<String> words){
        List<String> sortedWords = new ArrayList<>();
        for (String word : words) {
            sortedWords.add(word);
        }
        Collections.sort(sortedWords); // Sort the words alphabetically
        return sortedWords;
    }

    // Print the sorted words to the command line
    private static void printWords(List<String> words) {
        for (String word : words) {
            System.out.println(word);
        }
    }
    
    // Write the sorted words to a new file "sortedwords.txt"
    private static void writeSortedWordsToFile(List<String> words, String fileName) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(fileName))) {
            for (String word : words) {
                bw.write(word);
                bw.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
