"""
Storing results the last winner in to file
"""
import os
import shelve
import sys
from pathlib import Path


class StoreResults:
    """The StoreResults class is used to store and manage results."""

    LAST_WINNER = "last_winner"
    LAST_WINNER_TEXT = "Last Winner"

    @property
    def last_winner(self) -> str:
        """
        The get_last_winner function is used to retrieve the last winner from the database.
            If there is no database, it will return None.

        :param self: Access the class attributes
        :return: The value of the key last_winner from the database
        """
        if not StoreResults._has_db():
            return ""

        db = shelve.open(StoreResults._get_db_path())
        winner = (
            f"{self.LAST_WINNER_TEXT}: {db[self.LAST_WINNER]}"
            if list(db.keys())
            else ""
        )
        db.close()

        return winner

    @last_winner.setter
    def last_winner(self, data: str) -> None:
        """
        The set_last_winner function takes a string as an argument and stores it in the database.
        The function is called by the set_winner function in the main file.

        :param self: Refer to the object itself
        :param data: str: Set the last winner to whatever data is passed in
        :return: None
        """
        with shelve.open(StoreResults._get_db_path()) as db:
            db[self.LAST_WINNER] = data

    def clean_last_winner(self) -> None:
        """
        The clean_last_winner function deletes the last winner from the database.


        :param self: Refer to the object itself
        :return: None
        """
        if not StoreResults._has_db():
            return
        db = shelve.open(StoreResults._get_db_path())
        if list(db.keys()):
            del db[self.LAST_WINNER]
        db.close()

    @staticmethod
    def _get_db_path(is_full: bool = False) -> str:
        """
        The _get_db_path function is used to get the path of the database file.
        The function takes a boolean argument, when if True will return the full name of
        the database file (including extension), otherwise it will only return the name without
        extension. The function returns a string containing either just
        'cards21db&quot' or 'cards21db.dat&quot'.

        :param is_full: bool: Determine whether the full path of the
        database file is returned or just its name
        :return: The path to the database file
        """
        file_name = "cards21db"
        ext = ".dat"
        data_folder = "db"
        path_db = Path(data_folder)
        if not path_db.exists():
            path_db.mkdir()

        file_name = f"{file_name}{ext}" if is_full else file_name
        return str(Path(sys.argv[0]).parent / path_db / file_name)

    @staticmethod
    def _has_db() -> bool:
        """
        The _has_db function checks to see if the database file exists.
        It returns True if it does, and False otherwise.

        :return: True if the database exists, and false otherwise
        """
        return os.path.exists(StoreResults._get_db_path(True))


if __name__ == "__main__":
    last_winner = "GoodMan: 25"
    StoreResults().last_winner = last_winner
    print(StoreResults().last_winner)
    assert (
        StoreResults().last_winner
        == f"{StoreResults().LAST_WINNER_TEXT}: {last_winner}"
    ), "Not equal winners"
    StoreResults.clean_last_winner(StoreResults())
    assert not StoreResults().last_winner, "Last winner still exists in storage"
    print(f"Last winner after cleaning: {StoreResults().last_winner}")
