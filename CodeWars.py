

#  0123456789
# 0##########
# 1##      ##
# 2# #    # #
# 3#  #  #  #
# 4#   ##   #
# 5#   ##   #
# 6#  #  #  #
# 7# #    # #
# 8##      ##
# 9##########

# rowCount = 10
# columnCount = 10

# for i in range(rowCount):
#   for j in range(columnCount):
#     if i == 0 or i == rowCount - 1 or j == 0 or \
#       j == columnCount - 1 or i == j or j == columnCount - i - 1:
#       print("#", end='')
#     else:
#       print(" ", end='')
#   print()


def high_and_low(numbers):
  # l = numbers.split(' ')
  # print(l)
  # min = int(l[0])
  # max = int(l[0])
  # for num in l:
  #   if int(num) < min:
  #     min = int(num)
  #   if int(num) > max:
  #     max = int(num)

  # more clever
  l = [int(num) for num in numbers.split(' ')]
  return str(max(l)) + ' ' + str(min(l))

# print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))



## Descending Order
# def Descending_Order(num):
#     return int(''.join(sorted(str(num), reverse=True)))

# print(Descending_Order(10147237031))


# # initialize
# a = []
# # create the table (name, age, job)
# a.append(["Nick", 30, "Doctor"])
# a.append(["John",  8, "Student"])
# a.append(["Paul", 22, "Car Dealer"])
# a.append(["Mark", 66, "Retired"])

# # sort the table by age
# import operator
# a.sort(key=operator.itemgetter(0, 1), reverse=True)

# # print the table
# print(a)


def DNA_strand(dna):
  dna_map = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
  }
  return ''.join([dna_map[sym] for sym in dna])

def DNA_strand_v2(dna):
  return dna.translate(str.maketrans('ATCG', 'TAGC'))

# assert(DNA_strand('ATTGC') == 'TAACC')



##  Given a string, replace every letter with its position in the alphabet.
##  a being 1, b being 2, etc.
def alphabet_position(text):
  return ' '.join([str(ord(item.lower()) - ord('a') + 1) \
                   for item in text if item.isalpha() \
                  ])

# print(alphabet_position('asdjfak'))


## Take a list of non-negative integers and strings
## Returns a new list with the strings filtered out.
def filter_list(l):
  return [item for item in l if item is not str(item)]
def filter_list_v2(l):
  return [item for item in l if not isinstance(item, str)]
# print(filter_list([1,2,'aasf','1','123',123]) == [1,2,123])


