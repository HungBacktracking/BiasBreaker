import classes from './Header.module.css';
import './Header.module.css';
import React, { useState } from 'react';


function Header() {
  const [input, setInput] = useState('');

  const handleInputChange = (e) => {
    setInput(e.target.value);
  }

  return (
    <>
      <header className={classes.header}>
        <div className={classes.header_top}>
          <a className={classes.header_logo} href="/">
            <span className={classes.logo_img}></span>
            <span className={classes.logo_title}>Tin tức</span>
          </a>

          <div className={classes.search_noti}>
            <form method="post" action="/search">
              <div className={`${classes.the_input_search} ${classes.ml_6}`}>
                <div className={classes.t_popper}>
                  <div className={classes.t_popper__trigger}>
                    <div className={`${classes.t_text_field__wrapper} ${classes.t_text_field___lg}`}>
                      <span className={classes.t_text_field__prefix}><i className={`${classes.t_text_field__prefix_icon} ${classes.i_ui_search}`}></i></span> 
                      <input onChange={handleInputChange} enterkeyhint="search" required name="search" inputmode="search" placeholder="Tìm kiếm chủ đề và các tin tức nóng hổi" autocomplete="off" type="text" value={input} className={classes.t_text_field}/> 
                      <span className={classes.t_text_field__suffix}><i className={classes.t_text_field__clearable}></i></span>
                    </div>
                  </div> 
                </div>
              </div>
            </form>
            <i className={classes.noti_icon}></i>
          </div>

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

        <div className={classes.header_bottom}>
          <div className={classes.header_bottom_wrapper}>
            <div className={classes.header_bottom_wrapper_2}>
              <div className={classes.nav_bar_item}>
                <a className={classes.nav_link} href="#">Trang chủ</a>
              </div>
              <div className={classes.nav_bar_item}>
                <a className={classes.nav_link} href="#">Dành cho bạn</a>
              </div>
              <div className={classes.nav_bar_item}>
                <a className={classes.nav_link} href="#">Thịnh hành</a>
              </div>
              <div className={classes.separate_wrapper}>
                <div className={classes.separate}></div>
              </div>
              <div className={classes.nav_bar_item}>
                <a className={classes.nav_link} href="#">Việt Nam</a>
              </div>
              <div className={classes.nav_bar_item}>
                <a className={classes.nav_link} href="#">Thế giới</a>
              </div>
              <div className={classes.nav_bar_item}>
                <a className={classes.nav_link} href="#">Kinh tế</a>
              </div>
              <div className={classes.nav_bar_item}>
                <a className={classes.nav_link} href="#">Giải trí</a>
              </div>
              <div className={classes.nav_bar_item}>
                <a className={classes.nav_link} href="#">Thể thao</a>
              </div>
            </div>
          </div>

        </div>
      </header>
    </>
  );
}

export default Header;
