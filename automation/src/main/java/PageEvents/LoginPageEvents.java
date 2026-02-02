package PageEvents;

import org.testng.Assert;

import PageObject.LoginPageElements;
import constants.ElementFetch;

public class LoginPageEvents {


		ElementFetch ele=new ElementFetch();
		public void verifyLoginpage()
		{
			Assert.assertTrue(ele.getWebElements("XPath",LoginPageElements.LogInText).size()>0, "Element not found");
			
		}
		public void enterCredentails()
		{
			ele.getWebElement("XPath", LoginPageElements.emailFeild).sendKeys("xtyz.com");
			ele.getWebElement("XPath", LoginPageElements.passwordFeild).sendKeys("12345");
		}
}
