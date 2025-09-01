class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        #
        if "id" not in member or member["id"] is None:
            member["id"] = self._generate_id()
        #
        member["last_name"] = self.last_name
        self._members.append(member)
        return member
        # You have to implement this method
        # Append the member to the list of _members

    def delete_member(self, id):
        for i, m in enumerate(self._members):
            if m["id"] == id:
                self._members.pop(i)
                return True
        return False
    

        # You have to implement this method
        # Loop the list and delete the member with the given id

    def get_member(self, id):
        for m in self._members:
            if m["id"] == id:
                return m
        return None
        # You have to implement this method
        # Loop all the members and return the one with the given id

    # This method is done, it returns a list with all the family members

    def get_all_members(self):
        return self._members
