
public class calculator {
	
	int firstParam ;
	int secondParam ;
	
	public calculator()
	{
		System.out.println("Inside construtor");
	}
	
	public calculator(int firstParam , int secondParam)
	{
		System.out.println("Inside parameterized construtor");
		this.firstParam = firstParam;
		this.secondParam = secondParam;
	}

	// add method will take x and y arugument    grb
	public int add(int x, int y) {
		System.out.println("Inside construtor");
		return x + y;
	}

	public int substract(calculator c111111111111) {
		int f =c111111111111.firstParam;
		int s = c111111111111.secondParam;
		return f - s;
	}

	public int multiply(int x, int y) {
		x = 6;
		return x * y;
	}

	public int divide(int x, int y) {
		return x / y;

	}
	
	public void getSum(int s)
	{
		System.out.println("sum is -- " + s);
	}

	public static void main(String[] args) {
		//default construtor will be called
		calculator c = new calculator();
		//parameterized construtor will be called 
		calculator c1 = new calculator(2,3);
		
		//add method will be called , with method parameters 
		int sum = c1.add(2, c1.secondParam);
		c1.getSum(sum);
		
		System.out.println(c1.substract(c1));
		System.out.println(c1.multiply(4, 5));
		System.out.println(c1.divide(2, 2));
		c1.add(2,3);
	}
}
