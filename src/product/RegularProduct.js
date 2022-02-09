import React from 'react';
import Name from './Name.js'

class RegularProduct extends React.Component{
      render(){
      return (
            <div className="product">
                  <Name product={this.props.product} />
                  <div className="productVolume">
                        {this.props.product.volume} cl</div>
                  <div className="productPrice">
                        {this.props.product.price},- </div>
            </div>
            )
      }                 
}
export default RegularProduct;
