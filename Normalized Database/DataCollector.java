import java.io.BufferedReader;
import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.util.LinkedList;

public class DataCollector {
    public static void main(String[] args) throws Exception{

        LinkedList<Integer> majorIDCheck = new LinkedList<>();
        LinkedList<Integer> advisorIDCheck = new LinkedList<>();
        LinkedList<Integer> collegeIDCheck = new LinkedList<>();


        Class.forName("com.mysql.jdbc.Driver");
        Connection connection = DriverManager.getConnection("jdbc:mysql://35.185.192.119:3306/Normalized_Database?useSSL=false", "park240", "Nohacking123");

        BufferedReader br = new BufferedReader(new FileReader("data.csv"));
        String line = "";
        String cvsSplitBy = ",";

        while((line = br.readLine()) != null){

            //student_ID, student_Name, GPA, AdvisorName, Advisor_ID, Major, Major_ID, College, College_ID
            String[] data = line.split(cvsSplitBy);

            int studentID = Integer.parseInt(data[0]);
            String studentName = data[1];
            Float GPA = Float.parseFloat(data[2]);
            String advisorName = data[3];
            int advisorID = Integer.parseInt(data[4]);
            String major = data[5];
            int majorID = Integer.parseInt(data[6]);
            String college = data[7];
            int collegeID = Integer.parseInt(data[8]);

            if (!advisorIDCheck.contains(advisorID))
            {
                advisorIDCheck.add(advisorID);
                //advisor table
                PreparedStatement preparedStatementAdvisor = connection.prepareStatement("INSERT INTO Advisor(Advisor_ID, Advisor_Name) VALUES (?, ?)");
                preparedStatementAdvisor.setInt(1, advisorID);
                preparedStatementAdvisor.setString(2, advisorName);
                preparedStatementAdvisor.executeUpdate();
            }

            //student table
            PreparedStatement preparedStatementStudent = connection.prepareStatement("INSERT INTO Student(Student_ID, Student_Name, GPA, Advisor_ID) VALUES (?,?,?,?)");
            preparedStatementStudent.setInt(1, studentID);
            preparedStatementStudent.setString(2, studentName);
            preparedStatementStudent.setFloat(3, GPA);
            preparedStatementStudent.setInt(4, advisorID);
            preparedStatementStudent.executeUpdate();

            if (!collegeIDCheck.contains(collegeID)){
                collegeIDCheck.add(collegeID);
                //college table
                PreparedStatement preparedStatementCollegeID = connection.prepareStatement("INSERT INTO MajorCollege(College_ID, College) VALUES(?,?)");
                preparedStatementCollegeID.setInt(1, collegeID);
                preparedStatementCollegeID.setString(2, college);
                preparedStatementCollegeID.executeUpdate();
            }

            if (!majorIDCheck.contains(majorID))
            {
                majorIDCheck.add(majorID);
                //major table
                PreparedStatement preparedStatementMajorID = connection.prepareStatement("INSERT INTO Major(Major_ID, Major, College_ID) VALUES(?,?,?)");
                preparedStatementMajorID.setInt(1, majorID);
                preparedStatementMajorID.setString(2, major);
                preparedStatementMajorID.setInt(3, collegeID);
                preparedStatementMajorID.executeUpdate();
            }

            //StudentMajor table
            PreparedStatement preparedStatementStudentMajor = connection.prepareStatement("INSERT INTO StudentMajor(Student_ID, Major_ID) VALUES(?,?)");
            preparedStatementStudentMajor.setInt(1, studentID);
            preparedStatementStudentMajor.setInt(2, majorID);
            preparedStatementStudentMajor.executeUpdate();
        }











    }




}
