###Python Multiline Strings
# Multiline string
message = """To avoid pain, they avoid pleasure.
To avoid death, they avoid life."""

print(message)

model = 'ChatGPT'
print(model[8])       # IndexError

###Strings are Immutable
model = 'ChatGPT'

model[0] = 'W'
print(model)

###String Membership Test
print('Chat' in 'ChatGPT')        # True
print('Claude' not in 'ChatGPT')  # True

###Iterate Through a String
model = 'Opus'

for c in model:
    print(c)

###Python String Length
model = 'Opus'

# Count the number of characters
print(len(model))   # Output: 4

###Escape Sequences
example = 'He said, "What\'s there?"'

print(example) # Error

###String Formatting (f-Strings)
company = 'Google'
field = 'AI'

message = f'{company} is an {field} company.'
print(message)