#!/usr/bin/python

###################################################
###						###
###		palindrome generator		###
###						###
###################################################

#prompt the user to enter first half of a guessed password that needs to be mirrored
first_half = raw_input("Enter what you believe to be the first half of the palindrome'd password: ")

print first_half ## debug print

#populate second half of the palindrome by reversing the first half using string splicing
second_half = first_half[::-1]

print second_half ## debug print

#concatenate the two halves to produce one string
palindrome = first_half + second_half

print palindrome ## debug print

#produce a palindrome that doesn't repeat the middle characters
compressed_palindrome = first_half.strip(first_half[-1]) + second_half

print compressed_palindrome ## debug print
