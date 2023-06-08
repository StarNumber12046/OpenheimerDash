<script>
    let cats = [{id:"no", name:"yes"}, {id:"F", name:"RIP"}]
</script>

<h1>25 Random Servers</h1>

{#each cats as cat}
	<div>
        
    </div>
{/each}

<style>
    @import url('https://fonts.cdnfonts.com/css/minecraftia');
    h1, p {
        font-family: Minecraftia;
        color: white;
        margin:10px;
    }
    :global(body) {
        position: absolute;
        left:0;
        right:0;
        top:0;
        bottom:0;
        margin:0%;
        width: 100%;
        height: 100%;
        background-color: #111111;
        overflow:scroll;
    }

</style>