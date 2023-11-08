import React, { useState } from "react";
import { useFormik } from "formik";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { useNavigate } from "react-router-dom";
import load from "../../asset/loading2.svg";
import "./Login.css";

function Login() {
  let navigate = useNavigate();
  let [loading, setloading] = useState(false);

  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
    validate: (values) => {
      const errors = {};

      if (values.email.length === 0) {
        errors.email = "Enter your email address";
      } else if (values.email.search(/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/)) {
        errors.email = "Please provide a valid email address";
      }
      if (values.password.length === 0) {
        errors.password = "Enter your password";
      }

      return errors;
    },

    onSubmit: (values) => {
      try {
        setloading(true);
        const storedEmail = localStorage.getItem("email");
        const storedPassword = localStorage.getItem("password");

        if (values.email === storedEmail && values.password === storedPassword) {

          setloading(false);
          toast.success("Login successful!");

          setTimeout(() => {
            navigate("/dashboard"); 
          }, 350);
        } else {
          
          setloading(false);
          toast.warn("Invalid email or password. Please try again.");
        }
      } catch (error) {
        console.log(error);
      }
    },
  });

  return (
    <>
      <div className="containers  bg-transparent">
        <form
          className="form mb-5 "
          onSubmit={formik.handleSubmit}
        >
          <h4 className="login_hed">Login</h4>
          <div className="mb-3">
            <label htmlFor="exampleInputEmail1" className="form-label">
              Email
            </label>
            <input
              type="email"
              className="form-control shadow-none"
              id="exampleInputEmail1"
              placeholder="Enter your Email Id"
              value={formik.values.email}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              name="email"
            />
            {formik.touched.email && formik.errors.email ? (
              <div className="error"> {formik.errors.email}</div>
            ) : null}
          </div>
          <div className="mb-3">
            <label htmlFor="exampleInputPassword1" className="form-label ">
              Password
            </label>
            <input
              type="password"
              className="form-control shadow-none"
              id="exampleInputPassword1"
              placeholder="Enter your Password"
              value={formik.values.password}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              name="password"
            />
            {formik.touched.password && formik.errors.password ? (
              <div className="error"> {formik.errors.password}</div>
            ) : null}
          </div>
          <div className=" forgot ">
            <span onClick={() => navigate("/forgot-password")}>
              Forgot Password ?
            </span>
          </div>
          <button type="submit" className="btn btns" disabled={!formik.isValid}>
            {loading ? (
              <img src={load} alt="load" className="spinner" />
            ) : "Login"}
          </button>
          <div className="mt-3 new_user">
            <span>
              Don't have an account?{" "}
              <span className="sign_color" onClick={() => navigate("/register")}>
                Sign up now
              </span>
            </span>
          </div>
        </form>
        <ToastContainer />
      </div>
    </>
  );
}

export default Login;
