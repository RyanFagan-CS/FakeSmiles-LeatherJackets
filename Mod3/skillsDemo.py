# Mod 3 Skills Demo
qoute = "Code never lies, comments sometimes do"
# Calculate the length of the string & display it
print("Length of qoute", len(qoute))
# Add a new line after the comma & display it
qouteWithNewLine = qoute.replace(",",",\n")
print("qoute with new line", qouteWithNewLine)
# Make every character in the string capitalized & display it
print("All uppercase", qoute.upper())
# Use slicing to grab just "Code never lies" out of the string.
part = qoute[:15]
print("Sliced Part of qoute", part)
# Then, calculate the length of the substring and concatenate it onto the end of
#the substring. Display this.
partAndLength = part + str(len(part))
print("Part and Length", partAndLength)

