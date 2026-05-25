class Q12
{
    boolean silent = false;

    void permutation(String str)
    {
        permutation(str, "");
    }

    void permutation(String str, String prefix)
    {
        if (str.length() == 0) {
            if ( !silent ) {
                System.out.println(prefix);
            }
        } else {
            for (int i= 0; i < str.length(); i++) {
                String rem = str.substring(0, i) + str.substring(i + 1);
                permutation(rem, prefix + str.charAt(i));
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
        Q12 runner = new Q12();
        if ( last >= 0 ) {
            if ( "silent".equals( args[ last ] ) ) {
                runner.silent = true;
            }
        }
        runner.permutation( inString );

    }
}
