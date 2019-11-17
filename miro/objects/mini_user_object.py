from miro.objects.base_miro_object import MiroObjectType


class MiniUserObject:

    def __init__(self, obj_id: str, name: str):
        super().__init__(obj_id, MiroObjectType.USER_MINI)
        self.name = name

    def __repr__(self) -> str:
        return self.name
