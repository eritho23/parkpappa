<script lang="ts">
import "../app.css"
import { Navbar, NavBrand, NavHamburger, NavLi, NavUl} from "flowbite-svelte"
import { page } from "$app/stores"
$: activeUrl = $page.url.pathname;
const activeClass = "text-primary bold underline";
const nonActiveClass = "text-text hover:text-primary";
</script>


<div class="relative px-8">
  <Navbar class="px-2 sm:px-4 py-2.5 fixed w-full z-20 top-0 start-0 border-b bg-background-foreground">
    <NavBrand href="/">
      <span class="self-center whitespace-nowrap text-xl text-primary dark:text-white font-primary font-normal">Parkpappa</span>
    </NavBrand>
    <NavHamburger />
    <NavUl {activeUrl} {activeClass} {nonActiveClass}>
      <NavLi href="/">Hem</NavLi>
      <NavLi href="/map">Karta</NavLi>
      <NavLi href="/reviews">Recensioner</NavLi>
      <NavLi href="/settings">Inställningar</NavLi>
      <NavLi href="/about">Om oss</NavLi>
      <NavLi href="/contact">Kontakta oss</NavLi>
    </NavUl>
  </Navbar>
  <slot></slot>
</div>





