from enum import Enum

class Message(Enum):
    SUCCESS = ["Transaction is committed successfully.", "success"]
    FAILED = ["Transaction failed", "danger"]

class Alert:
    def alert_success( msg = "Transaction is committed successfully.", type="success"):
        return [msg,type]
    def alert_failed( msg = "Transaction failed.",type="danger"):
        return [msg,type]