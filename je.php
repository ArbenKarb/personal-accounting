<?php include "templates/header.php"; ?>

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


<?php include "templates/footer.php"; ?>