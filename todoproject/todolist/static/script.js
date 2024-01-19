function showConfirmation(id) {
  if (confirm("Вы уверены, что хотите удалить эту запись?")) {
    // Если пользователь нажал OK, перейдем по ссылке
    var lnk = `delete_task/${id}/`;
    document.location.href = lnk;
  }
  else{
    document.location.href = "/";
  }
}