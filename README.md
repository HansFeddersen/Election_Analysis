# Election_Analysis
Data Bootcamp Module 3: PyPoll With Python
## Overview of Project

### The purpose of this project is to write a code to audit an election in the counties of Jefferson, Denver and Arapahoe and make sure that the results are correct. The used Dataset contains all the votes recieved by 3 candidates in those counties (according to the Dataset there are no Null or Blank votes). With oour code, we are able to present the following results:
* 1. Number of votes casted
* 2. List of candidates who recieved votes
* 3. Number of votes that each candidate recieved
* 4. Percentage of votes each candidate obtained
* 5. The winner of the election based on popular vote.


## Resoruces
**For this analysis, the following resuorces were used**:
- Data Source: election_result.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Results

**How many votes were casted in this congretional election?**

According to the results of the eletion, a total of 369,711 votes were casted

**Breakdown of the number of votes and the percentage of votes for each county in the precint**

Of the 369,711 casted votes, the county with the largest number of votes was Denver with 306,055 votes (82.8%), followed by Jefferson with 38,855 votes (10,5%) and in the last place Arapahoe with 24,801 votes (6.7%).

**County with the largest number of votes**

The county with the largest number of votes was Denver. There were 306,055 casted votes in Denver (82,8% of the total) and of those votes 239,282 were fo candidate Diana DeGette (72.8%), 57,188 were for candidate Charles Casper Stockham (18,7%) and 9,585 were for candidate Raymon Anthony Doane (3.1%).

**Breakdown of the number of votes and the percentage of the total votes each candidate recieved**

The candidate with the most votes on her/his favor was Diana Degette with 272,892 votes (73.8%), followed by Charles Casper Stockham with 85,213 votes (23%) and finally Raymon Anthony Doane with 11,686 votes (3.1%).

**Candidate that won the election, his/her vote count and percentage of the total votes**

The election was won by Diana Degette with 272,892 votes on her favor, which represents a 73,8% of the total votes. All the votes that she obtained on Denver were sufficient to win the election (due to difference of casted votes between Denver and the other two counties).


## Election-Audit Summary

- The script is written to work with any election data that follows the same format as the election_results.csv used (Ballot Id, County and Candidate). The scrit can be modified to print more results about this elections. Results such as, candidate outcome on each county or group of two counties.

**Also, the script can be modified for other elections that have different data structures. Examples are as follows:

- 
