//AdminContext.js
import axios from "axios";
import { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { env } from "../../config";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

//
const AdminContext = createContext();

export const AdminProvider = ({ children }) => {
    const navigate = useNavigate();
    const [admin, setAdmin] = useState(null);
    const [brand, setBrand] = useState([]);
    const [category, setCategory] = useState([]);
    const [products, setProducts] = useState([]);
    const [dashboardProduct, setDashboardProduct] = useState([]);
    const [dashboardOverview, setDashboardOverview] = useState(null);
    const [dashboardBarChart, setDashboardBarChart] = useState(null);
    const [user, setUser] = useState(null);
    const [order, setOrder] = useState([]);

  const API_URL = "http://localhost:5000";

    useEffect(() => {
        getBrand();
    }, []);

    useEffect(() => {
        getCategory()
    }, []);

    useEffect(() => {
        checkSession()
    }, []);

    useEffect(() => {
        getproducts()
    }, []);

    useEffect(() => {
        getDashboardProduct()
    }, []);

    useEffect(() => {
        getDashboardProduct()
    }, [products]);


    useEffect(() => {
        getDashboardOverview()
    }, []);

    useEffect(() => {
        getDashboardOverview()
    }, [products]);

    useEffect(() => {
        getDashboardBarChart(new Date().getFullYear())
    }, []);

    useEffect(() => {
        getUser()
    }, []);

    useEffect(() => {
        getOrder()
    }, []);

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
      

    const getBrand = async (query) => {
        try {
            let value;
            if (!query) {
                value = await axios.get(`${env.api}/inventory/brand`);
            } else {
                value = await axios.get(`${env.api}/inventory/brand?q=${query}`);
            }
            setBrand(value.data.data);
        } catch (error) {
            console.log(error);
        }
    };

    const addBrand = async (values) => {
        try {
            let user = await axios.post(`${env.api}/inventory/Add-brand`, values);
            getBrand();
            const { data } = user;
            const { message, statusCode } = data;
            if (statusCode === 201) {
                navigate("/home/brand");
            } else {
                toast.warn(message);
            }
        } catch (error) {
            console.log(error);
        }
    };

    const editBrand = async (values, id) => {
        try {
            let value = await axios.put(`${env.api}/inventory/edit-brand/${id}`, values);
            getBrand();
            const { data } = value;
            const { message, statusCode } = data;
            if (statusCode === 200) {
                navigate("/home/brand");
            } else {
                toast.warn(message);
            }
        } catch (error) {
            console.log(error);
        }
    };

    const deleteBrand = async (id) => {
        try {
            let value = await axios.delete(`${env.api}/inventory/delete-brand/${id}`);
            getBrand();
            const { data } = value;
            const { message, statusCode } = data;
            if (statusCode === 200) {
                toast.success(message);
            } else {
                toast.warn(message);
            }
        } catch (error) {
            console.log(error);
        }
    };



    const getCategory = async (query) => {
        try {
            let value;
            if (!query) {
                value = await axios.get(`${env.api}/inventory/category`);
            } else {
                value = await axios.get(`${env.api}/inventory/category?q=${query}`);
            }
            setCategory(value.data.data);


        } catch (error) {
            console.log(error);
        }
    };

    const addCategory = async (values) => {
        try {
            let user = await axios.post(`${env.api}/inventory/add-category`, values);
            getCategory()
            const { data } = user;
            const { message, statusCode } = data;
            if (statusCode === 201) {
                navigate("/home/category");
            } else {
                toast.warn(message);
            }
        } catch (error) {
            console.log(error);
        }
    };

    const editCategory = async (values, id) => {
        try {
            let value = await axios.put(`${env.api}/inventory/edit-category/${id}`, values);
            getCategory()
            const { data } = value;
            const { message, statusCode } = data;
            if (statusCode === 200) {
                navigate("/home/category");
            } else {
                toast.warn(message);
            }
        } catch (error) {
            console.log(error);
        }
    };

    const deleteCategory = async (id) => {
        try {
            let value = await axios.delete(`${env.api}/inventory/delete-category/${id}`);
            getCategory();
            const { data } = value;
            const { message, statusCode } = data;
            if (statusCode === 200) {
                toast.success(message);
            } else {
                toast.warn(message);
            }
        } catch (error) {
            console.log(error);
        }
    };


    // product

    const getproducts = async (query) => {
        try {
            let value;
            if (!query) {
                value = await axios.get(`${env.api}/inventory/products`);
            } else {
                value = await axios.get(`${env.api}/inventory/products?q=${query}`);
            }
            setProducts(value.data.data);


        } catch (error) {
            console.log(error);
        }
    };

    const addProduct = async (values) => {
        try {
            let user = await axios.post(`${env.api}/inventory/add-product`, values);
            const { data } = user;
            const { message, statusCode } = data;
            if (statusCode === 201) {
                getproducts()
                navigate("/home/products");
            } else {
                toast.warn(message);
            }
        } catch (error) {
            console.log(error);
        }
    };



    const editProduct = async (values, id) => {
        try {
            let value = await axios.put(`${env.api}/inventory/edit-product/${id}`, values);
            const { data } = value;
            const { message, statusCode } = data;
            if (statusCode === 200) {
                getproducts()
                navigate("/home/products");
            } else {
                toast.warn(message);
            }
        } catch (error) {
            console.log(error);
        }
    };

    const deleteProduct = async (id) => {
        try {
            let value = await axios.delete(`${env.api}/inventory/delete-product/${id}`);
            const { data } = value;
            const { message, statusCode } = data;
            if (statusCode === 200) {
                getproducts();
                toast.success(message);
            } else {
                toast.warn(message);
            }
        } catch (error) {
            console.log(error);
        }
    };

    // Dashboard

    const getDashboardProduct = async (query) => {
        try {
            let value;
            if (!query) {
                value = await axios.get(`${env.api}/inventory/dashboard-products`);
            } else {
                value = await axios.get(`${env.api}/inventory/dashboard-products?q=${query}`);
            }
            const { data } = value;
            setDashboardProduct(data.products);
        } catch (error) {
            console.log(error);
        }
    };

    const getDashboardOverview = async () => {
        try {
            let value = await axios.get(`${env.api}/inventory/dashboard-overview`);
            const { data } = value;
            setDashboardOverview(data);
        } catch (error) {
            console.log(error);
        }
    };

    const getDashboardBarChart = async (query) => {
        try {
            console.log(query);
           
                let value = await axios.get(`${env.api}/inventory/dashboard-barChart/${query}`);
           
            const { data } = value;
            setDashboardBarChart(data);
        } catch (error) {
            console.log(error);
        }
    };


    const getUser = async () => {
        try {
            let value = await axios.get(`${env.api}/user/user-details`);
            const { data } = value;
            setUser(data.data)
        } catch (error) {
            console.log(error);
        }
    };

    const getOrder = async () => {
        try {
            let value = await axios.get(`${env.api}/orders/view-order`);
            const { data } = value;
            setOrder(data.data);
        } catch (error) {
            console.log(error);
        }
    };
    return (
        <AdminContext.Provider value={{
            admin, setAdmin, brand, getBrand, addBrand, editBrand, deleteBrand, category, addCategory, editCategory, deleteCategory,
            products, getproducts, addProduct, editProduct, deleteProduct, dashboardProduct, dashboardOverview, getCategory, user, getUser, order,
            getDashboardProduct, getDashboardOverview,checkSession, dashboardBarChart, getDashboardBarChart, getOrder, login,
            logout
        }}>
            {children}
        </AdminContext.Provider>
    );
};

export default AdminContext;

