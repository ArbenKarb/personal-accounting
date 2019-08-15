<?php include "templates/header.php"; ?>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>  
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>  

<!DOCTYPE html>
<script type ="text/javascript">
	function mje()
	{
		window.location.href = "mje.php"
	}
</script>
<script type ="text/javascript">
	function tje()
	{
		window.location.href = "tje.php"
	}
</script>


<div class="tabContainer2">
	<div class="buttonContainer2">
		<button onclick="mje()"> Manual journal entry </button>
		<button onclick="tje()"> Templates </button>
	</div>
	

<p>
	<form name="add_name" id="add_name">    
		<table class="table table-bordered" id="dynamic_field">  
			<tr>  
				<td><input type="text" name="name[]" placeholder="Enter your Name" class="form-control name_list" /></td>  
				<td><button type="button" name="add" id="add" class="btn btn-success">Add More</button></td>  
			</tr>  
		</table>  
		<input type="button" name="submit" id="submit" class="btn btn-info" value="Submit" />    
	</form>  
</p>


 
 <script>  
 $(document).ready(function(){  
      var i=1;  
      $('#add').click(function(){  
           i++;  
           $('#dynamic_field').append('<tr id="row'+i+'"><td><input type="text" name="name[]" placeholder="Enter your Name" class="form-control name_list" /></td><td><button type="button" name="remove" id="'+i+'" class="btn btn-danger btn_remove">X</button></td></tr>');  
      });  
      $(document).on('click', '.btn_remove', function(){  
           var button_id = $(this).attr("id");   
           $('#row'+button_id+'').remove();  
      });  
      $('#submit').click(function(){            
           $.ajax({  
                url:"name.php",  
                method:"POST",  
                data:$('#add_name').serialize(),  
                success:function(data)  
                {  
                     alert(data);  
                     $('#add_name')[0].reset();  
                }  
           });  
      });  
 });  
 </script>


</div>

</p>

<?php include "templates/footer.php"; ?>