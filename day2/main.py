def part1(fname ='test.txt'):
    ans = 0
    with open(fname) as f:
        for line in f:
            game_id = int(line.split(':')[0][5:])
            games = line.split(':')[1].split(';')
            valid_game = True
            for game in games:
                colors = game.split(',')
                for color in colors:
                    num, color = color.split()
                    num = int(num)
                    if num > {'red':12,'blue':14,'green':13}.get(color,0):
                        valid_game =False 
                        break
            if valid_game:
                ans += game_id
    return ans


print(part1('input.txt'))
print(part1())



def part2(fname ='test.txt'):
    # red = 12
    # green = 13
    # blue = 14
    ans = 0
    with open(fname) as f:
        for line in f:
            # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            # get the game id 
            game_id = int(line.split(':')[0][5:])
            # get each game's balls
            games = line.split(':')[1].split(';')
            red, green, blue = 0, 0, 0
            for game in games:
                # e.g. a game: ' 3 blue, 4 red'
                colors = game.split(',')
                valid_game = True
                for color in colors:
                    # e.g. a color: ' 3 blue'
                    num, color = color.split()
                    num = int(num)
                    # add the balls to the game
                    if color == 'red' and num > red:
                        red = num
                    elif color == 'green' and num > green:
                        green = num
                    elif color == 'blue' and num > blue:
                        blue = num
            ans += red*green*blue
    return ans



print(part2('input.txt'))
print(part2())