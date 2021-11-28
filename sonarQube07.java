public class sonarQube07 {
    public int calcSum(int lastNum) {
        int result = 0
        int j = 0;
        int i;
        for(i = 0; i < lastNum; i++){
            j++;
            result += j;
        }
        return result;
    }
}
