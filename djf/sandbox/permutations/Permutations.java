/*
 * Permutations function from Cracking the Coding Interview discussion of big O.
 * Added code to print debugging traces.
 */

// This code counts all permutations of a string.
//

class Permutations
{
    static void permutation(String str) {
        System.out.println( "permutation( " + str + " ):" );
        permutation(str, "", "");
    }

    static void permutation(String str, String prefix, String tag ) {
        tag = tag + "   ";
        System.out.println( tag + "permutation( " + str + ", " + prefix + " )" );
        if (str.length() == 0) {
            System.out.println(prefix);
        } else {
            for (int i= 0; i < str.length(); i++) {
                String rem = str.substring(0, i) + str.substring(i + 1);
                System.out.println( tag + "...moving <" + str.charAt(i)
                    + " from 'str' to 'prefix'" );
                permutation(rem, prefix + str.charAt(i), tag);
            }
        }
     }

    public static void main( String[] args )
    {
        permutation( "abc" );
    }

}

