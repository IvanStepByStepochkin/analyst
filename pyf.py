# import re
# music_base = eval(input())
# artist = input()
# song = input()

# def search_artist_and_song(database, artist_request, song_request):
#     artist_search = artist_request.lower()
#     found_artist = False
#     for i in range(0, len(database), 2):
#         artist = database[i]
#         songs = database[i + 1]
#         if artist == artist_search:
#             found_artist = True
#             song_list = [re.sub(r'[^a-z\s]', '', song).strip() for song in songs.split(';')]
#             formatted_songs = [' '.join(word.capitalize() for word in song.split()) for song in song_list]
#             discography = (artist_request, len(formatted_songs), formatted_songs)
#             print(discography)
#             formatted_song_search = ' '.join(word.capitalize() for word in song_request.split())
#             if formatted_song_search in formatted_songs:
#                 print(f"We have {len(formatted_songs)} songs by {artist_request}. The requested song {song_request} is also available. Enjoy your listening experience!")
#             else:
#                 print(f"We have {len(formatted_songs)} {artist_request} songs. However, the requested song {song_request} is not available. We offer our deepest apologies!")
#             return
#     if not found_artist:
#         print("Sorry, we don't have any songs by this artist")
# search_artist_and_song(music_base, artist, song)
# music_base = eval(input())
# artist = input()
# song = input()
# n = 0

# music_base2 = music_base
# print(music_base2.lower())
# while len(music_base) > n:
#     music_base[n] = music_base[n].replace("%", "")
#     music_base[n] = music_base[n].replace("#", "")
#     music_base[n] = music_base[n].replace("*", "")
#     music_base[n] = music_base[n].replace("^", "")
#     music_base[n] = music_base[n].replace("&", "")
#     music_base[n] = music_base[n].replace("$", "")
#     music_base[n] = music_base[n].title()
#     n = n + 1
# n = 0
# art = 0
# music_base

# while len(music_base) > n:
#     if music_base[n] == artist:
#         art = art + 1
#         g = 0
#         k = 0
#         j = 0
#         gt = music_base[n + 1]
#         while len(gt) > k:

#             if gt[k] == ";":
#                 j = j + 1
#             k = k + 1
#         discography = list()
#         discography = music_base[n], j + 1, music_base[n + 1].split("; ")
#         gtt = song in music_base[n + 1]
#         n = 100000
#     n = n + 1


# print(discography)

# if art == 0:
#     print("Sorry, we don't have any songs by this artist")
# elif art == 1 and gtt == True:
#     print(
#         f"We have {j + 1} songs by {discography[0]}. The requested song {song} is also available. Enjoy your listening experience!"
#     )
# elif art == 1 and gtt == False:
#     print(
#         f"We have {j+1} {discography[0]} songs. However, the requested song {song} is not available. We offer our deepest apologies!"
#     )

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def is_regular(n):
#     if n == 1:
#         return True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             if i not in [2, 3, 5]:
#                 return False
#             n //= i
#             while n % i == 0:
#                 n //= i
#     if n not in [1, 2, 3, 5]:
#         return False
#     return True

# def find_regular_numbers(n):
#     regular_numbers = []
#     for i in range(1, n + 1):
#         if is_regular(i):
#             regular_numbers.append(i)
#     return regular_numbers

# n = int(input())  # set integer value
# print(find_regular_numbers(n))


# temperatures = [32, 72, 85]
# index = 0
# max_index = len (temperatures)
# answer = []
# while index < max_index:
#     temperature = temperatures[index]
#     if temperature < 50:
#         category = "cold"
#     else:
#         category = "hot"
#     answer.append(f" {temperature} °F is {category}")
#     index += 1
# else:
#     print (answer)


# 1/1
# b = []

# for i in range (10, 0, -2):
#     b.append(str(i))

# ans = ' '.join(b)
# print(ans)

# 1/2

# text = "Python"
# s = ''
# for i in range(len(text)):
#     if i % 2 == 0:
#         s = s + text[i].upper()
#     else:
#         s = s + text[i].lower()
# print (s)


# 1/3


# for i in range(1, 3) :
#     for j in range(1, 3):
#         if i * j == 4:
#             break
#         print(f"{i} * {j} = {i * j}")

# 1/4

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c', 'd']
# for i in range (len(list1)):
#     print(f"Pair: {list1[i]}, {list2[i]}")


# 1/5


# total = 0
# for i in range(1, 6):
#     if i % 2 == 0:
#         total -= i
##         print(i, total, "a")
#     else:
#         total += i
##         print(i, total, "b")
# print (total)


# text = input()
# cleaned_text = ""
# for char in text:
#     if char.isalnum() or char.isspace():
#         cleaned_text += char.lower()
# words = cleaned_text.split()

# words2 = list()


# for h2 in range(len(words)):
#     if words[h2] not in words2:
#         words2.append(words[h2])

# count2 = 0
# for count in range(len(words2)):
#     count_words = 0
#     for count2 in range(len(words)):
#         if words2[count] == words[count2]:
#             count_words += 1
#     print(f"{words2[count]}: {count_words} time(s)")


# one = int(input())
# for i in range(11, one):

#     h = i%10
#     if h != 0:
#         number_differents = i / h
#     if h == number_differents:
#         print(i)

# number = int(input())

# k=0
# k2=1
# mass_fibonacci = list()
# mass_fibonacci.append(0)
# for i in range(0, number+1):
#     # mass_fibonacci.append(k)
#     k3 = k + k2
#     mass_fibonacci.append(k)
#     k = k2
#     k2 = k3

# for j in range(number, 0, -1):
#     if j%2 == 0 and mass_fibonacci[j]%5 == 0:
#         print(mass_fibonacci[j])
#         break


# one = int(input())
# for i in range(11, one):

#     g = i%10
#     if g != 0:
#         number_differents = i / g
#     if g == number_differents:
#         print(i)
