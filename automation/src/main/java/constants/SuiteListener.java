package constants;

import java.io.File;
import java.io.IOException;
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.testng.IAnnotationTransformer;
import org.testng.ITestListener;
import org.testng.ITestResult;
import org.testng.annotations.ITestAnnotation;

import selenium.automation.mini_project;

public class SuiteListener implements ITestListener, IAnnotationTransformer {
	
	public void onTestFailure(ITestResult result) {
		
		try {
			WebDriver driver = mini_project.driver;

            if (driver == null) {
                System.out.println("Driver is NULL. Screenshot not captured.");
                return;
            }
	        String filename = System.getProperty("user.dir")
	                + File.separator + "screenshots"
	                + File.separator + result.getMethod().getMethodName()
	                + ".png";

	            File src = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
	            File dest = new File(filename);
	            dest.getParentFile().mkdirs();
	            FileUtils.copyFile(src, dest);
	        }

	     catch (Exception e) {
	        e.printStackTrace();
	    }
		
		/**************
	
		String filename=System.getProperty("user.dir")+File.separator+"screenshots"+File.separator+result.getMethod().getMethodName();
		File f1=((TakesScreenshot)mini_project.driver).getScreenshotAs(OutputType.FILE);
		try {
		FileUtils.copyFile(f1, new File(filename+ ".png"));
		}
		catch(IOException e){
			e.printStackTrace();
		}
		
		***********/
	}
	
	
	public void transformer(
		ITestAnnotation annotation, Class testClass, Constructor testConstructor, Method testMethod){
			annotation.setRetryAnalyzer(RetryAnalyzer.class);
		}

}
