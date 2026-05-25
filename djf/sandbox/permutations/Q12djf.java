/**
 * I meant this to cycle through all permutations.  It doesn't.
 * It cycles through all combinations.  It doesn't ensure that
 * each value is selected by exactly one digit!
 * Hmmm.
 **/




public class Q12djf
{
    boolean silent = false;

    class Digit
    {
        private String values;
        private int valueIndex;
        private int nValues = 0;
        private boolean carry = false;

        public Digit()
        {
        }

        public Digit( String vals, int i )
        {
            values = vals;
            nValues = vals.length();
            valueIndex = 0;
            if (i >= 0 && i < nValues) {
                valueIndex = i;
            }
        }

        public char getValue() 
        {
            return values.charAt( valueIndex );
        }

        public void setValue( char val )
        {
            int i = 0;
            while (i < nValues && values.charAt( i ) != val) {
                i++;
            }
            if (i < nValues) {
                valueIndex = i;
            }
        }

        public boolean getCarry() {
            return carry;
        }

        public void printValue()
        {
            System.out.print( values.charAt( valueIndex ) );
        }

        public void increment()
        {
            valueIndex++;
            if (valueIndex == nValues) {
                valueIndex = 0;
                carry = true;
            }
            else {
                carry = false;
            }
        }
    }

    public String getConfiguration( Digit[] digits )
    {
        StringBuffer sb = new StringBuffer();
        sb.append( "<" );
        for (int i = 0; i < digits.length; i++) {
            sb.append( digits[ i ].getValue() );
        }
        sb.append( ">" );
        return sb.toString();
    }

    void permutation(String inStr)
    {
        int n = inStr.length();

        // Set initial "number" to be, e.g., abcdef for e.g., n == 6
        Digit[] digits = new Digit[ n ];
        for (int i = 0; i < n; i++)
        {
            digits[ i ] = new Digit( inStr, 0 );
        }

        // System.out.println( "Ready." );

        // "Count" through all permutations, with a carry.
        int last = n - 1;
        boolean done = false;
        while (!done)
        {
            // System.out.println( "    LOOP!" );
            if ( !silent ) {
                System.out.println( "    " + getConfiguration( digits ) );
            }

            int i = last;
            digits[ i ].increment();
            boolean carry = digits[ i ].getCarry();

            // process carries
            while ( (i > 0 ) && carry ) {
                // System.out.println( "    digit " + i + ": "
                //         + digits[i].getValue() + " with carry = "
                //         + digits[i].getCarry() );
                i--;
                digits[ i ].increment();
                carry = digits[ i ].getCarry();

                // System.out.println( "    now:  " + i + ": "
                //         + digits[i].getValue() + " with carry = "
                //         + digits[i].getCarry() );
            }

            if ( (i == 0) && carry ) {
                done = true;
            }
        }
    }

    public static void main( String[] args )
    {
        String ALPHABET = "abcdefghijklmnopqrstuvwxyz";
        int n = 2;

        // Process arguments: optional "n", then optional "silent"
        int last = args.length - 1;
        if ( last >= 0 ) {
            try {
                // Look for a numerical argument
                int arg = Integer.parseInt( args[0] );
                if (arg > 0 && arg <= ALPHABET.length() ) {
                    n = arg;
                }
            } catch (NumberFormatException e) {
                ;
            }
        }

        String inString = ALPHABET.substring( 0, n );
        System.out.println( "Requested permutations of \""
                            + inString + "\" :\n" );
        Q12djf runner = new Q12djf();
        if ( last >= 0 ) {
            if ( "silent".equals( args[ last ] ) ) {
                runner.silent = true;
            }
        }
        runner.permutation( inString );

    }
}
