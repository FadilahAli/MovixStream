import { getAuth } from "firebase/auth";
import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyCHv414KUPUywXIwph-IX_OdkUev7zOrR8",
  authDomain: "movixstream.firebaseapp.com",
  projectId: "movixstream",
  storageBucket: "movixstream.appspot.com",
  messagingSenderId: "543630040550",
  appId: "1:543630040550:web:b1c69e81d95cb94def8a27",
  measurementId: "G-Y7V6NEM132"
};

const app = initializeApp(firebaseConfig);
export const firebaseAuth = getAuth(app);


