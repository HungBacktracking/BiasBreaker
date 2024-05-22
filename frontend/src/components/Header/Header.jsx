import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import classes from './Header.module.css';
import './Header.module.css';
import Navbar from './Navbar/Navbar';
import InputSearch from './InputSearch';
import Button from '../Button/Button';
import { IoIosArrowRoundForward } from 'react-icons/io';

function Header() {
  const navigate = useNavigate();
  function handleClick() {
    navigate('/sign-up');
  }
  return (
    <>
      <header className={classes.header}>
        <div className={classes.header_top}>
          <a className={classes.header_logo} href="/">
            <span className={classes.logo_img}></span>
            <span className={classes.logo_title}>Tin tức</span>
          </a>

          <InputSearch />

          <div className={`ms-auto flex gap-3`}>
            {/* <div className={classes.user_state}>
              <p className={classes.user_role}>Admin</p>
              <div className={classes.status}>
                <div className={`${classes.status_icon} ${classes.online}`}></div>
                <p className={classes.status_text}>online</p>
              </div>
            </div>
            <img className={`${classes.avatar} ${classes.circle}`} src="/image/avatar_full.jpg" alt="Avatar" /> */}
            <Link href="/about">
              <Button variant="stroke">About us</Button>
            </Link>
            <Button onClick={handleClick}>
              Sign up now <IoIosArrowRoundForward className="text-lg font-semibold" />
            </Button>
          </div>
        </div>
        <Navbar />
      </header>
    </>
  );
}

export default Header;
