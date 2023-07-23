## SSH CONTROLLER
SSH Controller is a Python application that allows you to manage SSH connections and transfer files securely to remote servers. With a user-friendly interface built using Dear PyGui, this application provides a simple and efficient way to interact with remote servers using SSH.

## Features
`>` 🔐 Secure Authentication: SSH Controller ensures secure authentication to remote servers using SSH.

`>` 📂 File Transfer: Easily transfer files between your local machine and remote servers.

`>` 🚀 User-friendly Interface: The application provides an intuitive and user-friendly interface for a smooth experience.

## Requirements
To run this application, you need to have the following installed on your system:

`>` Python (version 3.6 or higher)   
`>` Paramiko library (for SSH functionality)   
`>` Dear PyGui library (for the GUI)   

## Installation
`1.` First, ensure you have Python installed. If not, download it from [Python Official Website](https://www.python.org/downloads/).     
`2.` Install the required libraries using pip:   
```
pip install paramiko dearpygui
```   
`3.` Clone this repository to your local machine:      
```
git clone https://github.com/YOUR_USERNAME/SSH-Controller.git
``` 

## How to Use
`1.` Navigate to the project directory:     
```
cd SSH-Controller
```   
`2.` Run the application:       
```
python main.py
``` 
      
            
`·` The application will launch, showing the main menu.     
`·` To establish an SSH connection, click on the "CONNECT TO THE SERVER" button. Enter the server's username, IP address, and password, and then click on the "LOGIN" button.    
`·` Once connected, you can check the server's files by clicking on the "TRANSFER FILE" button. Enter the path to the folder you want to list and click on the "SUBMIT" button.     
`·` You can always return to the main menu by clicking on the "BACK" button in the respective windows.   

## Contributions and Issues
Contributions and feedback are welcome! If you encounter any issues or have suggestions for improvements, please create an `issue` in the GitHub repository.
