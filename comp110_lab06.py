"""
Module: comp110_lab06

Exercises from lab 06, dealing with string accumualators.
"""

import sound

def repeater(note_name, times):
    """Creates a song that is a note repeated some number of times.

    Args:
        note_name (type: str): The name of the note (e.g. 'C')
        times (type: int): How many times to repeat the note.

    Returns:
        Sound: Song with note_name repeated numerous times.
    """
    song = sound.create_silent_sound(1)
    
    for i in range(times):
        song = song + sound.Note(note_name, 44100)

    return song


def mix_sounds(snd1,snd2):
    """Takes in two sounds and mixes them together to return this new mixed
    sound object.

    Args:
        snd1 (Sound) - original sound object to be mixed with snd2
        snd2 (Sound) - original sound object to be mixed with snd1

    Return:
        sound: mixed sound of snd1 and snd2
    """

    if XXX:
        longer_snd = XXX
        shorter_snd = XXX
    else:
        longer_snd = XXX
        shorter_snd = XXX

    mixed_snd = sound.copy(XXX)
    
    for i in range(len(XXX)):
        mix_sample = XXX[i]
        other_sample = XXX[i]
        mix_sample.left = mix_sample.left + other_sample.left
        mix_sample.right = mix_sample.right + other_sample.right
    
    return XXX


def create_edited_string(text_with_edit_marks):
    """Function that returns a string with editing applied."""

    final_str = ""

    for ch in text_with_edit_marks:
        final_str = final_str + ch

    return final_str



def test_create_edited_string():
    """Function that tests the create_edited_string function.

    DO NOT modify this function in any way.
    """

    # define a list with our test inputs
    test_cases = []
    test_cases.append("String without edit marks")
    test_cases.append("This was !qwicked awesome")
    test_cases.append("Please do not ^make me yell")
    test_cases.append("This is my ^roar!s")
    test_cases.append("You need to _CALM DOWN")
    test_cases.append("You need to _CALM ^down")
    test_cases.append("Please give me some _F!LOOD")
    test_cases.append("Interesting _result")
    test_cases.append("I am !sc!hool")
    test_cases.append("_SHHH!H ^I am trying _to sleep")

    # define a list with the expected results based on inputs
    solutions = []
    solutions.append("String without edit marks")
    solutions.append("This was wicked awesome")
    solutions.append("Please do not MAKE ME YELL")
    solutions.append("This is my ROAR")
    solutions.append("You need to calm down")
    solutions.append("You need to calm DOWN")
    solutions.append("Please give me some food")
    solutions.append("Interesting result")
    solutions.append("I am cool")
    solutions.append("shhh I AM TRYING to sleep")

    num_passed = 0
    num_failed = 0

    for i in range(len(test_cases)):
        # get the input and expected result
        current_test = test_cases[i]
        current_solution = solutions[i]

        # call the function and check the result
        result = create_edited_string(current_test)
        if result != current_solution:
            print("Test", i, "(", current_test, ") FAILED. \n\tExpected Result:", current_solution, "\n\tActual Result:", result)
            num_failed = num_failed + 1
        else:
            print("Test", i, "(", current_test, ") PASSED.\n\tResult:", current_solution)
            num_passed = num_passed + 1

    print("\nTest summary:", num_passed, "case(s) passed,", num_failed, "case(s) failed.")

# Do not modify anything after this point.
if __name__ == "__main__":
    test_create_edited_string()
