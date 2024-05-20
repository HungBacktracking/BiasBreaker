import React from 'react';
import { NavLink } from 'react-router-dom';
import classes from './Navbar.module.css';

function Navbar() {
  return (
    <>
      <div className={classes.header_bottom}>
        <div className={classes.header_bottom_wrapper}>
          <div className={classes.header_bottom_wrapper_2}>
            <div className={classes.nav_bar_item}>
              <NavLink className={classes.nav_link} activeClassName={classes.active} exact to="/">
                Trang chủ
              </NavLink>
            </div>
            <div className={classes.nav_bar_item}>
              <NavLink className={classes.nav_link} activeClassName={classes.active} exact to="/for-you">
                Dành cho bạn
              </NavLink>
            </div>
            <div className={classes.nav_bar_item}>
              <NavLink className={classes.nav_link} activeClassName={classes.active} exact to="/trending">
                Thịnh hành
              </NavLink>
            </div>
            <div className={classes.separate_wrapper}>
              <div className={classes.separate}></div>
            </div>
            <div className={classes.nav_bar_item}>
              <NavLink className={classes.nav_link} activeClassName={classes.active} exact to="/category/thế giới">
                Thế giới
              </NavLink>
            </div>
            <div className={classes.nav_bar_item}>
              <NavLink className={classes.nav_link} activeClassName={classes.active} exact to="/category/chính trị">
                Chính trị
              </NavLink>
            </div>
            <div className={classes.nav_bar_item}>
              <NavLink className={classes.nav_link} activeClassName={classes.active} exact to="/category/kinh doanh">
                Kinh doanh
              </NavLink>
            </div>
            <div className={classes.nav_bar_item}>
              <NavLink className={classes.nav_link} activeClassName={classes.active} exact to="/category/giải trí">
                Giải trí
              </NavLink>
            </div>
            <div className={classes.nav_bar_item}>
              <NavLink className={classes.nav_link} activeClassName={classes.active} exact to="/category/thể thao">
                Thể thao
              </NavLink>
            </div>
            <div className={classes.nav_bar_item}>
              <NavLink className={classes.nav_link} activeClassName={classes.active} exact to="/category/du lịch">
                Du lịch
              </NavLink>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Navbar;