## Decode morse_code
MORSE_CODE = {
  '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
  '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
  '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
  '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
  '-.--': 'Y', '--..': 'Z',
  '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
  '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
  '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
  '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
  '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
  '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}

def decodeMorse(morse_code):
  morse_code_part = morse_code.strip().split(' ')
  space_cnt = 0
  output = ''
  for ele in morse_code_part:
    if ele is '':
      space_cnt += 1
      if space_cnt == 2:
        space_cnt = 0
        output += ' '
    else:
      output += MORSE_CODE[ele]
  return output

def decodeMorse_v2(morse_code):
    return ' '.join([
                     ''.join([MORSE_CODE[code] for code in word.split(' ')])
                     for word in morse_code.strip().split('   ')
                    ])

# print(decodeMorse_v2(".... . -.--   .--- ..- -.. ."))




## persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
##                       # 1*2*6 = 12, and finally 1*2 = 2.

def persistence(n):
  factors = list(str(n))
  cnt = 0
  if len(factors) <= 1:
    return 0
  res = int(factors[0])
  for i in range(1, len(factors)):
    res *= int(factors[i])
    cnt = persistence(res)
  return cnt + 1

from functools import reduce
## reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
def persistence_v2(n):
  factors = [int(x) for x in str(n)]
  i = 0
  while len(factors) > 1:
    res = reduce(lambda x, y: x*y, factors)
    i += 1
    factors = [int(x) for x in str(res)]
  return i
# print(persistence_v2(999))


def get_sign(x):
  return (x > 0) - (x < 0)

# print(get_sign(-1))

## Write a function to calculate the absolute value of a 32-bit integer
def myabs(x):
  high_bit_mask = x >> 31
  return (x ^ high_bit_mask) - high_bit_mask

# print(myabs(7))

# import random
# print(random.randrange(10))


## Dig Pow 89 = 8^1 + 9^2
def sum_dig_pow(a, b):# range(a, b + 1) will be studied by the function
  output = []
  for num in range(a, b+1):
    parts = list(str(num))
    new_num = 0
    for exp, base in enumerate(parts, 1):
      new_num += (int(base))**exp
    if num == new_num:
      output.append(num)
  return output


def dig_pow(n):
  return sum([int(y)**x for x, y in enumerate(str(n), 1)])
def sum_dig_pow_v2(a, b):
  return [num for num in range(a, b+1) if num == dig_pow(num)]

# print(sum_dig_pow_v2(89,135))


def countBits(n):
  count = 0
  while n > 0:
    n = n & (n - 1)
    count += 1
  return count


# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
def unique_in_order(iterable):
  unique = []
  prev = None
  for char in iterable:
    if char != prev:
      unique.append(char)
      prev = char
  return unique

# print(unique_in_order([]))


def duplicate_count(text):
  ## str.count(sub) count the ocurrences of substring
  occurs = [text.lower().count(char_cnt) for char_cnt in list(set(list(text.lower)))]
  cnt = 0
  for num in occurs:
    if num > 1:
      cnt += 1
  return cnt

def duplicate_count_v2(text):
  return len([c for c in set(text.lower()) if text.lower().count(c) > 1])
# print(duplicate_count_v2("aaBbccddeeffgg"))



# add 2 integers using bitwise operations
# but need to deal with special case a < 0; b > 0 abs(a) < b

def add(a, b):
  while a:
    b, a = b ^ a, (b & a) << 1
  return b
print(add(-1, -800))


def reverseWords(str):
  return ' '.join(str.split(' ')[::-1])

# print(reverseWords("hello world"))



## if a portion of str1 characters can be rearranged to match str2,
## otherwise returns false.
# Only lower case letters will be used (a-z).
# No punctuation or digits will be included.
# Performance needs to be considered.
# scramble('rkqodlw', 'world') ==> True
# scramble('katas', 'steak') ==> False

##cost time 4861ms
def scramble_v1(s1,s2):
  for c in set(s2):
    if s1.count(c) < s2.count(c):
      return False
  return True

##cost time 5865ms
def scramble_v2(s1, s2):
  s1_dict = {}
  s2_dict = {}
  for char in s1:
    if char in s1_dict:
      s1_dict[char] += 1
    else:
      s1_dict[char] = 1
  for char in s2:
    if char in s2_dict:
      s2_dict[char] += 1
    else:
      s2_dict[char] = 1
  for k, v in s2_dict.items():
    if s1_dict.get(k, 0) >= v:
      continue
    else:
      return False
  return True


## cost time 6396ms
def scramble_v3(s1, s2):
  h = [0] * 26
  for char in s1:
    h[ord(char) - 97] += 1
  for char in s2:
    h[ord(char) - 97] -= 1
  for i in h:
    if i < 0:
      return False
  return True



## Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42.
## These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764.
## The sum of the squared divisors is 2500 which is 50 * 50, a square!
## Given two integers m, n (1 <= m <= n) we want to find all integers between m and n
## whose sum of squared divisors is itself a square. 42 is such a number.

import math
def list_squared(m, n):
  res = []
  for num in range(m, n+1):
    i = 1
    sum = 0
    while i <= math.sqrt(num):  # all the divisors present in pairs
      if num % i == 0:
        div = num // i
        sum += i**2
        if div != i:
          sum += div**2
      i += 1
    if math.sqrt(sum).is_integer():
      res.append([num, sum])
  return res



## If the input number is already a palindrome, the number of steps is 0.
## Input will always be a positive integer.
##For example, start with 87:
## 87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884
##4884 is a palindrome and we needed 4 steps to obtain it, so palindrome_chain_length(87) == 4

def is_palindrome(n):
  return str(n) == str(n)[::-1]
def palindrome_chain_length(n):
  step = 0
  while not is_palindrome(n):
    n += int(str(n)[::-1])
    step += 1
  return step

# print(palindrome_chain_length(87))




## Breadcrumb Generator

ignore_words = ["the", "of", "in", "from", "by", "with", "and",
                "or", "for", "to", "at", "a"
                ]
def generate_bc(url, separator):
  if url.startswith("http"):
    url = url.split("//")[1]
  crumb = url.split('/')
  crumb[-1] = crumb[-1].split('.')[0].split('?')[0].split('#')[0]
  if crumb[-1] in ('', 'index'):
    crumb.pop()

  n = len(crumb)
  processed_parts = []
  for i, level in enumerate(crumb):
    aux = level
    if i == 0:
      if n == 1:
        processed_parts.append('<span class="active">HOME</span>')
      else:
        processed_parts.append('<a href="/">HOME</a>')
    else:
        if len(level) > 30:
          aux = ''.join([entry[0] for entry in level.split('-')
                          if entry not in ignore_words
                          ])
        else:
          aux = ' '.join(aux.split('-'))
        if i > 1 and i <= n - 2:
          level = "/".join(crumb[1:i+1])
        if i == n - 1:
          processed_parts.append('<span class="active">%s</span>' % aux.upper())
        else:
          processed_parts.append('<a href="/%s/">%s</a>' % (level, aux.upper()))
  return separator.join(processed_parts)



## hamming number
# Write a function that computes the nth smallest Hamming number.

# Specifically:

# The first smallest Hamming number is 1 = 2^0 * 3^0 * 5^0
# The second smallest Hamming number is 2 = 2^1 * 3^0 * 5^0
# The third smallest Hamming number is 3 = 203150
# The fourth smallest Hamming number is 4 = 223050
# The fifth smallest Hamming number is 5 = 203051
def hamming(n):
  hamm = [0 for num in range(n)]
  hamm[0] = 1
  a, b, c = 0, 0, 0
  for i in range(1, n):
    hamm[i] = min(hamm[a] * 2, hamm[b] * 3, hamm[c] * 5)
    if hamm[i] == hamm[a] * 2: a += 1
    if hamm[i] == hamm[b] * 3: b += 1
    if hamm[i] == hamm[c] * 5: c += 1
  return hamm[-1]

## original version also bad code
hamset = {1:1}
divisors = [2, 3, 5]
def hamming_v2(n):
  if hamset.get(n) is not None:
    return hamset[n]

  i = list(hamset.keys())[-1] + 1

  while i <= n:
    now = hamset[i - 1]
    find = False
    while not find:
      now += 1
      rem = now
      for div in divisors:
        while (rem / div).is_integer():
          rem = rem / div
          if rem == 1:
            hamset[i] = now
            find = True
            break
        if find is True:
          break
    i += 1
  return hamset[n]



# Strip Comments
# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

def solution(string,markers):
  parts = string.split('\n')

  for m in markers:
    parts = [p.split(m)[0].rstrip() for p in parts]
  print(parts)
  return '\n'.join(parts)

# solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

# Original Version
def solution_v2(string,markers):
  strip = 0
  s = list(string)
  for i in range(len(string)):
    if s[i] in markers:
      strip = 1
      if s[i - 1] == ' ':
        s[i - 1] = ''
    if s[i] == "\n":
      strip = 0
    if strip == 1:
      s[i] = ''
  return ''.join(s)



# How many numbers III?
# Generate all the numbers of three digits that:
# the value of adding their corresponding ones(digits) is equal to 10.
# their digits are in increasing order (the numbers may have two or more equal contiguous digits)
# The numbers that fulfill the two above constraints are: 118, 127, 136, 145, 226, 235, 244, 334

import itertools
def find_all(sum_dig, digs):
  res = []
  aux = list(itertools.combinations_with_replacement(range(1, 10), digs))
  res = [''.join([str(num) for num in t]) for t in aux if sum(t) == sum_dig]
  if res == []:
    return []
  return [len(res), int(min(res)), int(max(res))]


