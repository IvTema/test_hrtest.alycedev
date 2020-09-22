# test_hrtest.alycedev
This repository for http://hrtest.alycedev.com/

Underlying business rules:
- Business logic rule 1 - basket never can give more than 1 apple per minute
- Business logic rule 2 - user never can have apples with both odd and even ids

Test scenarios:
  1. Check grab button works properly
  2. Check all odd apples can be add to user from basket
  3. Check all even apples can be add to user from basket
  4. Check even cant be added than user have odd
  5. Check odd cant be added than user have even
  6. Check alert can't add apple in 60 second after add
  7. Check alert can't add even apple to user odd apples
  8. Check alert can't add odd apple to user even apples
  9. Check alert can't add apple than basket empty

Bug report:
  1. Basket gives apples after 5 second delay - not 60 second
  2. After using "Free Apples" button apples can be added only after 5 second
 
Automation issues:
  1. Cant to realize 6th scenario(Check alert can't add apple in 60 second after add) due to no stable element to bind it to Explicit Waits

Usability recommendation:
  1. Make "Grab apple" button disabled for time lapse than apple can't be added after button using. It will support user and automation
