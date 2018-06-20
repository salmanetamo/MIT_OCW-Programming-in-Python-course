# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    
    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    if len(sequence) == 1:
        return list(sequence)
    else:
        sequence = list(sequence)
        held_out_letter = sequence[0]
        del(sequence[0])
        sequence = ''.join(sequence)
        list_to_return = []
        
        for permutation in get_permutations(sequence):
            permutation = list(permutation)
            for i in range(len(permutation)+1):
                permutation.insert(i,held_out_letter)
                permutation = ''.join(permutation)
                list_to_return.append(permutation)
                permutation = list(permutation)
                del(permutation[i])
        return list_to_return

            

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    example_2 = 'cup'
    print('Input:', example_2)
    print('Expected Output:', ['cup', 'ucp', 'upc', 'cpu', 'pcu', 'puc'])
    print('Actual Output:', get_permutations(example_2))

    example_3 = 'hi'
    print('Input:', example_3)
    print('Expected Output:', ['hi', 'ih'])
    print('Actual Output:', get_permutations(example_3))
