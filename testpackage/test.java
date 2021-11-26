package testpackage;

public class TestClass{
    private int x;
    private int y;
    
    int getX() {
        return x;
    }
    void setX(int val){
        x = val;
    }
    
    int getY() {
        return y;
    }
    void setY(int val){
        y = val;
    }
        
    
    String addHeader(String stringToAdd){
        return String.format("Added Header %s %d %d", stringToAdd, x, y);
    }
}
