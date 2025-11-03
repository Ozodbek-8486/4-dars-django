// Parolni ko'rsatish/yashirish funksiyasi
const togglePassword = document.getElementById("togglePassword")
const passwordInput = document.getElementById("password")

togglePassword.addEventListener("click", function () {
  const type = passwordInput.getAttribute("type") === "password" ? "text" : "password"
  passwordInput.setAttribute("type", type)

  // Icon o'zgartirish
  const eyeIcon = this.querySelector(".eye-icon")
  if (type === "text") {
    eyeIcon.innerHTML = `
            <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
            <line x1="1" y1="1" x2="23" y2="23"></line>
        `
  } else {
    eyeIcon.innerHTML = `
            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
            <circle cx="12" cy="12" r="3"></circle>
        `
  }
})

// Forma yuborilganda
const loginForm = document.getElementById("loginForm")

loginForm.addEventListener("submit", (e) => {
  e.preventDefault()

  const email = document.getElementById("email").value
  const password = document.getElementById("password").value

  // Validatsiya
  if (!email || !password) {
    alert("Iltimos, barcha maydonlarni to'ldiring!")
    return
  }

  // Email formatini tekshirish
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!emailRegex.test(email)) {
    alert("Iltimos, to'g'ri email kiriting!")
    return
  }

  // Bu yerda backend ga so'rov yuboriladi
  console.log("Login ma'lumotlari:", {
    email: email,
    password: password,
  })

  alert("Kirish muvaffaqiyatli! (Bu demo versiya)")

  // Forma tozalash
  loginForm.reset()
})

// Ijtimoiy tarmoqlar tugmalari
const socialButtons = document.querySelectorAll(".social-btn")

socialButtons.forEach((button) => {
  button.addEventListener("click", function () {
    const buttonText = this.textContent.trim()
    console.log(`${buttonText} bosildi`)
    alert(`${buttonText} funksiyasi tez orada qo'shiladi!`)
  })
})

// Input animatsiyalari
const inputs = document.querySelectorAll("input")

inputs.forEach((input) => {
  input.addEventListener("focus", function () {
    this.parentElement.style.transform = "scale(1.01)"
  })

  input.addEventListener("blur", function () {
    this.parentElement.style.transform = "scale(1)"
  })
})
