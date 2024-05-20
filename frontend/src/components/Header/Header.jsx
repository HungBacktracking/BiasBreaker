import React from 'react';
import { useState, useEffect, useContext } from 'react';
import { Link } from 'react-router-dom';
import classes from './Header.module.css';
import './Header.module.css';
import Navbar from './Navbar/Navbar';
import InputSearch from './InputSearch';
import Button from '../Button/Button';
import { AuthContext } from '../../auth/AuthContext';
import { IoIosArrowRoundForward } from 'react-icons/io';

function Header() {

  const { isLoggedIn } = useContext(AuthContext);


  return (
    <>
      <header className={classes.header}>
        <div className={classes.header_top}>
          <a className={classes.header_logo} href="/">
            <span className={classes.logo_img}></span>
            <span className={classes.logo_title}>Tin tức</span>
          </a>

          <InputSearch />

          <div className={`ms-auto flex ${classes.center}`}>
            { isLoggedIn ? (
              <>
                <div className={classes.user_state}>
                  <p className={classes.user_role}>Admin</p>
                  <div className={classes.status}>
                    <div className={`${classes.status_icon} ${classes.online}`}></div>
                    <p className={classes.status_text}>online</p>
                  </div>
                </div>
                <img className={`${classes.avatar} ${classes.circle}`} src="/image/avatar_full.jpg" alt="Avatar" />
              </>
            ) : (
              <Link to="/sign-in">
                <Button>
                  Đăng nhập <IoIosArrowRoundForward className="text-lg font-semibold" />
                </Button>
              </Link>
            )
            }
          </div>
        </div>
        <Navbar />
      </header>
    </>
  );
}

export default Header;
