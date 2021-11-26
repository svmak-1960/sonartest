public class sonarQube03 {
    int calcNumbers(int start){
        int accumulator = start;
        int count = 10;
        while(count > 0){
            accumulator = accumulator + start;
        }
        return accumulator;
    }
}
