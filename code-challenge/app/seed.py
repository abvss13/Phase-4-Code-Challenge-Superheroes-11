from setup import db, app
from models import Power, Hero, HeroPower
from sqlalchemy import func
import random

with app.app_context():
    print("🦸‍♀️ Seeding powers...")

    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"},
    ]

    for power_data in powers_data:
        power = Power(**power_data)
        db.session.add(power)

    print("🦸‍♀️ Seeding heroes...")

    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"},
    ]

    for hero_data in heroes_data:
        hero = Hero(**hero_data)
        db.session.add(hero)

    print("🦸‍♀️ Adding powers to heroes...")

    strengths = ["Strong", "Weak", "Average"]

    heroes = Hero.query.all()

    import random

    for hero in heroes:
        random_power_count = random.randint(1, 3)
        for _ in range(random_power_count):
            random_power = Power.query.order_by(func.random()).first()  
            random_strength = random.choice(strengths)
            hero_power = HeroPower(hero=hero, power=random_power, strength=random_strength)
            db.session.add(hero_power)

    db.session.commit()

    print("🦸‍♀️ Done seeding!")