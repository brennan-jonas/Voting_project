from gui import ID, VoteMenu, CandidateMenu, TotalVotes
from PyQt6.QtWidgets import *
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    total_votes = TotalVotes()
    vote_menu = VoteMenu(None, total_votes)
    id_widget = ID(vote_menu)
    candidate_menu = CandidateMenu(vote_menu, total_votes, id_widget)
    vote_menu.candidate_menu = candidate_menu
    id_widget.show()
    vote_menu.hide()

    sys.exit(app.exec())
