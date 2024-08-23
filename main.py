# age: int
# name: str
# height: float
# is_human: bool


#specifying the data type in the paraments and as an out
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(police_check(19))

