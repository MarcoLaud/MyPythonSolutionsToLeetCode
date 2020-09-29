#    You are given the array paths, where paths[i] = [cityAi, cityBi]
#    means there exists a direct path going from cityAi to cityBi.
#    Return the destination city, that is, the city without any path
#    outgoing to another city.
#
#    It is guaranteed that the graph of paths forms a line without
#    any loop, therefore, there will be exactly one destination city.


class Solution:
    def destCity(self, paths):
        paths_unpkd = sum([couple for couple in paths], [])
        return [city for par in paths for city in par
                if paths_unpkd.count(city) == 1 and par.index(city) != 0][0]


if __name__ == "__main__":
    test_input = [["London", "New York"], ["New York", "Lima"],
                  ["Lima", "Sao Paulo"]]
    print(Solution.destCity(Solution, test_input))
