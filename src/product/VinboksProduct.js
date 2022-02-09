import React from 'react';
import Name from './Name.js'
class VinboksProduct extends React.Component{
      render(){
      return (
            <div className="product">
                  <Name product={this.props.product} />
                  <div className="productVolume">glass</div>
                  <div className="productPrice">{this.props.product.price},-</div>
                  </div>
      )}

}
export default VinboksProduct;
