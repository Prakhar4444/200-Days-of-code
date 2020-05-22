monthconversion = {
    1: "January",
    2: "February",
}
print(monthconversion[1])
print(monthconversion.get(2))
print(monthconversion.get(0))
print(monthconversion.get(0,"Not a valid value"))