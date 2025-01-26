<script lang="ts">
import "../app.css"
import { Navbar, NavBrand, NavHamburger, NavLi, NavUl, Dropdown, DropdownItem, DropdownDivider, BottomNav, BottomNavItem} from "flowbite-svelte"
import { page } from "$app/stores"
import { Menu, User, House, MapPinned, MessageSquareMore, Settings } from "lucide-svelte"
let activeUrl = $derived($page.url.pathname);
const activeClass = "text-primary bold underline stroke-primary";
const nonActiveClass = "text-text hover:text-primary";

let { data, children } = $props();
let {isLoggedIn, email, avatarUrl} = data;

let showLogout = $state(false); // Reactive variable for hover effect

</script>

<svelte:head>
  <title>
    Parkpappa
  </title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-hidden">
<Navbar class="px-2 sm:px-4 py-2.5 w-full z-30 top-0 start-0 border-b bg-background-foreground hidden md:block">
  <NavBrand href="/">
    <span class="self-center whitespace-nowrap text-xl text-primary dark:text-white font-primary font-normal">Parkpappa</span>
  </NavBrand>
  <NavHamburger />
  <NavUl {activeUrl} {activeClass} {nonActiveClass}>
    <NavLi href="/">Hem</NavLi>
    <NavLi href="/map">Karta</NavLi>
    {#if isLoggedIn}
      <NavLi class="flex flex-row space-x-4 hover:cursor-pointer" title="Logga ut" 
      on:mouseenter={() => (showLogout = true)}
      on:mouseleave={() => (showLogout = false)}
      onclick={() => {
        window.location.href = '/auth';
        
      }}>
      
        {#if avatarUrl}
          <img alt="user avatar" class="rounded-full size-6" onerror={() => {
            console.error('image error');
          }} src={avatarUrl} />
        {:else}
          <User class="md:block hidden size-5" />
        {/if}
        <span>{showLogout ? 'Logga ut' : email}</span>
      </NavLi>
      <NavLi class="flex flex-row space-x-4" href="/settings"><Settings class="size-5"></Settings>Inställningar</NavLi>
    {:else}
      <NavLi href="/auth" title="Logga in">Logga in</NavLi>
    {/if}
  </NavUl>
  
</Navbar>
  <main class="flex-grow flex flex-col">
    {@render children?.()}
  </main>

  <div class="block md:hidden">
    <BottomNav classInner="grid-cols-4 h-36 items-start mt-2" {activeUrl} classActive="font-bold text-primary [&>*]:stroke-primary">
      <BottomNavItem btnName="Hem" href="/">
        <House class="w-6 h-6 mb-1 text-gray-500 dark:text-gray-400 group-hover:text-primary-600 dark:group-hover:text-primary-500" />
      </BottomNavItem>
      <BottomNavItem btnName="Karta" href="/map">
        <MapPinned class="w-6 h-6 mb-1 text-gray-500 dark:text-gray-400 group-hover:text-primary-600 dark:group-hover:text-primary-500" />
      </BottomNavItem>
      <BottomNavItem class="" btnName={isLoggedIn ? 'Logout' : 'Login'} href="/auth">
        {#if isLoggedIn}
          <img alt="user avatar" class="rounded-full size-6 mb-1" onerror={() => {
            console.error('image error');
          }} src={avatarUrl} />
        {:else}
          <User class="w-6 h-6 mb-1 text-gray-500 dark:text-gray-400 group-hover:text-primary-600 dark:group-hover:text-primary-500" />
        {/if}
      </BottomNavItem>
      <BottomNavItem btnName="Inställningar" href="/settings">
        <Settings class="w-6 h-6 mb-1 text-gray-500 dark:text-gray-400 group-hover:text-primary-600 dark:group-hover:text-primary-500" />
      </BottomNavItem>
    </BottomNav>
  </div>
</div>






