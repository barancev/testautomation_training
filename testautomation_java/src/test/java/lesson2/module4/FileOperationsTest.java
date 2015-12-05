package lesson2.module4;

import com.google.common.io.Files;
import org.testng.Assert;
import org.testng.annotations.Factory;
import org.testng.annotations.Test;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class FileOperationsTest {

  private File dir;
  private String name;

  public FileOperationsTest(File dir, String name) {
    this.dir = dir;
    this.name = name;
  }

  @Test
  public void createFile() throws IOException {
    System.out.println("create " + name);
    File f = new File(dir, name);
    Assert.assertTrue(f.createNewFile());
    Assert.assertTrue(f.exists());
    Assert.assertEquals(f.getName(), name);
  }

  @Test(dependsOnMethods = "createFile")
  public void deleteFile() throws IOException {
    System.out.println("delete " + name);
    File f = new File(dir, name);
    Assert.assertTrue(f.exists());
    f.delete();
    Assert.assertFalse(f.exists());
  }

  @Factory
  public static Object[] metaScenario() {
    File tempDir = Files.createTempDir();
    List<Object> tests = new ArrayList<>();
    for (String name : new String[] {"test.txt", ".txt", "@#$%&.txt"}) {
      tests.add(new FileOperationsTest(tempDir, name));
    }
    return tests.toArray();
  }
}
