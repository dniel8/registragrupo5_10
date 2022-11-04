from models.party import Party


class PartyController:
    # Constructor
    def __int__(self):
        """

        :return:
        """
        print("Party controller ready...")

    def get_all_parties(self) -> list:
        """
        This method get all the parties stored in the DB
        :return: list of parties
        """
        print("Get all parties")

    def get_party_by_id(self, id_: str) -> dict:
        """
        This method gets one party in the DB by providing its id
        :param id_:
        :return: party dictionary
        """
        print("Get one party by id")

    def insert_party(self, party_: dict) -> dict:
        """
        This method inserts a party in the DB by providing its attributes in a dictionary
        :param party_:
        :return: party dictionary
        """
        print("Insert party")

# UPDATE party
    def update_party(self, id_: str, party_: dict) -> dict:
        """
        This method updates a party in the DB by providing its id and attributes
        :param id_:
        :param party_:
        :return: party dictionary
        """
        print("Update party")

# DELETE party
    def delete_party(self, id_: str) -> str:
        """
        This method deletes a party in the DB by providing its id
        :param id_:
        :return: message: "Delete party"
        """
        print("Deleted " + id_)
        return {"Delete count": 1}
