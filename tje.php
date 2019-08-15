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
	<div class="tabPanel2">Tab 1: User Management</div>
	<div class="tabPanel2">Tab 2: User Management</div>


<p>

List of Journal Templates will appear here!

</p>

<?php include "templates/footer.php"; ?>