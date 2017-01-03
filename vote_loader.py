#!/usr/bin/env python
'''This simply reads in a csv file of votes, and produces a list of votes'''
import csv
import numpy as np
from vote import Vote

CSVFILE = '/Users/will/Downloads/brainpirg.csv'


def load_votes(csv_file=CSVFILE):
    '''Read a csv file - each line is a vote, return a list of votes'''
    myvotes = []
    names = ['S', 'SSG', 'SSC', 'ScAAN']
    dict = {'Most preferred': 1, '---': 2, '----': 3, 'Least preferred': 4}
    try:
        # with open(csv_file, 'rb') as f:
        with open(csv_file, 'rU') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i > 0:
                    pref = [dict[j] for j in row[2:6]]
                    vote = [names[j] for j in np.array(pref).argsort()]
                    myvotes.append(Vote(vote))

    except Exception, e:
        raise
    return myvotes


def main():
    all_votes = load_votes()
    return all_votes


if __name__ == "__main__":
    votes_read_in = main()
    for vote in votes_read_in:
        print vote.choice()
