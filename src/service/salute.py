import random


class SaluteService:
    def __init__(self):
        self.salutes: list[str] = [
            "Rock on!",
            "For Karl!",
            "Rock and Stone!",
            "For Rock and Stone!",
            "ROCK... AND... STONE!",
            "Rock and Stone forever!",
            "Rock and roll and stone!",
            "Rock and Stone everyone!",
            "Rock and Stone, Brother!",
            "Yeaahhh! Rock and Stone!",
            "None can stand before us!",
            "Like that! Rock and Stone!",
            "Rock and Stone to the Bone!",
            "Yeah, yeah, Rock and Stone.",
            "We fight for Rock and Stone!",
            "Rock and Stone in the Heart!",
            "Did I hear a Rock and Stone?",
            "Stone and Rock! ...Oh, wait...",
            "That's it lads! Rock and Stone!",
            "If you don't Rock and Stone, you ain't comin' home!"
        ]

    def get_random_salute(self) -> str:
        return random.choice(self.salutes)

    def get_salute(self, index: int) -> str:
        return self.salutes[index]
