# monitoring-crypto
An example flask rest API server, for SE Fall 2022.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

## Target Audience/Goal

The target audiences are primarily crypto investors based on their investment portfolio


## Requirements
* Each of the main requirements will corespond to an API endpoint.
* Main focus is on the coinmarket API

## Front-End Design
Login Page
* Use mongodb for logging in
* database stores username/account data
* account recovery

Sign up
* include node for buttons/activate database

Home Page - Logged In
* User personalized
* Investor/crypto movements
* Include graph based on what they follow

Home Page - Not Logged In
* Latests Trends

Investor/User Profile
* Follow github UI
* Use twitter api for tweets
* follow button
* include net worth
* show socials

User Account (logged in)
* when first logging show "Hello Name"
* Drop down settings option
* Followers/ following
* Users can follow other users
* include net worth

Search bar
* include filter for user to choose what they search for
* include auto ending?

Search Page
* search crypto/investor option
* leading trends (e.g price change)
* shows what user search for
* shows similar things with same name/searched term
* includes market cap/ popular crypto trends
* include filter

Investor/Cryptocurrency Page
* info on it
* price change
* market news 


## Back-End Design
Users and Systems
* Login and registration authentication
* Subscriptions for alerts (e.g. texts, emails)
* Customized alerts based on prices and activity of followed investors
* Send alerts/messages

Data Processing
* Get data from APIs chosen
* Process and analyze data for different use cases

## Database
Database design update:
* include who users follows
* include who follows user

* Store user data, e.g. account info
* Query user data, e.g. get the number of accounts
* ER Diagram: [Draw.io Design](https://drive.google.com/file/d/1_9ncNf8hwSNbuxS2CsFDgUAu4zlofcJg/view?usp=sharing) 
