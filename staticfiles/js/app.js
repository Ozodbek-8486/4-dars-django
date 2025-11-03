// // Password toggle functionality
// const togglePassword = document.getElementById("togglePassword")
// const passwordInput = document.getElementById("password")
// const eyeIcon = document.getElementById("eyeIcon")

// togglePassword.addEventListener("click", () => {
//   const type = passwordInput.getAttribute("type") === "password" ? "text" : "password"
//   passwordInput.setAttribute("type", type)

//   if (type === "text") {
//     eyeIcon.innerHTML =
//       '<path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line>'
//   } else {
//     eyeIcon.innerHTML =
//       '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle>'
//   }
// })

// // Form submission
// const registerForm = document.getElementById("registerForm")
// registerForm.addEventListener("submit", (e) => {
//   e.preventDefault()

//   const formData = {
//     username: document.getElementById("username").value,
//     firstName: document.getElementById("firstName").value,
//     lastName: document.getElementById("lastName").value,
//     email: document.getElementById("email").value,
//     password: document.getElementById("password").value,
//   }

//   console.log("Registration data:", formData)
//   alert("Ro'yxatdan o'tish muvaffaqiyatli! (Bu demo versiya)")
// })

// // Social login buttons
// document.getElementById("googleBtn").addEventListener("click", () => {
//   console.log("Google login clicked")
//   alert("Google orqali kirish (Bu demo versiya)")
// })

// document.getElementById("twitterBtn").addEventListener("click", () => {
//   console.log("Twitter login clicked")
//   alert("Twitter orqali kirish (Bu demo versiya)")
// })

// document.getElementById("linkedinBtn").addEventListener("click", () => {
//   console.log("LinkedIn login clicked")
//   alert("LinkedIn orqali kirish (Bu demo versiya)")
// })
