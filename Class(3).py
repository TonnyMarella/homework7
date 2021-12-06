class SoccerPlayer:
    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self, goal=1):
        self.goals += goal

    def make_assist(self, assist=1):
        self.assists += assist

    def statistics(self):
        print(f"{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}")


leo = SoccerPlayer('Leo', 'Messu')
leo.score(700)
leo.make_assist(500)
leo.statistics()
kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics()