package lesson2.module2;

import org.junit.Test;
import org.testng.Assert;

public class Sample4 {

    @Test
    public void testSuccess() {
        Assert.assertTrue(2*2 == 4);
    }

    @Test
    public void testFailure() {
        Assert.assertTrue(2*2 == 5);
    }

    @Test
    public void testAssertSuccess() {
        assert 2*2 == 4;
    }

    @Test
    public void testAssertFailure() {
        assert 2*2 == 5;
    }

}
