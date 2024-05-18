import classes from './Navbar.module.css';

function Navbar() {
  return (
    <>
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
    </>
  );
  
}

export default Navbar;
