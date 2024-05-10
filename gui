import sys
from PyQt5.QtWidgets import *
import logic

class ID(QWidget):
    def __init__(self, vote_menu):
        '''
        Makes ID gui and shows if an invalid ID occurs
        Makes buttons for the ID gui
        Connects vote_menu to ID gui to show it after correct ID is entered
        :param vote_menu:
        '''
        super().__init__()
        self.id = ID
        self.setWindowTitle('ID')
        self.setGeometry(0,0, 338, 282)
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().geometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.label_id = QLabel("Enter Voter ID", self)
        self.label_id.setGeometry(50, 30, 150, 20)

        self.invalid_id = QLabel("Invalid ID", self)
        self.invalid_id.setGeometry(50, 150, 110, 24)
        self.invalid_id.hide()

        self.id = QLineEdit(self)
        self.id.setGeometry(30, 75, 291, 20)

        self.enterButton = QPushButton("Enter", self)
        self.enterButton.setGeometry(50, 120, 110, 24)
        self.enterButton.clicked.connect(self.id_check)

        self.id.returnPressed.connect(self.id_check)
        self.voter_id = ""
        self.vote_menu = vote_menu

    def id_check(self)-> None:
        '''
        Uses logic function to check the id to know if they can vote
        Shows invalid ID if voter id is invalid
        '''
        self.voter_id = self.id.text()
        if logic.id_check(self.voter_id):
            self.hide()
            self.vote_menu.show()
            self.invalid_id.hide()
            self.id.clear()
        else:
            self.invalid_id.show()

class CandidateMenu(QWidget):
    def __init__(self, vote_menu, total_votes_widget, ID):
        '''
        Sets up candidate menu and buttons for each one
        Connects buttons to each candidate
        :param vote_menu:
        :param total_votes_widget:
        :param ID:
        '''
        super().__init__()
        self.vote_menu = vote_menu
        self.total_votes_widget = total_votes_widget
        self.ID = ID

        self.setWindowTitle("Candidate Menu")
        self.setGeometry(0, 0, 338, 282)
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().geometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.label = QLabel("Candidate Menu", self)
        self.label.setGeometry(110, 40, 111, 20)

        self.radioButton1 = QPushButton("Bianca", self)
        self.radioButton1.setGeometry(50, 100, 110, 24)
        self.radioButton1.clicked.connect(lambda: self.vote("Bianca"))

        self.radioButton2 = QPushButton("Edward", self)
        self.radioButton2.setGeometry(50, 130, 110, 24)
        self.radioButton2.clicked.connect(lambda: self.vote("Edward"))

        self.radioButton3 = QPushButton("Felicia", self)
        self.radioButton3.setGeometry(50, 160, 110, 24)
        self.radioButton3.clicked.connect(lambda: self.vote("Felicia"))

        self.label2 = QLabel("Click on the candidate you want to vote for", self)
        self.label2.setGeometry(30, 220, 291, 20)

    def vote(self, candidate_name)-> None:
        '''
        Uses logic functions to update the candidates vote total in the gui
        Shows to enter a new voter ID when a vote is cast
        :param candidate_name:
        :return:
        '''
        logic.vote_for(candidate_name)
        bianca, edward, felicia = logic.get_individual_votes()
        self.total_votes_widget.update_votes(bianca, edward, felicia)
        self.hide()
        self.ID.show()


class VoteMenu(QWidget):
    def __init__(self, candidate_menu, total_votes):
        '''
        Sets up the vote menu window and connects it to the candidate menu and total votes
        Connects vote and exit buttons to their respective menus
        :param candidate_menu:
        :param total_votes:
        '''
        super().__init__()
        self.setWindowTitle("Vote Menu")
        self.setGeometry(0, 0, 338, 282)
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().geometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.candidate_menu = candidate_menu
        self.total_votes = total_votes

        self.label = QLabel("Vote Menu", self)
        self.label.setGeometry(120, 30, 111, 20)

        self.voteButton = QPushButton("Vote", self)
        self.voteButton.setGeometry(50, 80, 110, 24)
        self.voteButton.clicked.connect(self.vote)

        self.exitButton = QPushButton("Exit", self)
        self.exitButton.setGeometry(50, 120, 110, 24)
        self.exitButton.clicked.connect(self.exit)
        

    def vote(self)-> None:
        '''
        When someone votes show the candidate menu
        :return:
        '''
        self.hide()
        self.candidate_menu.show()

    def exit(self)-> None:
        '''
        When someone presses exit show the total votes
        :return:
        '''
        self.hide()
        self.total_votes.show()

class TotalVotes(QWidget):
    def __init__(self):
        '''
        Makes Total votes gui
        '''
        super().__init__()
        self.setWindowTitle("Total Votes")
        self.setGeometry(0, 0, 338, 282)
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().geometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.label_bianca = QLabel("Bianca: ", self)
        self.label_bianca.setGeometry(50, 30, 150, 20)

        self.label_edward = QLabel("Edward: ", self)
        self.label_edward.setGeometry(50, 60, 150, 20)

        self.label_felicia = QLabel("Felicia: ", self)
        self.label_felicia.setGeometry(50, 90, 150, 20)

        self.label_total = QLabel("Total Votes: ", self)
        self.label_total.setGeometry(50, 120, 150, 20)

    def update_votes(self, bianca, edward, felicia)-> None:
        '''
        Updates each candidates vote totals gui and updates the total votes
        :param bianca:
        :param edward:
        :param felicia:
        :return:
        '''
        self.label_bianca.setText(f"Bianca: {bianca}")
        self.label_edward.setText(f"Edward: {edward}")
        self.label_felicia.setText(f"Felicia: {felicia}")

        total_votes = bianca + edward + felicia
        self.label_total.setText(f"Total Votes: {total_votes}")


