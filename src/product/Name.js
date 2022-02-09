import React from 'react';
import gf from '../imgs/gf.png'; // gives image path
import none from '../imgs/none.png'; // gives image path

class Name extends React.Component{
      constructor(props){
            super();
            this.name = props.product.name;
            this.gf = props.product.glutenfree;
            this.info = props.product.info;

            console.log(this.info);
      }
      render(){
            var source = this.gf ? gf  : none;
            var alttxt = this.gf ? "glutenfree" : "not glutenfree"
            return(
                  <div className="productName">
                        <p className="noPadding">
                        {this.name +" "}
                        <img 
                              className="gfImage"
                              src={source}
                              alt={alttxt}/>
                              <i>{this.info}</i>
                        </p>
                  </div>
            )
      }
}
export default Name;
