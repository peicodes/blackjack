# blackjack
Blackjack is a card counting simulation tool. It is used to prove that a simple card counting and betting strategy can be reliably profitable.

To run the simulation, run test.py. To change the minimum bet, change MIN_BET in simulation.py.

### Playing Strategy
The playing strategy used is the basic strategy table for blackjack: http://www.blackjackinstitute.com/store/Basic_Strategy_Chart.php

### Counting Strategy
The counting strategy used is the Hi-Lo counting system. Cards 10-A are worth -1, and cards 2-6 are worth +1. The rest are neutral. The summation of this count divided by an estimate of the number of decks left provides us with the True Count.

The true count is used to determine when to start and stop playing. Additionally, it is used to increase the bet size as the true count increases. 

### Security
The betting strategy used contains security considerations to prevent discovery while counting. There is a 'buffer zone' between the Start and Stop thresholds for the true count, which prevents the player from rapidly switching between playing and sitting out.

### Future Development
The playing strategy used does not adjust its play based on the true count. This optimization can be made using index tables, such as the Illustrious 18. 

The betting strategy can be further improved to prevent scrutiny by casino managers. It may appear suspicious when a player's winning frequency correlates with his bet size.

The simulation can be made more abstract by allowing third parties to use their own custom betting, playing, and counting strategies. 