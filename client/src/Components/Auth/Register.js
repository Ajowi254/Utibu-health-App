import React, { useState } from "react";
import { useFormik } from "formik";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { useNavigate } from "react-router-dom";
import { env } from "../../config";
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

      function validateMobile(mobilenumber) {
        var regmm = /^([0-9]{10})$/; 
        if (values.mobile.length === 0) {
          return (errors.mobile = "Enter your mobile number");
        }
        if (regmm.test(mobilenumber)) {
          return errors;
        } else {
          return (errors.mobile = "Please provide a valid mobile number");
        }
      }

      validateMobile(values.mobile);

      if (values.password.length === 0) {
        errors.password = "Enter your password";
      } else if (!/[a-z]/i.test(values.password)) {
        errors.password = "Your password must contain at least one letter";
      } else if (!/\d/.test(values.password)) {
        errors.password = "Your password must contain at least one digit";
      } else if (values.password.length < 8) {
        errors.password = "Your password must be at least 8 characters";
      }
      if (values.conformPassword !== values.password) {
        errors.conformPassword = "Confirm password does not match";
      } else if (values.conformPassword.length === 0) {
        errors.conformPassword = "Enter your confirm password";
      }
      return errors;
    },

    onSubmit: async (values) => {
      try {
        delete values.conformPassword;
        setloading(true);
        let user = await axios.post(`${env.api}/register`, values); 
        const { data } = user;
        const { message, statusCode } = data;
        if (statusCode === 201) {
          setloading(false);
          toast.success(message);
          setTimeout(() => {
            navigate("/"); 
          }, 700);
        } else {
          setloading(false);
          toast.warn(message);
        }
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
          onSubmit={formik.handleSubmit}
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
            <label className="form-label">Mobile</label>
            <input
              type="text"
              className="form-control shadow-none"
              placeholder="Enter your mobile number"
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
              placeholder="Enter your Confirm Password"
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
              <img
                src={load}
                alt="load"
                className="spinner"
              />
            ) : "Sign Up"}
          </button>
          <div className="mt-3 new_user">
            <span>
              Already have an account?{" "}
              <span className="sign_color" onClick={() => navigate("/")}>
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
