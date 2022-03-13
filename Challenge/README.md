# Election_Analysis
Data Bootcamp Module 3: PyPoll With Python
## Overview of Project

### The purpose of this project is to write a code to audit an election in the counties of Jefferson, Denver and Arapahoe and to make sure that the results are correct. The used Dataset contains all the votes received by 3 candidates in those counties (according to the Dataset there are no Null or Blank votes). With our code, we are able to present the following results:
* I. Number of votes casted
* II. List of candidates who received votes
* III. Number of votes that each candidate received
* IV. Percentage of votes each candidate obtained
* V. The winner of the election based on popular vote.


## Resoruces
**For this analysis, the following resuorces were used**:
- Data Source: election_result.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Results

**How many votes were casted in this congretional election?**

According to the results of the eletion, a total of 369,711 votes were casted.

The script to get this result is as follows (total votes started from 0):

![This is an image](https://github.com/HansFeddersen/Election_Analysis/blob/main/Challenge/Resources/More/Total%20_number%20_of_votes.png)

**Breakdown of the number of votes and the percentage of votes for each county in the precint**

Of the 369,711 casted votes, the county with the largest number of votes was Denver with 306,055 votes (82.8%), followed by Jefferson with 38,855 votes (10,5%) and in the last place Arapahoe with 24,801 votes (6.7%).

The script to get this result is as follows:

![This is an image](https://github.com/HansFeddersen/Election_Analysis/blob/main/Challenge/Resources/More/Votes_per_county.png)
![This is an image](https://github.com/HansFeddersen/Election_Analysis/blob/main/Challenge/Resources/More/Percntage_per_county.png)


**County with the largest number of votes**

The county with the largest number of votes was Denver. There were 306,055 casted votes in Denver (82,8% of the total) and of those votes 239,282 were fo candidate Diana DeGette (72.8%), 57,188 were for candidate Charles Casper Stockham (18,7%) and 9,585 were for candidate Raymon Anthony Doane (3.1%).

The script to get this result is as follows:

![This is an image](https://github.com/HansFeddersen/Election_Analysis/blob/main/Challenge/Resources/More/largest_county.png)

**Breakdown of the number of votes and the percentage of the total votes each candidate recieved**

The candidate with the most votes on her/his favor was Diana Degette with 272,892 votes (73.8%), followed by Charles Casper Stockham with 85,213 votes (23%) and finally Raymon Anthony Doane with 11,686 votes (3.1%).

The script to get this result is as follows:

![This is an image](https://github.com/HansFeddersen/Election_Analysis/blob/main/Challenge/Resources/More/Votes_per_candidate.png)

**Candidate that won the election, his/her vote count and percentage of the total votes**

The election was won by Diana Degette with 272,892 votes on her favor, which represents a 73,8% of the total votes. All the votes that she obtained on Denver were sufficient to win the election (due to difference of casted votes between Denver and the other two counties).

The script to get this result is as follows:

![This is an image](https://github.com/HansFeddersen/Election_Analysis/blob/main/Challenge/Resources/More/Winning_candidate.png)

## Election-Audit Summary

- The script is written to work with any election data that follows the same format as the election_results.csv used (Ballot Id, County and Candidate). The script can be modified to print more results about these elections. Results such as, candidate outcome on each county or group of two counties.

**Also, the script can be modified for other elections that have different data structures. Examples are as follows:**

- Elections for city/state/country position (such as senator or president) where you can group the information by county, city and state. For this analysis the code should be modified to contain more dictionaries with all the counties that belong to one city and all the cities that belong to one state. Then one gets and group the results to have a very delicate analysis of the elections.

- Elections such as the US presidential election where the candidate that wins the popular vote, does not necessarily wins the election (because each state represents a certain number of electors from the electoral college). One can introduce the data of how many electors does each state give and get the outcome of how many electoral votes each of the candidates received.

