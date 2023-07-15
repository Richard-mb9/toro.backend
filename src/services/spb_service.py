from src.commons.errors import NotFoundError, BadRequestError

from .schemas import SPBEventRequest
from .account_service import AccountService
from .user_service import UserService


class SPBService:
    """Class for events SPB"""

    def execute_event(self, event: SPBEventRequest):
        if event.event == "TRANSFER":
            account_target = AccountService().find_by_account_id(
                int(event.target.account)
            )
            if account_target is None:
                raise NotFoundError("Account not found")
            user_target = UserService().find_by_id(account_target.user_id)

            if user_target.cpf != event.origin.cpf:
                raise BadRequestError(
                    "the source cpf should be the same as the destination account"
                )

            new_amount = float(account_target.amount) + float(event.amount)

            AccountService().update(event.target.account, new_amount)
