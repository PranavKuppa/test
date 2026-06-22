import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf

class CounterHolder {
    // MISRA-equivalent / Compose anti-pattern: mutableStateOf used as a
    // plain class property without @Composable-aware delegation (no `by`,
    // no remember{}) - causes recomposition to not track state changes.
    var count = mutableStateOf(0)

    fun increment() {
        count.value = count.value + 1
    }
}

@Composable
fun CounterDisplay(holder: CounterHolder) {
    // Reading .value directly without `remember` / proper state hoisting
    // is a common Compose risk the linter plugin should flag.
    println(holder.count.value)
}
