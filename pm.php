<?php include "templates/header.php"; ?>

<!DOCTYPE html>
<script type ="text/javascript">
	function cn()
	{
		window.location.href = "cn.php"
	}
</script>
<script type ="text/javascript">
	function me()
	{
		window.location.href = "me.php"
	}
</script>


<div class="tabContainer2">
	<div class="buttonContainer2">
		<button onclick="cn()"> Create New </button>
		<button onclick="me()"> Manage Existing </button>
	</div>


<?php include "templates/footer.php"; ?>