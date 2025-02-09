const login = document.querySelector("#login");
const form = document.querySelector("#form");
const user = document.querySelector("#user");
const pass = document.querySelector("#pass");
const submit = document.querySelector("#submit");
const show = document.querySelector("#show");
const data = document.querySelector("#current");
const history = document.querySelector("#history");
const signup = document.querySelector("#signup");
const signup_form = document.querySelector("#signup_form");
const signup_submit = document.querySelector("#singup_submit");
const signup_username = document.querySelector("#signup_username");
const signup_email = document.querySelector("#signup_email");
const signup_password = document.querySelector("#signup_password");



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

// show.addEventListener("click", async (event) => {
//     event.preventDefault();
//       try{
//         const username = localStorage.getItem('username');
//         console.log(username);
//         const response = await fetch(`/show/${username}`, {
//           method : "GET",
//           headers : {
//             "Content-Type": "application/json"
//           }
//         })

//         const current_data = await response.json();        
//         show.innerHTML = "hide";
//         data.innerHTML = JSON.stringify(current_data["current_data"])
//         data.style.display = 'block';
//       }
//       catch(error)
//       {
//         alert(error.message)
//       }
    
// });


setInterval(async () => {
  try {
      const username = localStorage.getItem('username');
      console.log(username);
      const response = await fetch(`/show/${username}`, {
          method: "GET",
          headers: {
              "Content-Type": "application/json"
          }
      });

      const current_data = await response.json();
      show.innerHTML = "hide";
      data.innerHTML = JSON.stringify(current_data["current_data"]);
      data.style.display = 'block';
  } catch (error) {
      alert(error.message);
  }
}, 30000); 


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
    data.innerHTML = JSON.stringify(current_history);
    data.style.display = 'block';

  } catch (error) {
    alert(error.message);
  }
});

signup.addEventListener("click", async (event) => {
  event.preventDefault();
  signup_form.style.display = 'block'
});

signup_submit.addEventListener("click", async (event) => {
  event.preventDefault();
  try
  {
    signup_form.style.display = 'none';
    const username = signup_username.value;
    const email = signup_email.value;
    const password = signup_password.value;
    const response = await fetch('/add_user', {
      method: "POST",
      headers :{
        "Content-Type": "application/json"
      },
      body: JSON.stringify({username, email, password})
    })
    if(response.status == 200)
    {
      alert("User created sucessfully")
    }
    else{
      alert("Username already exist")
    }
  }catch(error)
  {
    alert(error.message);
  }
});














