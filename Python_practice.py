counties= ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print ("El Paso in in the list of counties.")
# else:
#         print("El Paso is not on the list of counties.")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     #print("Arapahoe or El Paso is not in the list of counties")

# if "Arapahoe" in counties or "El Paso" in counties:
#     #print("Arapahoe or El Paso is in the list of counties.")
# else:
#    # print("Arapahoe and El Paso are not in the list of counties.")
# if "Arapahoe" in counties and "El Paso" not in counties:
#   # print("Only Arapahoe is in the list of counties.")
# else:
#     # print("Arapahoe is in the list of counties and El Paso is not in the list of counties")
# for i in range(len(counties)):
#    # print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict.keys():
#    # print(county)
# for voters in counties_dict.values():
#    # print(voters)
# for county in counties_dict:
#     #print(counties_dict[county])
# for county,voters in counties_dict.items():
#     #print(county and "County has",voters and "registered voters")
print(counties_dict)
print((dir(counties_dict)))
print((dir(counties)))