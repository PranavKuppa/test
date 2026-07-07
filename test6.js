function fetchData() {
return new Promise((resolve) => {
setTimeout(() => {
    resolve("Data received");
        }, 1000);
  });
}
fetchData().then((data) => {
console.log(data);
  }).catch((err) => {
        console.error(err);
});
