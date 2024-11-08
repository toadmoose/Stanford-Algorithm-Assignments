import java.math.BigInteger;

public class KaratsubaMultiplication {

    // Karatsuba multiplication function
    public static BigInteger karatsuba(BigInteger x, BigInteger y) {
        int N = Math.max(x.bitLength(), y.bitLength());
        
        // Base case: when numbers are small enough to be handled directly
        if (N <= 64) {
            return x.multiply(y);  // Standard multiplication for small numbers
        }

        // Number of bits divided by 2, rounded up
        N = (N / 2) + (N % 2);
        
        // x = a + 2^N * b, y = c + 2^N * d
        BigInteger b = x.shiftRight(N);
        BigInteger a = x.subtract(b.shiftLeft(N));
        BigInteger d = y.shiftRight(N);
        BigInteger c = y.subtract(d.shiftLeft(N));

        // Compute the three products using recursion
        BigInteger ac = karatsuba(a, c);
        BigInteger bd = karatsuba(b, d);
        BigInteger abcd = karatsuba(a.add(b), c.add(d));

        // Karatsuba's trick: ac + bd + (abcd - ac - bd) * 2^N
        BigInteger adbc = abcd.subtract(ac).subtract(bd);

        return ac.add(adbc.shiftLeft(N)).add(bd.shiftLeft(2 * N));
    }

    public static void main(String[] args) {
        // Input numbers as strings
        String num1 = "3141592653589793238462643383279502884197169399375105820974944592";
        String num2 = "2718281828459045235360287471352662497757247093699959574966967627";

        // Convert to BigInteger
        BigInteger x = new BigInteger(num1);
        BigInteger y = new BigInteger(num2);

        // Multiply using Karatsuba
        BigInteger result = karatsuba(x, y);

        // Print the result
        System.out.println(result);
    }
}
