import React from 'react';
import gf from '../imgs/gf.png';
class MenuHeader extends React.Component{
      render(){
            return(<div className="footer">
                  <span className="info">
                  <img
                        className="gfImage hmargin"
                        src={gf}
                        alt="glutenfree symbol"
                  /> betyr glutenfritt
                  </span>
            </div>);
      }
}
export default MenuHeader;
