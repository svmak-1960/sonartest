public class sonarQube03 {
    int calcNumbers(int start, int count){
        int accumulator = start;
        while(count > 0){
            accumulator = accumulator + start;
        }
        return accumulator;
    }
}
