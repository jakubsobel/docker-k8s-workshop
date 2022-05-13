async function getBookList() {
  const response = await fetch("http://localhost:8081/books");
  const books = await response.json();
  const list = document.querySelector("ul");

  books.forEach((book) => {
    const li = document.createElement("li");
    li.textContent = book.title;
    list.appendChild(li);
  });
}

getBookList();
