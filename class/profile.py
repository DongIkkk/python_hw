class Profile:
    def __init__(self):
        self.profile = {
            "name": "-",
            "gender": "-",
            "birthday": "-",
            "age": 0,
            "phone": "-",
            "email": "-",
        }

    def set_profile(self, profile):
        self.profile = profile

    def get_name(self):     # 딕셔너리 객체 호출 get
        return self.profile.get("name")

    def get_gender(self):
        return self.profile.get("gender")

    def get_birthday(self):
        return self.profile.get("birthday")

    def get_age(self):
        return self.profile.get("age")

    def get_phone(self):
        return self.profile.get("phone")

    def get_email(self):
        return self.profile.get("email")


profile = Profile()
profile.set_profile({
    "name": "kim",
    "gender": "man",
    "birthday": "01/01",
    "age": 28,
    "phone": "01012345678",
    "email": "python@sparta.com"
})

print(profile.get_name())
print(profile.get_gender())
print(profile.get_birthday())
print(profile.get_age())
print(profile.get_phone())
print(profile.get_email())
