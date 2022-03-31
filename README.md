# SE-Sprint01-Team12


**Contributors:** 
#### Chigozirim Margaret Arukwe and Julia Ramos Alves (Sprint 1)

## About the Project


### Description  

Corona Archive is a web service for tracking, displaying, evaluating, and archiving of the Corona infections in a particular location. There are four different types of users: visitors, establishments, hospitals and the agent. Visitors are the users that visit an establishment and their visits will be tracked by the application. Hospitals have control over the infection status of visitors and the agent has access to all archived information. Detailed explanations about which functionality is available for each one of these users can be found further in this document.

### Built with

- HTML
- CSS
- Python3
- Bootstrap
- Flask



### File Structure

```
\--SE-Sprint01-Team12    #root folder
	\--sql           #MySQL querys for initialization
	    ---
	\--static        #contains css, js and images files
	    ---
	\--templates	#contains all HTML files
	    ----
	-- README.md
	-- app.py		#main flask code with flask app initialization
	-- auth.py		#flask routes for authentication like registering, login
	-- routes.py		# other flask routes different from those for authentication
	-- main.py		#actual python file to be run (`python3 main.py` on terminal)
	-- db.yaml		#MySQL database configuration
	-- requirements.txt	#python dependencies to install for flask app to run
```

## Getting Started

### Guide for installing and getting it to work on your local machine


**Prerequisites**  
- MySQL  
- Flask (and therefore Python3)
```
pip3 install Flask
```

- Virtual Env
```
sudo pip3 install virtualenv
```


### Installation Guide

```

#Clone the repo (git clone <repo's_URL> )

#Create virtial environment
$ virtualenv env

# Start virtual environment
$ source env/bin/activate

# Install all the dependencies
$ pip3 install -r requirements.txt

# Open  MySQL
$ mysql -u {ENTER YOUR USERNAME OR ROOT} -p
	#enter your password

# Run this command in MYSQL command line to create required database.
> source sql/create_table.sql
> exit

# Edit the db.yam file (or create a new one) 

# Open db.yaml and enter database credentials (Format to enter your credentials is described below)
$ nano db.yaml

# Run python server
$ python3 main.py

```

### db.yaml File Format

```
mysql_host: "localhost"
mysql_user: "{YOUR USERNAME CHANGE THIS WHEN TYPING IN YOUR COMPUTER}"
mysql_password: "{YOUR PASSWORD CHANGE THIS WHEN TYPING IN YOUR COMPUTER}"
mysql_db: "seteam12"
```

### Links

##### Home page: http://localhost:5000/




## Documenting and Testing

### Establishment Registration

When accessing the application, there exists a registration page for establishments. For testing purposes, use the following information from example establishments on this page:

- **Establishment 1**  
**Name:** Nordmetall Servery  
**Address:** College Ring 3  
**City:** Bremen  
**State:** Bremen  
**ZIP Code:**  28759  

- **Establishment 2**  
**Name:** Mercator Servery  
**Address:** College Ring 6  
**City:** Bremen  
**State:** Bremen  
**ZIP Code:**  28759  

- **Establishment 3**  
**Name:** C3 Servery  
**Address:** College Ring 7  
**City:** Bremen  
**State:** Bremen  
**ZIP Code:**  28759  

- **Establishment 4**  
**Name:** Krupp Servery  
**Address:** College Ring 4  
**City:** Bremen  
**State:** Bremen  
**ZIP Code:**  28759  


- **Establishment 5**  
**Name:** Central Perk  
**Address:** 130 East 23rd Street  
**City:** New York  
**State:** New York  
**ZIP Code:** 11420  

For the last test in establishment registration, press the “Register” button with empty fields so that a warning will appear.

After each establishment registration there will be a QRcode displayed on the screen which can be downloaded. When these establishments have been registered, users will be able to see them displayed on the “Places” page. If a visitor visits a place, they have the possibility of scanning the QRcode that the establishment will hopefully have printed out and displayed, or they can locate an establishment on the “Places” page and scan their QRcode there. If the visitor doesn’t have any means of scanning the QRcode, they have the option of clicking a button to visit it instead. Since this application is at this time being hosted locally, the testing should be done by clicking that button.


### Visitor Registration

Considering that the previous step has been concluded and the visit button has been clicked, it is time for the visitor to provide their personal information. In order to create example visits, repeat this procedure for the existing establishments and the following example visitors:

