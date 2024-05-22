import React, { useState, useContext } from 'react';
import CryptoJS from 'crypto-js';
import { Link, useNavigate } from 'react-router-dom';
import { AuthContext } from '../auth/AuthContext';

export default function SingIn() {
  const { login } = useContext(AuthContext);
  const [formData, setFormData] = useState({});
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const [error, setError] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.id]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Hash the password before sending to backend
    const hashedPassword = CryptoJS.SHA256(password).toString(CryptoJS.enc.Hex);

    const user = {
        email: email,
        password: hashedPassword,
    };

    try {
      setLoading(true);
      setError(false);
      const res = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
      });
      const data = await res.json();
      console.log(data);
      setLoading(false);
      if (!res.ok) {
        setError(true);
        return;
      }
      localStorage.setItem('email', data.email);
      login(data.access_token);
      navigate('/');
    } catch (error) {
      setLoading(false);
      setError(true);
    }
  };
  return (
    <div className="p-6 max-w-lg mx-auto bg-white rounded-xl translate-y-1/2">
      <h1 className="text-3xl text-center font-semibold my-7">Sign In</h1>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input
          type="email"
          placeholder="Email"
          id="email"
          className="bg-slate-100 p-3 rounded-lg"
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          id="password"
          className="bg-slate-100 p-3 rounded-lg"
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          disabled={loading}
          className="bg-green-700 text-white p-3 rounded-lg uppercase hover:opacity-95 disabled:opacity-80"
        >
          {loading ? 'Loading...' : 'Sign In'}
        </button>
      </form>
      <div className="flex gap-2 mt-5">
        <p>Don&apos;t have an account?</p>
        <Link to="/sign-up">
          <span className="text-green-700">Sign up</span>
        </Link>
      </div>
      <p className="text-red-700 mt-5">{error && 'Something went wrong!'}</p>
    </div>
  );
}
