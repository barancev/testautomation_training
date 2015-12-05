package lesson2.module4;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TemporaryFolder;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import java.io.File;
import java.io.IOException;

public class xUnitSample {

    @Rule
    public TemporaryFolder tempDir = new TemporaryFolder();

    @Test
    public void canCreateFileWithValidName() throws IOException {
        File f = tempDir.newFile("test.txt");
        Assert.assertTrue(f.exists());
        Assert.assertEquals(f.getName(), "test.txt");
    }

    @Test
    public void cannotCreateFileWithInvalidName() {
        try {
            File f = tempDir.newFile("test/txt");
        } catch (IOException expected) {
            return;
        }
        Assert.fail("Should throw!");
    }

    @Test
    public void deleteFile() throws IOException {
        File f = tempDir.newFile("test.txt");
        Assert.assertTrue(f.exists());

        f.delete();
        Assert.assertFalse(f.exists());
    }

}
