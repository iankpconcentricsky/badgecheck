from ..actions.action_types import STORE_EXTENSION


def extension_reducer(state=None, action=None):
    if state is None:
        state = []

    if action.get('type') == STORE_EXTENSION:
        state.append(
            action.get('data'),
        )

    return state
