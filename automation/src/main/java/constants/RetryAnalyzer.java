package constants;

import org.testng.IRetryAnalyzer;
import org.testng.ITestResult;

public class RetryAnalyzer implements IRetryAnalyzer{
 int count=0;
 int retryCount=1;
 
	@Override
	public boolean retry(ITestResult result) {
		
		while (count<retryCount)
		{
			count++;
			return true;
		}
		
		// TODO Auto-generated method stub
		return false;
	}

}
