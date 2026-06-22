import org.junit.Test
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Assert.assertFalse

class UtilsTest {
    @Test
    fun testSquare() {
        assertEquals(16, square(4))
    }

    @Test
    fun testIsEven() {
        assertTrue(isEven(4))
        assertFalse(isEven(3))
    }
}
