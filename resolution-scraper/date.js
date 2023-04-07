// Get the current date
const currentDate = new Date();

// Get the date one month ago
const oneMonthAgo = new Date(currentDate);
oneMonthAgo.setMonth(currentDate.getMonth() - 1);

// Format the dates as strings (YYYY-MM-DD)
const formatDate = (date) => {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
};

$(document).ready(function () {
    appPage.init();
});

// ...

var appPage = {
    // ...
    parameters: {
        wardId: [],
        ancId: [],
        selectedFromDate: formatDate(oneMonthAgo),
        selectedToDate: formatDate(currentDate),
        filtered: false
    },
    // ...
};

// ...
