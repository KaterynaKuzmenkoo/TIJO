from src.math_lib import max, is_perfect

#assert max([None, 1, 2, 3]) == None, "max([None, 1, 2, 3]) zwraca None?"
#assert max([None,None, 2, 3]) == None, "max([None, None, 2, 3]) zwraca None?"

def none_test():
    #Arrange
    numbers = None

    #Act
    result = max(numbers)

    #Assert
    assert numbers is None, "max([None]) zwraca None?"


def empty_test():
    #Arrange
    numbers = []

    #Act
    result = max(numbers)

    #Assert
    assert result is None, "max([]) zwraca None?"

def one_element_test():
    #Arrange
    numbers = [4]

    #Act
    result = max(numbers)

    #Assert
    assert result == 4, "max([4]) zwraca 4?"

def many_elements_test():

    #Arrange
    numbers = [1, 2, 3, 4, 5]

    #Act
    result = max(numbers)

    #Assert
    assert result == 5, "max([1, 2, 3, 4, 5]) zwraca 5?"


#---------- Liczba doskonała ----------

def perfect_test():
    # Arrange
    digit = 28

    #Act
    result = is_perfect(digit)

    # Assert
    assert result == True, "is_perfect(6) zwraca True?"


def not_perfect_test():
    # Arrange
    digit = 1
    # Act
    result = is_perfect(digit)

    # Assert
    assert result == False, "is_perfect(1) zwraca True?"

none_test()
empty_test()
one_element_test()
many_elements_test()
perfect_test()
not_perfect_test()

