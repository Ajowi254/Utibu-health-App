import React, { useState } from "react";
import { useFormik } from "formik";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { useNavigate } from "react-router-dom";
import load from "../../asset/loading2.svg";

function Register() {
  let navigate = useNavigate();
  let [loading, setloading] = useState(false);

  const formik = useFormik({
    initialValues: {
      name: "",
      email: "",
      mobile: "",
      password: "",
      conformPassword: "",
    },
    validate: (values) => {
      const errors = {};

      if (values.name.length === 0) {
        errors.name = "Enter your name";
      }
      if (values.email.length === 0) {
        errors.email = "Enter your email address";
      } else if (!/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/.test(values.email)) {
        errors.email = "Please provide a valid email address";
      }

      if (values.mobile.length === 0) {
        errors.mobile = "Enter your mobile number";
      } else if (!/^[0-9]{10}$/.test(values.mobile)) {
        errors.mobile = "Please provide a valid 10-digit mobile number";
      }

      if (values.password.length === 0) {
        errors.password = "Enter your password";
      } else if (!/(?=.*[A-Za-z])(?=.*\d).{8,}/.test(values.password)) {
        errors.password = "Your password must contain at least one letter, one digit, and be at least 8 characters long";
      }

      if (values.conformPassword !== values.password) {
        errors.conformPassword = "Confirm password does not match";
      } else if (values.conformPassword.length === 0) {
        errors.conformPassword = "Enter your confirm password";
      }

      return errors;
    },

    onSubmit: (values) => {
      try {
        setloading(true);
        localStorage.setItem("name", values.name);
        localStorage.setItem("email", values.email);
        localStorage.setItem("mobile", values.mobile);
        localStorage.setItem("password", values.password);

        setloading(false);
        toast.success("Registration successful!");

        setTimeout(() => {
          navigate("/");
        }, 700);
      } catch (error) {
        console.log(error);
      }
    },
  });

  return (
    <>
      <div className="containers">
        <form
          className="form"
          onSubmit={(e) => {
            e.preventDefault();
            formik.handleSubmit();
          }}
        >
          <h4 className="text-center mb-4">Register Form</h4>
          <div className="mb-3">
            <label className="form-label">Name</label>
            <input
              type="text"
              className="form-control shadow-none"
              placeholder="Enter your name"
              value={formik.values.name}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              name="name"
            />
            {formik.touched.name && formik.errors.name ? (
              <div className="error"> {formik.errors.name}</div>
            ) : null}
          </div>
          <div className="mb-3">
            <label className="form-label">Email</label>
            <input
              type="email"
              className="form-control shadow-none"
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
            <label className="form-label">Mobile Number</label>
            <input
              type="text"
              className="form-control shadow-none"
              placeholder="Enter your 10-digit mobile number"
              value={formik.values.mobile}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              name="mobile"
            />
            {formik.touched.mobile && formik.errors.mobile ? (
              <div className="error"> {formik.errors.mobile}</div>
            ) : null}
          </div>
          <div className="mb-3">
            <label className="form-label">Password</label>
            <input
              type="password"
              className="form-control shadow-none"
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
          <div className="mb-3">
            <label className="form-label">Confirm Password</label>
            <input
              type="password"
              className="form-control shadow-none"
              placeholder="Confirm your Password"
              value={formik.values.conformPassword}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              name="conformPassword"
            />
            {formik.touched.conformPassword && formik.errors.conformPassword ? (
              <div className="error"> {formik.errors.conformPassword}</div>
            ) : null}
          </div>
          <button type="submit" className="btns btn" disabled={!formik.isValid}>
            {loading ? (
              <img src={load} alt="load" className="spinner" />
            ) : "Sign Up"}
          </button>
          <div className="mt-3 new_user">
            <span>
              Already have an account?{" "}
              <span className="sign_color" onClick={() => navigate("/login")}>
                Sign in now
              </span>
            </span>
          </div>
        </form>
        <ToastContainer />
      </div>
    </>
  );
}

export default Register;
