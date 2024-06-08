let heading = document.getElementById("heading")
const date = new Date();
pointer = date.setTime(date.getTime() + (30 * 24 * 60 * 60 * 1000));
heading.textContent = pointer;

