
# * DESCRIPTOR CLASS

class  Parent:
    def __init__(self, child_name, father_name, mother_name):
        self.child_name = child_name
        self.father_name = father_name
        self.mother_name = mother_name


    @property
    def child_name(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        try:
            return self._child_name
        except:
            print("no has attr name")

    @child_name.setter
    def child_name(self, child_name):
        if 0 < len(child_name) < 15:
            self._child_name = child_name
        else:
            raise ValueError(f"Invalid value")
    
    @child_name.deleter
    def child_name(self):
        print("Deleting...")
        del self._child_name


    #* FRO FATHER
    @property
    def father_name(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        try:
            return self._father_name
        except:
            print("no has attr name")

    @child_name.setter
    def father_name(self, father_name):
        if 0 < len(father_name) < 15:
            self._father_name = father_name
        else:
            raise ValueError(f"Invalid value")
    
    @child_name.deleter
    def father_name(self):
        print("Deleting...")
        del self._father_name


p = Parent("raza", "ali", "nada")

p.child_name = "asgar"


# ---

class NameField:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value):
        if 0 < len(value) < 15:
            self.name = value
        else:
            raise ValueError(f"Invalid value")

    def __delete__(self, instance):
        print("Deleting...")
        del self.name




class  Parent:
    child_name = NameField() 
    father_name = NameField() 
    mother_name = NameField()

    def __init__(self, child_name, father_name, mother_name):
        self.child_name = child_name
        self.father_name = father_name
        self.mother_name = mother_name


p = Parent()
print(p.child_name)
print(p.mother_name)
print(p.father_name)
