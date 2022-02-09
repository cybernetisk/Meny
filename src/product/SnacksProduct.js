import React from 'react';
import Name from './Name.js'

class SnackProduct extends React.Component{
      render(){
      return (
            <div className="product">
                  <Name product={this.props.product} />
                  <div className="productVolume">
                        {this.props.product.volume} g</div>
                  <div className="productPrice">
                        {this.props.product.price},- </div>
            </div>
            )
      }                 
}
export default SnackProduct;
