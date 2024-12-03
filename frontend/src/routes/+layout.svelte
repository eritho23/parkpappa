<script lang="ts">
import "../app.css"
import { Navbar, NavBrand, NavHamburger, NavLi, NavUl, Dropdown, DropdownItem, DropdownDivider} from "flowbite-svelte"
import { page } from "$app/stores"
import { Menu } from "lucide-svelte"
$: activeUrl = $page.url.pathname;
const activeClass = "text-primary bold underline";
const nonActiveClass = "text-text hover:text-primary";
</script>



<div class="min-h-screen flex flex-col overflow-hidden">
<Navbar class="px-2 sm:px-4 py-2.5 w-full z-30 top-0 start-0 border-b bg-background-foreground">
  <NavBrand href="/">
    <span class="self-center whitespace-nowrap text-xl text-primary dark:text-white font-primary font-normal">Parkpappa</span>
  </NavBrand>
  <NavHamburger />
  <NavUl {activeUrl} {activeClass} {nonActiveClass}>
    <NavLi href="/">Hem</NavLi>
    <NavLi href="/map">Karta</NavLi>
    <NavLi href="/reviews">Recensioner</NavLi>
    <NavLi class="cursor-pointer hidden md:block">
      More
      <Menu size=24 class="hidden md:inline"></Menu>
    </NavLi>
    <Dropdown class="w-40 z-20" containerClass="absolute">
      <DropdownItem href="/settings">Inställningar</DropdownItem>
      <DropdownItem href="/contact">Om oss</DropdownItem>
      <DropdownItem href="/about">Kontakta oss</DropdownItem>
      <DropdownDivider />
      <DropdownItem href="/">Sign out</DropdownItem>
    </Dropdown>
  </NavUl>
  
</Navbar>
  <main class="flex-grow flex flex-col">
    <slot></slot>
  </main>
</div>






