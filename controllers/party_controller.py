from models.party import Party
from repositories.party_repository import PartyRepository


class PartyController:
    # Constructor
    def __init__(self):
        """

        :return:
        """
        self.party_repository = PartyRepository()
        print("Party controller ready...")

    def get_all_parties(self) -> list:
        """
        This method get all the parties stored in the DB
        :return: list of parties
        """
        return self.party_repository.find_all()

    def get_party_by_id(self, id_: str) -> dict:
        """
        This method gets one party in the DB by providing its id
        :param id_:
        :return: party dictionary
        """
        return self.party_repository.find_by_id(id_)

    def insert_party(self, party_: dict) -> dict:
        """
        This method inserts a party in the DB by providing its attributes in a dictionary
        :param party_:
        :return: party dictionary
        """
        new_party = Party(party_)
        return self.party_repository.save(new_party)

# UPDATE party
    def update_party(self, id_: str, party_: dict) -> dict:
        """
        This method updates a party in the DB by providing its id and attributes
        :param id_:
        :param party_:
        :return: party dictionary
        """
        party = Party(party_)
        return self.party_repository.update(id_, party)

# DELETE party
    def delete_party(self, id_: str) -> dict:
        """
        This method deletes a party in the DB by providing its id
        :param id_:
        :return: message: "Delete party"
        """
        print("Deleted " + id_)
        return self.party_repository.delete(id_)
