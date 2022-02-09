import React from 'react';
import data from "../data.json"
import EditProduct from "./EditProduct.js"
class EditList extends React.Component {
      constructor(props){
            super(props);
            this.data = data;
      }
      render(){
            return( <ul> {
                  this.data.map(
                        i => (<li key={i.name}> { 
                              i.products.map(
                                    g =>( <EditProduct
                                          key={g.name}
                                          product={g}
                                    />)
                              ) 
                        } </li>)
                  )
            } </ul >);
      }
}
export default EditList;
