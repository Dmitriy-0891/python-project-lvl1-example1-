import prompt
from brain_games.scripts import brain_progression


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    for x in list(range(1, 5)):
        if x == 4:
            print("Congratulations, " + name + "!")
        else:
            if brain_progression.main(name, x) is False:
                break


if __name__ == '__main__':
    main()
