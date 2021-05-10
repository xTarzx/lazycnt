function toClipboard() {
    var url = document.getElementById("shortened_url")
    url.select()
    document.execCommand("copy")
}