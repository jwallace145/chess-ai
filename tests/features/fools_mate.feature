Feature: Fool's Mate

    Scenario: start a game of chess
        Given a chess board and white and black teams
        When we set the chess board in standard position
        Then team moves are valid for starting chess position

    Scenario: move white pawn to f3
        Given a chess board and white and black teams
        When we move white pawn to f3
        Then the team moves are valid for 1. pf3

    Scenario: move black pawn to e5
        Given a chess board and white and black teams
        When we move black pawn to e5
        Then the team moves are valid for 1. pf3 pe5

    Scenario: move white pawn to g4
        Given a chess board and white and black teams
        When we move white pawn to g4
        Then the team moves are valid for 1. pf3 pe5 2. pg4

    Scenario: move black queen to h4
        Given a chess board and white and black teams
        When we move black queen to h4
        Then the team moves are valid for 1. pf3 pe5 2. pg4 qh4
        And white is in a checkmate position



