package lesson2.module4;

import com.tngtech.java.junit.dataprovider.DataProvider;
import com.tngtech.java.junit.dataprovider.DataProviderRunner;
import com.tngtech.java.junit.dataprovider.UseDataProvider;
import org.junit.Assert;
import org.junit.ClassRule;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TemporaryFolder;
import org.junit.runner.RunWith;

import java.io.File;
import java.io.IOException;

import static org.junit.Assert.assertTrue;

@RunWith(DataProviderRunner.class)
public class ParametrizedSample {

    @Rule
    public TemporaryFolder tempDir = new TemporaryFolder();

    @DataProvider
    public static String[] validFileNames() {
        return new String[]{ "test.txt", ".txt", "@#$%&.txt" };
    }

    @DataProvider
    public static String[] invalidFileNames() {
        return new String[]{ "", "test/txt", "*", "\"" };
    }

    @Test
    @UseDataProvider("validFileNames")
    public void canCreateFileWithValidName(String name) throws IOException {
        File f = tempDir.newFile(name);
        assertTrue(f.exists());
        Assert.assertEquals(f.getName(), name);
    }

    @Test
    @UseDataProvider("invalidFileNames")
    public void cannotCreateFileWithInvalidName(String name) {
        try {
            File f = tempDir.newFile(name);
        } catch (IOException expected) {
            return;
        }
        Assert.fail("Should throw!");
    }

    @Test
    public void deleteFile() throws IOException {
        File f = tempDir.newFile("test.txt");
        assertTrue(f.exists());

        f.delete();
        Assert.assertFalse(f.exists());
    }

}
