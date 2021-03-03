attrs = ["courseType","courseId","slot","name","link","default_id","password"];
for(item in attrs)
{
  let crs = document.getElementById(attrs[item]);
  if(crs!= null)
  {
    crs.classList.add("form-control");
  }
}