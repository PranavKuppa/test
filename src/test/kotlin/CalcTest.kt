import org.junit.Test
import org.junit.Assert.assertEquals

class CalcTest {
    @Test
    fun testAdd() {
        assertEquals(5, add(2, 3))
    }

    @Test
    fun testSubtract() {
        assertEquals(3, subtract(5, 2))
    }
}
