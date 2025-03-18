from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Remote Tutoring - Teach students online from anywhere!",
    "Handmade Crafts - Sell unique, handmade items on Etsy!",
    "Virtual Assistant - Help businesses with administrative tasks!",
    "Photography - Capture moments and sell your photos online!",
    "Podcasting - Start a podcast and monetize through sponsorships!",
    "E-book Publishing - Write and sell e-books on Amazon Kindle!",
    "Home Baking - Sell homemade baked goods in your community!",
    "Voiceover Work - Lend your voice to commercials and audiobooks!",
    "Website Flipping - Buy, improve, and sell websites for profit!",
    "Fitness Coaching - Provide virtual fitness training and meal plans!",
    "Local Tour Guide - Offer guided tours of your city or area!",
]

money_quotes = [
    "Wealth consists not in having great possessions, but in having few wants. – Epictetus",
    "An investment in knowledge pays the best interest. – Benjamin Franklin",
    "The stock market is filled with individuals who know the price of everything, but the value of nothing. – Philip Fisher",
    "Financial freedom is available to those who learn about it and work for it. – Robert Kiyosaki",
    "A penny saved is a penny earned. – Benjamin Franklin",
    "It’s not the employer who pays the wages. Employers only handle the money. It’s the customer who pays the wages. – Henry Ford",
    "You can be young without money, but you can’t be old without it. – Tennessee Williams",
    "Never spend your money before you have earned it. – Thomas Jefferson",
    "The real measure of your wealth is how much you’d be worth if you lost all your money. – Anonymous",
    "Do what you love and the money will follow. – Marsha Sinetar",
    "Money is a tool. Used properly it makes something beautiful; used wrong, it makes a mess! – Anonymous",
    "Do not be fooled by how much money you make, but by how much money you keep. – Robert Kiyosaki",
    "Financial fitness is not a pipe dream or a state of mind. It’s a reality if you are willing to pursue it and embrace it. – Will Robinson",
]

@app.get("/")
def read_root():
    return {
        "message": "Hello World, Go to /side_hustles or /money_quotes to get a random side hustle or money quote"
    }

@app.get("/side_hustles")
def get_side_hustles():
    """Returns a random side hustle idea"""
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
    """Returns a random money quote"""
    return {"money_quote": random.choice(money_quotes)}
