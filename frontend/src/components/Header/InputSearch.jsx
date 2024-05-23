import classes from './Header.module.css';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function InputSearch() {
  const [input, setInput] = useState('');
  const navigate = useNavigate();

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setInput('');
    navigate(`/keyword/${input}`);
  }

  return (
    <>
      <div className={classes.search_noti}>
        <form onSubmit={handleSubmit} action="">
          <div className={`${classes.the_input_search} ${classes.ml_6}`}>
            <div className={classes.t_popper}>
              <div className={classes.t_popper__trigger}>
                <div className={`${classes.t_text_field__wrapper} ${classes.t_text_field___lg}`}>
                  <span className={classes.t_text_field__prefix}>
                    <i className={`${classes.t_text_field__prefix_icon} ${classes.i_ui_search}`}></i>
                  </span>
                  <input
                    onChange={handleInputChange}
                    enterKeyHint="search"
                    required
                    name="search"
                    inputMode="search"
                    placeholder="Tìm kiếm chủ đề và các tin tức nóng hổi"
                    autoComplete="off"
                    type="text"
                    value={input}
                    className={classes.t_text_field}
                  />
                  <span className={classes.t_text_field__suffix}>
                    <i className={classes.t_text_field__clearable}></i>
                  </span>
                </div>
              </div>
            </div>
          </div>
        </form>
        <i className={classes.noti_icon}></i>
      </div>
    </>
  );
}

export default InputSearch;
