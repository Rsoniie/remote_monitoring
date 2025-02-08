const login = document.querySelector("#login");
const form = document.querySelector("#form");
const user = document.querySelector("#user");
const pass = document.querySelector("#pass");
const submit = document.querySelector("#submit");
const show = document.querySelector("#show");
const data = document.querySelector("#current");
data.style.display = "none";
form.style.display = "none";

login.addEventListener("click", (event) => {
  event.preventDefault();
  form.style.display = "block";
});



submit.addEventListener("click", async (event) => {
  event.preventDefault();

  const username = user.value;
  const password = pass.value;

  form.style.display = "none";

  try {
    const response = await fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });

    if (!response.ok) {
      throw new Error(`Enter correct credentials: ${response.status}`);
    }

    const data = await response.json();
    localStorage.setItem("username", data.username);
    console.log(data.username);
    console.log(data.message);
  } catch (error) {
    console.error("Error:", error);
    alert(error.message);
  }
});


show.addEventListener("click", (event) => {
    event.preventDefault();
    if(data.style.display == 'none')
    {
        show.innerHTML = "hide";
        data.style.display = 'block';
    }
    else 
    {
        show.innerHTML = "show";
        data.style.display = 'none';
    }
})

