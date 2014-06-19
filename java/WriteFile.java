/**
 * Example to write file using FileOutputStream.
 * FileWriter is similar to Fileoutputstream.
 * 
 * NOTICE
 * Fileoutputstream write bytes to file.
 * Operations to fos need to try-catch.
 *
 * HOW TO RUN
 * javac Writefile
 * java WritFile
 */

import java.io.*;

public class WriteFile{
    public static FileOutputStream fos;
    
    public static final String FILE_NAME="temp.dat";    

    public static void main(String args[]){
        try{
            fos=new FileOutputStream(FILE_NAME);

            String str="Hello World!\n";

            byte[] bytes=str.getBytes(); // convert String to bytes

            fos.write(bytes);

            fos.close();
        } catch(Exception e){
            e.printStackTrace();
        }
    }
}
