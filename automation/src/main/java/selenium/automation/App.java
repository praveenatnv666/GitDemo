package selenium.automation;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import io.github.bonigarcia.wdm.WebDriverManager;

/**
 * Hello world!
 *
 */
public class App {
	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub
		// WebDriverManager.chromedriver().proxy("testhost:8080").setup();
		WebDriverManager.chromedriver().setup();
		WebDriver driver = new ChromeDriver();
		driver.manage().window().maximize();
		
		driver.get("https://www.hyrtutorials.com/"); 

		/*****
		 * Scroll action using javascript **************
		 * 
		 * 
		 * driver.get("https://www.hyrtutorials.com/"); Thread.sleep(3000);
		 * 
		 * JavascriptExecutor js= (JavascriptExecutor) driver;
		 * 
		 * js.executeScript("window.scrollTo(0,500)"); Thread.sleep(3000);
		 * js.executeScript("window.scrollBy(0,500)"); Thread.sleep(3000);
		 * js.executeScript("document.getElementById('ty_footer').scrollIntoView();");
		 * 
		 * 
		 ****************/

		/*
		 * Find element using Java Script ******
		 * 
		 * 
		 * driver.get("https://demoqa.com/"); JavascriptExecutor js =
		 * (JavascriptExecutor)driver;
		 * js.executeScript("return document.getElementsByClassName('card-body');");
		 * WebElement element=(WebElement)js.
		 * executeScript("return document.evaluate(\"//div[@class='card-body']\",document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue;"
		 * ); element.click();
		 * 
		 */

		/*
		 * GitHUB**********
		 * 
		 * driver.get("https://github.com"); Thread.sleep(3000); WebElement a=
		 * driver.findElement(By.partialLinkText("Sign")); a.click();
		 * Thread.sleep(3000); WebElement login=
		 * driver.findElement(By.xpath("//*[@id='login_field']")); if
		 * (login.isDisplayed()) { if (login.isEnabled() ) { login.sendKeys("ramnagar");
		 * String username= login.getAttribute("value"); System.out.println(username); }
		 * else System.err.println("not displayed"); }
		 */
	}
}
