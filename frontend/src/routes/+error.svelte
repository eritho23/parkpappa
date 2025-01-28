<!--
    Basic error page

    Author: Eric Thorburn
-->
<script>
    import {page} from "$app/stores"
</script>

<div class="w-1/4 h-1/4 mx-auto my-auto align-center justify-center flex flex-col border-2 border-primary rounded">
    <span class="text-4xl mx-auto">{$page.status}</span>
    <span class="mx-auto">{$page.error?.message}</span>
</div>

