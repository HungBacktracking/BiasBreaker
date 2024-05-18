import classes from './Header.module.css';
import './Header.module.css';
import Navbar from '../Navbar/Navbar';
import InputSearch from './InputSearch';
import React, { useState } from 'react';


function Header() {
  return (
    <>
      <header className={classes.header}>
        <div className={classes.header_top}>
          <a className={classes.header_logo} href="/">
            <span className={classes.logo_img}></span>
            <span className={classes.logo_title}>Tin tức</span>
          </a>

          <InputSearch />

          <div className={`ms-auto flex`}>
            <div className={classes.user_state}>
                <p className={classes.user_role}>Admin</p>
                <div className={classes.status}>
                    <div className={`${classes.status_icon} ${classes.online}`}></div>
                    <p className={classes.status_text}>online</p>
                </div>
            </div>
            <img className={`${classes.avatar} ${classes.circle}`} src="/image/avatar_full.jpg" alt="Avatar"/>
          </div>
        </div>
        <Navbar />
      </header>
    </>
  );
}

export default Header;