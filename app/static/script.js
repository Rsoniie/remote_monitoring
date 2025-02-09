const login = document.querySelector("#login");
const form = document.querySelector("#form");
const user = document.querySelector("#user");
const pass = document.querySelector("#pass");
const submit = document.querySelector("#submit");
const show = document.querySelector("#show");
const data = document.querySelector("#current");
const history = document.querySelector("#history");
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


show.addEventListener("click", async (event) => {
    event.preventDefault();
    if(data.style.display == 'none')
    {


      try{
        const username = localStorage.getItem('username');
        console.log(username);
        const response = await fetch(`/show/${username}`, {
          method : "GET",
          headers : {
            "Content-Type": "application/json"
          }
        })

        const current_data = await response.json();        
        show.innerHTML = "hide";
        data.innerHTML = JSON.stringify(current_data["current_data"])
        data.style.display = 'block';
      }
      catch(error)
      {
        alert(error.message)
      }
    }
    else 
    {
        show.innerHTML = "show";
        data.innerHTML = "This is hiding state";
        data.style.display = 'none';
    }
});

history.addEventListener("click", async(event) => {
  event.preventDefault();
  try {
    const username = localStorage.getItem('username');
    // console.log(username);

    const response = await fetch(`/history/${username}`, {
      method: "GET",
      headers:{
        "Content-Type": "application/json"
      }
    })
    const current_history = await response.json();
    // console.log(current_history["history"]);
    data.innerHTML = JSON.stringify(current_history);
    data.style.display = 'block';

  } catch (error) {
    alert(error.message);
  }
})










