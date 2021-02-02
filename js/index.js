// Add python name & description here!
const dic = {
    "abs.py"                    : "Get absolute number",
    "archive_example.py"        : "Create/Extract archive file",
    "bubble_sort.py"            : "Bubble sort",
    "calc_file_hash.py"         : "Get MD5 checksum of a file",
    "encrypt_password.py"       : "Password encryption using Fernet",
    "excel_example.py"          : "Read/Write excel",
    "file_read_write_ex.py"     : "Read/Write file",
    "flask_sample.py"           : "Simple flask example code",
    "flask_session.py"          : "flask session example code",
    "flask_upload.py"           : "flask file upload code",
    "get_ip_address.py"         : "Get ip address using host",
    "get_nmap.py"               : "Port scanning using nmap",
    "get_text_hash.py"          : "Convert text to hash",
    "heap_sort.py"              : "Heap sort",
    "insertion_sort.py"         : "Insertion sort",
    "is_same_file.py"           : "Check if two files are same",
    "json_util.py"              : "Covert dict to json",
    "log_tail.py"               : "Log tailing example",
    "logger.py"                 : "python logging example",
    "make_dir.py"               : "Make directory",
    "md5_tree.py"               : "Make MD5 tree of directory",
    "nslookup.py"               : "Get ip from domain name using nslookup",
    "permission_check.py"       : "Check file permission",
    "request.py"                : "Example of http request",
    "rock_scissors_paper.py"    : "Simple rock, scissors, paper game",
    "run_shell_cmd.py"          : "Run shell command",
    "selection_sort.py"         : "Selection sort",
    "ssh_connect.py"            : "SSH connection example code",
    "tail_example.py"           : "Log tailing",
    "threading_example.py"      : "Python thread example code",
    "unique_chars.py"           : "Check if a string contains all unique chars",
    "wget_download.py"          : "file download using wget",
    "windows_process_check.py"  : "Process exists check in windows",
    "zip_example.py"            : "Create/Extract zip file",
}

const myInput = document.getElementById("my-input");
const table = document.getElementById("my-table");

myInput.addEventListener("keyup", tableFilter);
window.onload = () => {
    document.getElementById("my-input").value = "";
    createTable();
}

function tableFilter() {
    let filter, tr, td, i, txtValue;
    filter = document.getElementById("my-input").value.toUpperCase();
    
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

function createTable() {
    for (var key in dic) {
        var row = table.insertRow(-1);
        row.setAttribute("onclick",`location.href='https://github.com/minyong-jeong/hello-python/blob/master/${key}'`);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        cell1.innerHTML = key;
        cell2.innerHTML = dic[key];
    }
}
