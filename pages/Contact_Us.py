import streamlit as stl
import smtplib
from email.message import EmailMessage

stl.header("CONTACT US")
fullname = stl.text_input("Enter your fullname")
email = stl.text_input("Enter your Email")
contact = stl.text_input("Contact")