As per the software description, a registered visitor does not have to provide details to the website again when visiting a place.
This is achieved by storing user input on their local machine, and retrieving it when next they access the registration form.

- **Visitor 1**  
**Name:** Monica Geller  
**Address:** 99 Maiden St. Fresh Meadows  
**City:** New York  
**State:** New York  
**ZIP Code:** 11365  
**Phone Number:** +1 212-200-0570  
**Email:** mgeller@jacobs-university.de  


- **Visitor 2**  
**Name:** Ross Geller  
**Address:** 391 Hill Field Ave. Bronx  
**City:** New York  
**State:** New York  
**ZIP Code:** 10456  
**Phone Number:** +1 212-202-0132  
**Email:** rgeller@jacobs-university.de  

- **Visitor 3**  
**Name:** Chandler Bing  
**Address:** 99 Maiden St. Fresh Meadows  
**City:** New York  
**State:** New York  
**ZIP Code:** 11365  
**Phone Number:** +1 212-204-9055  
**Email:** cbing@jacobs-university.de  

- **Visitor 4**   
**Name:** Phoebe Buffay  
**Address:** 9610 Cardinal Ave. New York  
**City:** New York  
**State:** New York  
**ZIP Code:** 10040  
**Phone Number:** +1 212-215-1287  
**Email:** pbuffay@jacobs-university.de  


- **Visitor 5**  
**Name:** Joey Tribbiani  
**Address:** 7041 North Fairground Street South Ozone Park  
**City:** New York  
**State:** New York  
**ZIP Code:** 11420  
**Phone Number:** +1 212-243-5925  
**Email:** jtribbiani@jacobs-university.de  

For the last test in visitor registration, press the “Enter” button with the following information on the fields, so that a warning will appear:

**Name:** Rachel Green  
**Address:** 7041 North Fairground Street South Ozone Park  
**City:** New York  
**State:** New York  
**ZIP Code:** 11420  
**Phone Number:** +1 212-243-5925  
**Email:** rgreen  



### Hospital Registration

There also exists a registration page for hospitals. Note that the registration for hospitals should be approved by the agent. For approval, the agent needs to provide the username and the password for each hospital. For testing purposes, use the following information from example hospitals (the username and password will be not be provided at the time of registration):

- **Hospital 1**  
**Name:** Klinikum Bremen Nord  
**Address:** Hammersbecker Str. 228  
**City:** Bremen  
**State:** Bremen  
**ZIP Code:** 28755  
**Username:** klinikumnord  
**Password:** healthy12  

- **Hospital 2**  
**Name:** Klinikum Bremen Mitte  
**Address:** Sankt-Jürgen-Straße 1  
**City:** Bremen  
**State:** Bremen  
**ZIP Code:** 28205  
**Username:** klinikumbremenmitte  
**Password:** fightcovid  

- **Hospital 3**  
**Name:** Hospital St. Joseph-Stift Bremen  
**Address:** Schwachhauser Heerstraße 54  
**City:** Bremen  
**State:** Bremen  
**ZIP Code:** 28209  
**Username:** krankenhausstjoseph  
**Password:** notocorona  


### Login

On the login page, the credentials of either the agent or a hospital can be submitted, so that the interface for either of these users will appear. The developers have already created the credentials for the agent. 

For the first test of this page, enter the following credentials as if trying to log in as a hospital before their registration has been approved, so that a warning will appear:

**Username:** krankenhausstjoseph  
**Password:** notocorona  

For testing the functionality of the agent, enter the following credentials on the login page:

**Username:** testadmin  
**Password:** testadmin123%

When logged in, approve the registration of the hospitals by entering the previously provided username and passwords for each. The hospitals awaiting approval appear on the bottom of the agent page.

On the agent page, the first thing that appears is a list of all registered visitors. An agent can see their status as infected or not infected and can click to see the visit history. They can also search the visitor’s by name.

Following that, there is a list of all establishments and the agent can click to see the visit history for each establishment as well. It’s also possible to search establishments by name.


For testing the functionality of the hospitals, enter one of the credentials that has been approved in the previous step. 

In the hospital page, there will be a list of all visitors displaying their information and their infection status. Visitors can be searched by name and the hospital can change their infection status. The infection status is also color coded, red for infected and green for not infected. 

# Change Log: 

```
- Packaging
- Login manager
- Encryption
- User login with cookies
- QR code 
- dashboards
- User check in
- 
```