# Taltio-cleaner
Taltio cleaner is a toolset created to help MTEK (utu) data managers keep the taltio data storage clean. The main purpose of the toolset is to find users whom are not using Taltio at all, or are using it against the units data storage structures and naming conventions.

## How to use Taltio-cleaner
Clone the repository
```sh
git clone https://github.com/Teolhyn/taltio-checker.git
```
If you have Github CLI installed you can do
```sh
gh repo clone Teolhyn/taltio-checker
```
Then inside the local repository run
```sh
python taltio_cleaner.py
```

## Functionality

- [x] Find users who have not used taltio
- [x] Generate email-list from given users
- [x] Find users who use taltio
- [ ] Format checker
    - [x] Check ISO8601 timestamp
    - [x] Check whitespaces
    - [x] Check for files on wrong layers
    - [ ] Select depth of format checker
