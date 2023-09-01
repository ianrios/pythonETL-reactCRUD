# Assignment 4 - React Table

## Steps for running Assignment 4 code

- Start via `docker compose up --build -d`
- navigate to `http://localhost:3000/`

## process from readme

- [x] implement a page displaying information from the api endpoint in [Assignment 3](#assignment-3---working-with-apis). This page does not have to be aesthetically pleasing, but it should have good usability. Though not required, feel free to use any third party tools or libraries to help complete the assignment.

## Success criteria

- [ ] The covid data table is paginated. Users may navigate to the `next` or `previous` pages.
- [x] The user can set "number of rows to display" to 25, 50, or 100
  - this may have been easier to achieve if the split was done purely on the backend, idk, i kinda like it now, but it could be improved
  - [ ] actually ^ do that

## Tasks

- [x] start react project
- [x] throw away any files we dont need for this small demo
- [x] configure front end to look pretty for demo - add styling and meta tags such as title and favicon
- [x] install packages (mui, virtualized, axios?)
- [x] choose a couple example mui tables to combine into one
- [x] combine current page, and total pages possible with current rows displayed to format pagination footer
- [ ] show nulls as "null"
- [ ] on click out of page bounds should pull query and build local size
- [ ] add buttons for last page, first page, etc
- [ ] split mui components out into their own files

## Optimizations to try

- [x] show off some react skills? context, etc? - this seems too small to require something like that
- [ ] localstorage caching?
- [ ] react testing

## Notes

- This one was the easiest and I needed a break from python so I worked on this one a bit after assignment 2 before working on assignment 3
- react isn't inherently difficult for me, so I didn't see the point in spending too much time on this one. I decided to spend my effort in the python code and actually make that look good.
- i think i made it more complex than it needed to be, but it looks good
