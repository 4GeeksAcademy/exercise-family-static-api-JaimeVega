"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, _member):
        ## You have to implement this method
        ## Append the member to the list of _members
        _member['id'] = self._generate_id()
        _member["last_name"] = self.last_name
        self._members.append(_member)
        return _member

    def delete_member(self, id):
        ## You have to implement this method
        ## Loop the list and delete the member with the given id
        new_list = []
        for member in self._members:
            if member['id'] != id:
                new_list.append(member)
        self._members = new_list
        return new_list

    def get_member(self, id):
        ## You have to implement this method
        ## Loop all the members and return the one with the given id
        for member in self._members:
            if id == member["id"]:
                return member

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    
    def repeat_member(self, add_member):
        for member in self._members:
            if member['first_name'] == add_member['first_name'] and member['age'] == add_member['age'] and member['lucky_numbers'] == add_member['lucky_numbers']:
                return True
        return False
            
            
