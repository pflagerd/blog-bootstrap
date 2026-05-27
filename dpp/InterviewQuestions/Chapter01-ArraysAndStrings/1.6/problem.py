
import unittest

def stringCompression(string):
    return compressStringA(string)

# finite state machine
def compressStringA(string):
    EOT = chr(4)

    characterCount = 0
    outputString = ""
    originalString = string
    previousCharacter = chr(0)

    def initialState(character):
        nonlocal previousCharacter
        nonlocal characterCount
        nonlocal currentState

        if character == EOT:
            finalState(character)

        previousCharacter = character
        characterCount = 1
        currentState = foundCurrentCharacter

    def finalState(character):
        if len(outputString) < len(originalString):
            return outputString
        else:
            return originalString

    def foundCurrentCharacter(character):
        nonlocal previousCharacter
        nonlocal characterCount
        nonlocal currentState
        nonlocal originalString
        nonlocal outputString

        if character == EOT:
            outputString += str(previousCharacter) + str(characterCount)
            currentState = finalState
            if len(outputString) < len(originalString):
                return outputString
            else:
                return originalString

        if character == previousCharacter:
            characterCount += 1
        else:
            outputString += str(previousCharacter) + str(characterCount)
            characterCount = 1
            previousCharacter = character


    currentState = initialState

    for character in string:
        currentState(character)
    return currentState(EOT)




def finiteStateAutomaton(string):
    EOT = chr(4)

    def initialState(character):
        pass

    currentState = initialState

    for character in string:
        currentState(character)
    currentState(EOT)


class StringCompression(unittest.TestCase):
    def test_1(self):
       self.assertEqual( "a2b1c5a3", stringCompression("aabcccccaaa"))

    def test_2(self):
       self.assertEqual("abcdef", stringCompression("abcdef"))


if __name__ == "__main__":
    unittest.main()
