import React, { useState, useContext } from "react";
import "./Login.css";
import { useFormik } from "formik";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { useNavigate } from "react-router-dom";
import { env } from "../../config";
import load from "../../asset/loading2.svg";
import UserContext from "../Context/usercContext";
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import AdminContext from "../Context/adminContext";


function Login() {
  const context = useContext(UserContext)
  const context1 = useContext(AdminContext);
  const { setUsername,productData } = context
  const { getDashboardProduct,getDashboardOverview,getDashboardBarChart,getUser,getOrder } = context1

  let navigate = useNavigate();
  let [loading, setloading] = useState(false);
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  //const handleShow = () => setShow(true);


  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
    validate: (values) => {
      const errors = {};
    
      if (values.email.length === 0) {
        errors.email = "Enter your email address";
      } else if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(values.email)) {
        errors.email = "Please provide a valid email address";
      }
      if (values.password.length === 0) {
        errors.password = "Enter your password";
      }
    
      return errors;
    },

    onSubmit: async (values) => {
      try {
        setloading(true)
        let value = await axios.post(`${env.api}/login`, values);
        const { data } = value;
        const { isAdmin, message, name, statusCode, token, user } = data;
        if (statusCode === 200) {
        console.log(values);

          setloading(false)
          window.sessionStorage.setItem("token", token);
          window.sessionStorage.setItem("name", name);
          window.sessionStorage.setItem("isAdmin", isAdmin);
          window.sessionStorage.setItem("userId", user._id);
          toast.success(message);

          setTimeout(() => {
            if (isAdmin) {
              getOrder()
              getUser()
              getDashboardProduct()
              getDashboardOverview()
              getDashboardBarChart(new Date().getFullYear())
              navigate("/home");
            }
            else {
              setUsername(name)
              productData()
              navigate("/user-portal")

            } 
          
          },350);
        }

        if (statusCode === 401) {
          setloading(false)
          toast.warn(message);
        }
        if (statusCode !== 200) {
          setloading(false)
          toast.warn(message);
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
          onSubmit={(values) => {
            formik.handleSubmit(values);
          }}
        >
          <h4 className="login_hed">Login</h4>
          <div className="mb-3">
            <label htmlFor="exampleInputEmail1" className="form-label">
              UserName
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
              placeholder="Enter you Password"
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
              <img
                src={load}
                alt="load"
                className="spinner"
              />
            ) : "Login"}

          </button>
          <div className="mt-3 new_user">
            <span>
              Dont't have an account?{" "}
              <span
                className="sign_color"
                onClick={() => navigate("/register")}
              >
                Sign up now
              </span>
            </span>
          </div>
        </form>
        <ToastContainer />
      </div>
      <Modal show={show} onHide={handleClose} animation={false}>
        <Modal.Header closeButton>
          <Modal.Title><h5 className="ttt">Login Successful..</h5> </Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <h5 className="fff">Your request Send to Admin.Plz Wait for conformation..!!!</h5>
         
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default Login;