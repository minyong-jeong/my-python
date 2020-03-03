const myInput = document.getElementById("my-input");
myInput.addEventListener("keyup", tableFilter);

function tableFilter() {
    let filter, table, tr, td, i, txtValue;
    filter = document.getElementById("my-input").value.toUpperCase();
    table = document.getElementById("my-table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        td2 = tr[i].getElementsByTagName("td")[1];
        if (td) {
            txtValue = td.textContent || td.innerText;
            txtValue2 = td2.textContent || td2.innerText;
            txt1_ok = txtValue.toUpperCase().indexOf(filter) > -1
            txt2_ok = txtValue2.toUpperCase().indexOf(filter) > -1
            if (txt1_ok || txt2_ok) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }       
    }
}