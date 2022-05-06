class People:
    """People class.

    Returns:
        People: People instance.
    """
    population = 0

    def __init__(self) -> None:
        """ 
        Creates an instance of the People class. 
        """
        People.population += 1
        self.name = ''
        self.age = None
        self.address = ''
        self.favorite_color = ''

    def __repr__(self) -> str:
        """Defines the representation of the object. 

        Returns:
            str: Representation of the object.
        """
        return f"My name is {self.name}"

    def set_name(self, name) -> None:
        """Set's the name of the People Instance.

        Args:
            name (str): Name of the Person.
        """
        self.name = name

    def get_name(self) -> str:
        """Returns the name of the instance.

        Returns:
            str: Name of the Person.
        """
        return self.name


henny = People()
henny.set_name('Henny')
print(henny)  # 'My name is Henny'
print(People.population)  # 1
