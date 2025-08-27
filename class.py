class SuperHero:
    def __init__(self, name, real_name, power_level, custom_color, nemesis, special_abilities):
        self.name = name
        self.real_name = real_name
        self.power_level = power_level
        self.custom_color = custom_color
        self.nemesis = nemesis
        self.special_abilities = special_abilities
        self.__secret_mission = None  # Private attribute

    def fight_crime(self):
        if self.power_level > 85:
            print(f"{self.name} says: 'Yo, you're good!' 💥")
            self.power_level += 10
        elif 80 < self.power_level <= 85:
            print(f"{self.name} says: 'Not bad, keep pushing.' ⚡")
            self.power_level += 5
        else:
            print(f"{self.name} says: 'Work hard, fam.' 🧠")

    def train(self):
        print(f"{self.name} is training... 🏋️‍♂️")
        self.power_level += 7

    def reveal_identity(self):
        print(f"Real name: {self.real_name}")

    def set_secret_mission(self, mission):
        self.__secret_mission = mission

    def get_secret_mission(self):
        return self.__secret_mission


class OtherTwin(SuperHero):
    def __init__(self, name, real_name, power_level, custom_color, nemesis, special_abilities):
        super().__init__(name, real_name, power_level, custom_color, nemesis, special_abilities)

    def fight_crime(self):
        print(f"{self.name} prefers debugging over fighting. 🐛🔧")
        self.power_level += 8

    def super_power(self):
        print(f"{self.name}'s super power: Debugging anything, even your mood swings 😅")

    def secret(self):
        self.set_secret_mission("Rob a house... or maybe just rob bugs from your code 🕵️‍♂️")


# Example usage
codeman = SuperHero(
    name="CodeMan",
    real_name="Aschalew",
    power_level=90,
    custom_color="Electric blue with green accents",
    nemesis="me",
    special_abilities="Logic boost, bug zapper, Amharic code translator"
)

twin = OtherTwin(
    name="CodeTwin",
    real_name="AshClone",
    power_level=82,
    custom_color="Neon green with black trim",
    nemesis="SyntaxError",
    special_abilities="Debugger, sarcasm shield, loop breaker"
)

codeman.fight_crime()
twin.fight_crime()
twin.super_power()
twin.secret()
print("Twin's secret mission:", twin.get_secret_mission())