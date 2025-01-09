# def parse_input(lines):
#     distances = {}
#     locations = set()
#
#     for line in lines:
#         parts = line.split()
#         loc1, loc2 = parts[0], parts[2]
#         distance = int(parts[4])
#
#         distances[(loc1, loc2)] = distance
#         distances[(loc2, loc1)] = distance
#
#         locations.add(loc1)
#         locations.add(loc2)
#
#     return distances, locations
#
#
# def shortest_route(distances, locations):
#     shortest_distance = float('inf')
#     locations_list = list(locations)
#
#     for i in range(len(locations_list)):
#         for j in range(i + 1, len(locations_list)):
#             loc1, loc2 = locations_list[i], locations_list[j]
#
#             if (loc1, loc2) in distances:
#                 distance = distances[(loc1, loc2)]
#             elif (loc2, loc1) in distances:
#                 distance = distances[(loc2, loc1)]
#             else:
#                 continue  #
#
#             print(locations_list[i], locations_list[j], distance)
#
#
# lines = []
#
# while True:
#     line = input()
#     if not line:
#         break
#     lines.append(line.strip())
#
# distances, locations = parse_input(lines)
#
# shortest_distance = shortest_route(distances, locations)
# print(shortest_distance)
