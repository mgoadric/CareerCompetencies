init python in mystore:


    #string stuff
    txtdict = {}
    chapters = []
    chapters.append(1)
    chapters.append(2)

    txtdict[1] = [["Welcome Center", "Come by the Welcome Center to get an overview of", "the Hendrix experience!"], ["Library", "Meet and Greet for new students! Come meet some new friends!"], ["SLTC", "No events planned for today"], ["Resume Tip #1","Get new experiences!", "Always be on the lookout for new opportunities you would enjoy!"], ["Good Vibe of the Day", "'Thinking: the talking of the soul with itself.'", "           -Plato"]]
    txtdict[2] = [["Library", "Come study for finals with others with Peer Learning!"], ["SLTC", "Information Panel for STEM Majors in the Burrow!"], ["Mills", "Interested in the Humanities? Come by for an overview of", "our program!"], ["Resume Tip #2", "Use Reverse Cronological Order!", "List most recent experiences and work backwards"], ["Good Vibe of the Day", "'Love and desire are the spirit's wings to great deeds.'", "              -Johann Wolfgang von Goethe"]]
    def gettxt(chapter, i):
        return txtdict[chapter][i]

    def gettxtblock(chapter):
        return txtdict[chapter]
