//UserContext.js
import { createContext, useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { env } from "../../config";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";


const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [admin, setAdmin] = useState(null);
  const [product, setProduct] = useState([]);
  const [orders, setOrders] = useState([]);
  const [data, setData] = useState(null);

  const API_URL = "http://localhost:5000";

  useEffect(() => {
    productData()
  }, []);

  useEffect(() => {
    productData()
  }, [orders]);

  useEffect(() => {
    checkSession()
  }, [orders]);

  const checkSession = async () => {
    try {
      const response = await axios.get(`${API_URL}/check-session`);
      if (response.data.isAdmin) {
        setAdmin(response.data);
        navigate("/admin-dashboard");
      } else if (response.data.user) {
        setUser(response.data);
        navigate("/user-dashboard");
      } else {
        navigate("/login");
      }
    } catch (error) {
      console.error(error);
      navigate("/login");
    }
  };
  
  const login = async (credentials) => {
    try {
      const response = await axios.post(`${API_URL}/login`, credentials);
      if (response.data.isAdmin) {
        setAdmin(response.data);
        navigate("/admin-dashboard");
      } else {
        setUser(response.data);
        navigate("/user-dashboard");
      }
    } catch (error) {
      console.error(error);
      toast.error("Invalid credentials. Please try again.");
    }
  };
  
  const logout = async () => {
    try {
      await axios.post(`${API_URL}/logout`);
      setUser(null);
      setAdmin(null);
      navigate("/login");
    } catch (error) {
      console.error(error);
    }
  };
  
  const signup = async (userData) => {
    try {
      await axios.post(`${API_URL}/register`, userData);
      toast.success("Account created successfully. Please log in.");
      navigate("/login");
    } catch (error) {
      console.error(error);
      toast.error("Error creating account. Please try again.");
    }
  };
  

  const productData = async () => {
    try {
      let value;
      value = await axios.get(`${env.api}/inventory/products`);
      setProduct(value.data.data);
    } catch (error) {
      console.log(error);
    }
  };

  const setOrderz = async (data) => {
    const { paymenttype } = data;
    if (paymenttype === "online_payment") {
      navigate("/user-portal/razorpay")
    } else {
      let mongo_id = await axios.post(`${env.api}/orders/order`, data);
      setOrders({});
      navigate(`/user-portal/order-success/${mongo_id.data.id}`)
    }
  }


  const getInvoice = async (id) => {
    try {
      let value = await axios.get(`${env.api}/orders/invoice/${id}`);
      setData(value.data);
      navigate(`/user-portal/order-success/invoice`)
    } catch (error) {
      console.log(error);
    }
  };


  return (
    <UserContext.Provider value={{ user,setUser, setUser, setProduct, orders, setOrders, setOrderz, data, getInvoice, productData ,product, checkSession,
      login,
      signup,
      logout,}}>
      {children}
    </UserContext.Provider>
  );
};

export default UserContext;