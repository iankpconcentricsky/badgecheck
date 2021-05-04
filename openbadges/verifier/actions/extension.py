from .action_types import STORE_EXTENSION


def add_extension(node_id=None, data=None):
    action = {
        'type': STORE_EXTENSION,
        'node_id': node_id,
        'data': data
    }
    return action
