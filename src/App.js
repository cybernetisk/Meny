import React from 'react';
import data from "./data.json"

import CategoryList from './category/CategoryList.js';
import MenuHeader from './misc/MenuHeader.js';
import Footer from './misc/Footer.js'
// import EditList from './edit/EditList.js'

class App extends React.Component {
      constructor(props) {
            super(props);
            this.cat = data;
      }

      render(){
            document.title = "Meny";
            return (
                  <div className="top">
                        {/* <EditList /> */}
                        <MenuHeader />
                        <CategoryList
                              categories={this.cat} />
                        <Footer />
                  </div>
            );
      }
}
export default App;
