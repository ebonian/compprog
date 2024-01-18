import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class TestFile {
    public static void main(String[] args) {
        TestFile testApp = new TestFile();

        HashMap<String, int[]> allScores = testApp.readScoresFromFile("./data/student_scores.csv");
        printAllScores(allScores);

        String studentIDToLookup = "6632462421";
        int totalScore = testApp.getTotalScore(allScores, studentIDToLookup);
        printTotalScore(studentIDToLookup, totalScore);

        HashSet<String> editedStudentIDs = testApp.getEditedStudentIDs("./data/edited_scores.csv");
        printEditedStudentIDs(editedStudentIDs);

        testApp.createNewEditedScore("./data/student_scores.csv", "./data/edited_scores.csv", "./data/new_scores.csv");
        System.out.println("New scores have been written to 'new_scores.csv'.");
    }

    public HashMap<String, int[]> readScoresFromFile(String filePath) {
        HashMap<String, int[]> scores = new HashMap<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            reader.readLine();
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                String studentId = parts[0];
                int[] scoreArray = Arrays.stream(parts, 1, parts.length)
                        .mapToInt(Integer::parseInt)
                        .toArray();
                scores.put(studentId, scoreArray);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return scores;
    }

    public int getTotalScore(HashMap<String, int[]> scores, String studentId) {
        return scores.getOrDefault(studentId, new int[0]).length > 0 ? Arrays.stream(scores.get(studentId)).sum() : -1;
    }

    public HashSet<String> getEditedStudentIDs(String filePath) {
        HashSet<String> editedStudentIDs = new HashSet<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            reader.readLine();
            String line;
            while ((line = reader.readLine()) != null) {
                editedStudentIDs.add(line.split(",")[0]);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return editedStudentIDs;
    }

    public void createNewEditedScore(String originalFilePath, String editedFilePath, String newFilePath) {
        HashMap<String, int[]> originalScores = readScoresFromFile(originalFilePath);

        try (BufferedReader reader = new BufferedReader(new FileReader(editedFilePath));
                PrintWriter writer = new PrintWriter(new File(newFilePath))) {

            writer.println("ID,Quiz1,Quiz2,Quiz3,Quiz4,Quiz5");

            reader.readLine();
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                String studentId = parts[0];
                int quizIndex = Integer.parseInt(parts[1].replace("Quiz", "")) - 1;
                int newScore = Integer.parseInt(parts[2]);

                int[] scores = originalScores.get(studentId);
                if (scores != null && quizIndex >= 0 && quizIndex < scores.length) {
                    scores[quizIndex] = newScore;
                }
            }

            for (Map.Entry<String, int[]> entry : originalScores.entrySet()) {
                String studentId = entry.getKey();
                int[] scores = entry.getValue();
                String joinedScores = Arrays.stream(scores)
                        .mapToObj(String::valueOf)
                        .collect(Collectors.joining(","));
                writer.println(studentId + "," + joinedScores);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void printAllScores(HashMap<String, int[]> scores) {
        System.out.println("All Scores:");
        scores.forEach((studentID, scoreArray) -> System.out.println(studentID + " - " + Arrays.toString(scoreArray)));
    }

    private static void printTotalScore(String studentID, int totalScore) {
        if (totalScore != -1) {
            System.out.println("Total Score for " + studentID + ": " + totalScore);
        } else {
            System.out.println("Student not found.");
        }
    }

    private static void printEditedStudentIDs(HashSet<String> editedStudentIDs) {
        System.out.println("Edited Student IDs: " + editedStudentIDs);
    }
}
