from game.npc import Npc


class Location:
    def __init__(self, name: str, desc: str, options: dict, npcs: dict, items: dict):
        self.name = name
        self.desc = desc
        self.options = options
        self.npcs = npcs
        self.items = items

    @classmethod
    def from_dict(cls, name: str, data: dict) -> "Location":
        npcs = {n: Npc.from_dict(n, d) for n, d in data.get("npcs", {}).items()}
        items = data.get("items", {})
        return cls(name, data.get("desc", ""), data.get("options", {}), npcs, items)

    def list_npcs(self):
        pass

    #    def select_npc(self, selection: int) -> "Npc":
    #        npc_list = self.npcs.items()
    #        if not 1 <= selection <= len(self.npcs):
    #            raise ValueError(
    #                f"Incorrect choice - number out of ragnge: {selection}. Select from 1 to {len(self.npcs)}."
    #            )
    #        return npc_list[selection - 1]

    def go_to_conversation(self):
        pass
