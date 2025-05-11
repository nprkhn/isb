import java.util.Random;

public class RandomBinarySequence {
    public static void main(String[] args) {
        int length = 128;
        
        Random random = new Random();
        
        StringBuilder binarySequence = new StringBuilder(length);
        
        for (int i = 0; i < length; i++) {
            int bit = random.nextInt(2);
            binarySequence.append(bit);
        }
        
        System.out.println(binarySequence.toString());
    }
}