package constants;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

import selenium.automation.mini_project;


public class ElementFetch {
	
	public WebElement getWebElement(String identifierType, String identifierValue)
	{
		switch(identifierType) {
		
		case "XPath":
			return mini_project.driver.findElement(By.xpath(identifierValue));
		case "CSS":
			return mini_project.driver.findElement(By.cssSelector(identifierValue));
		case "id":
			return mini_project.driver.findElement(By.id(identifierValue));
		
		default:
			return null;
		}
		
	}
	public List<WebElement> getWebElements(String identifierType, String identifierValue)
	{
		switch(identifierType) {
		
		case "XPath":
			return mini_project.driver.findElements(By.xpath(identifierValue));
		case "CSS":
			return mini_project.driver.findElements(By.cssSelector(identifierValue));
		case "id":
			return mini_project.driver.findElements(By.id(identifierValue));
		
		default:
			return null;
		}
	}
}
