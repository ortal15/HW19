oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom\
Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris\
Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

"""a"""
print('a:')
oscar_winners.add('Watson Emma')
"""b"""
print('b:')
oscar_winners2 = oscar_winners.copy()
oscar_winners2.remove("Meryl Streep")
oscar_winners2.clear()
"""c"""
print('c:')
print(titanic_actors & dark_knight_actors)
"""d"""
print('d:')
print(avengers_actors.intersection(iron_man_actors))
"""e"""
print('e:')
print(oscar_winners.isdisjoint(actor_list))
"""f"""
print('f:')
print(avengers_actors.issubset(actor_list))
"""g"""
print('g:')
print(movie_cast.pop())
"""h"""
print('h:')
# movie_cast.remove("Matt Damon")
"""i"""
print('i:')
print(titanic_actors.difference(oscar_winners))
"""j"""
print('j:')
print(titanic_actors.symmetric_difference(dark_knight_actors))
"""k"""
print('k:')
add = {'Daniel Day-Lewis', 'Cate Blanchett'}
oscar_winners.update(add)
print(oscar_winners)
"""l"""
print('l:')
print(titanic_actors.union(dark_knight_actors))
