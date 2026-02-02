package PageEvents;

import PageObject.HomePageElements;
import constants.ElementFetch;

public class HomePageEvents {
	ElementFetch ele=new ElementFetch();
	public void SignInButton()
	{
		ele.getWebElement("XPath",HomePageElements.About).click();
		ele.getWebElement("XPath",HomePageElements.signInButtonText).click();
	
	}

}
