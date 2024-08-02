"""base class for fields"""
class Field:
    """base class for fields"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
