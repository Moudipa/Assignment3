import React, { Component } from "react";
import Login from "../../components/Login/Login";
import NavigationLayout from "../../components/Nav/NavigationLayout";
import style from "./Landing.module.css";
import WelcomeImg from "../../assets/images/WelcomeImg.jpg";
import Register from "../../components/Register/Register";

export class LandingPage extends Component {
  state = {
    showLogin: true,
  };

  showRegister = () => {
    this.setState({
      showLogin: false,
    });
  };

  showLogin = () => {
    this.setState({
      showLogin: true,
    });
  };
  render() {
    return (
      <NavigationLayout>
        <div className={style.container}>
          <div className={style.innerContainer}>
            <div className={style.loginContainer}>
              {this.state.showLogin ? (
                <Login showRegister={this.showRegister} />
              ) : (
                <Register showLogin={this.showLogin} />
              )}
            </div>
            <div className={style.welcomeContainer}>
              <div className={style.welcomeInnerContainer}>
                <div>
                </div>
                <p className={style.welcomeText1}>Vaayu</p>
                <p className={style.welcomeText2}>
                  E-health solution
                </p>
                <p className={style.welcomeText3}>
                  To stay connected with us, please log in with your email
                  address
                </p>
              </div>
            </div>
          </div>
        </div>
      </NavigationLayout>
    );
  }
}

export default LandingPage;
