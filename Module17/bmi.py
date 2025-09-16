import streamlit as st
from abc import ABC, abstractmethod


class Person(ABC):
    """
    Abstract base class representing a person.
    """

    def __init__(self, name, age, weight, height):
        """
        Initializes a new instance of the Person class.
        """
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        """
        Gets the weight of the person.

        Returns:
            float: The weight of the person.
        """
        return self._weight

    @weight.setter
    def weight(self, value):
        """
        Sets the weight of the person.

        Raises:
            ValueError: If the weight is negative.
        """
        if value < 0:
            raise ValueError("Weight cannot be negative")
        self._weight = value

    @property
    def height(self):
        """
        Gets the height of the person.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the person.

        Raises:
            ValueError: If the height is negative.
        """
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        """
        Calculates the BMI of the person.
        """
        pass

    @abstractmethod
    def get_bmi_category(self):
        """
        Gets the BMI category of the person.
        """
        pass

    def print_info(self):
        """
        Prints the information of the person, including BMI and category.
        """
        st.write(f"{self.name}, Age: {self.age}, Weight: {self.weight} kg, Height: {self.height} m, "
              f"BMI: {self.calculate_bmi():.2f}, Category: {self.get_bmi_category()}")


class Adult(Person):
    """
    Subclass representing an adult person.
    """

    def calculate_bmi(self):
        """
        Calculates the BMI of the adult using the formula weight/(height^2).
        """
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        """
        Gets the BMI category of the adult.
        """
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):
    """
    Subclass representing a child person.
    """

    def calculate_bmi(self):
        """
        Calculates the BMI of the child using the formula weight/(height**2)*1.3
        """
        return (self.weight / (self.height ** 2)) * 1.3

    def get_bmi_category(self):
        """
        Gets the BMI category of the child.
        """
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 24:
            return "Overweight"
        else:
            return "Obese"



st.title("BMI Calculator")

if 'people' not in st.session_state:
    st.session_state['people'] = []

with st.form("person_form"):
    name = st.text_input("Enter name:")
    age = st.number_input("Enter age:", min_value=0, step=1)
    weight = st.number_input("Enter weight in kilograms:", min_value=0.0, format="%.2f")
    height = st.number_input("Enter height in meters:", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Add Person")

    if submitted and name and weight > 0 and height > 0:
        if age >= 18:
            person = Adult(name, age, weight, height)
        else:
            person = Child(name, age, weight, height)
        st.session_state['people'].append(person)
        st.success(f"Added {name}")

if st.session_state['people']:
    st.header("Results")
    for person in st.session_state['people']:
        person.print_info()

    if st.button("Clear All"):
        st.session_state['people'] = []