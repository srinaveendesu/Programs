################################################################################
# This file should be copied to a new test suite directory.
################################################################################

*** Settings ***
Library    		 ../lib/kone_webapp.py
Library    		 SeleniumLibrary
Library          BuiltIn
Library          Collections

*** Variables ***
${URL}      https://koneiot-portal-uat.eu-gb.mybluemix.net