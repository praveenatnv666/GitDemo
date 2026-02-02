package QAtests;

import org.testng.annotations.Test;

import PageEvents.HomePageEvents;
import PageEvents.LoginPageEvents;
import constants.ElementFetch;
import selenium.automation.mini_project;

public class Testcase1 extends mini_project {
	ElementFetch ele=new ElementFetch();
	HomePageEvents homePage =new HomePageEvents();
	LoginPageEvents loginPage=new LoginPageEvents();
  @Test
  public void samplemethodForEnterningCredentails() {
	  
	  logger.info("Signin into login page");
	  homePage.SignInButton();
	  logger.info("Verify if login is present");
	  loginPage.verifyLoginpage();
	  logger.info("Enter Credentails");
	  loginPage.enterCredentails();
	  
	  
  }
}
