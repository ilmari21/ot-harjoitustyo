from connect_db import get_database_connection
from services.logbook_service import LogbookService
from repositories.logbook_repository import LogbookRepository
from repositories.user_repository import UserRepository


def initialize_services():
    """Initializes a LogbookService instance.

    Returns:
        Initialized LogbookService instance.
    """

    connection = get_database_connection()
    logbook_repository = LogbookRepository(connection)
    user_repository = UserRepository(connection)
    logbook_service = LogbookService(logbook_repository, user_repository)
    return logbook_service
