function updateDateTime() {
    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    let now = new Date();
    let day = days[now.getDay()];
    let date = now.getDate();
    let month = months[now.getMonth()];
    let year = now.getFullYear();

    let hours = now.getHours();
    let minutes = now.getMinutes();
    let ampm = hours >= 12 ? "PM" : "AM";
    hours = hours % 12 || 12; // Convert 24-hour format to 12-hour format
    minutes = minutes.toString().padStart(2, "0"); // Add leading zero for minutes if necessary

    let formattedDateTime = `${day}, ${date} ${month} ${year}, ${hours}:${minutes} ${ampm}`;

    document.getElementById("datetime").innerHTML = formattedDateTime;
}

updateDateTime();
setInterval(updateDateTime, 60000); // Update the time every 60 seconds
