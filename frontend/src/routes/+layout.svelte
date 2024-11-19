<script lang="ts">
import "../app.css"
import { Navbar, NavBrand, NavHamburger, NavLi, NavUl} from "flowbite-svelte"
</script>


<div class="relative px-8">
  <Navbar class="px-2 sm:px-4 py-2.5 fixed w-full z-20 top-0 start-0 border-b bg-background-foreground">
    <NavBrand href="/">
      <span class="self-center whitespace-nowrap text-xl font-semibold text-text dark:text-white">Parkpappa</span>
    </NavBrand>
    <NavHamburger />
    <NavUl>
      <NavLi class="text-text" href="/">Home</NavLi>
      <NavLi class="text-text" href="/about">About</NavLi>
      <NavLi class="text-text" href="/docs/components/navbar">Navbar</NavLi>
      <NavLi class="text-text" href="/pricing">Pricing</NavLi>
      <NavLi class="text-text" href="/contact">Contact</NavLi>
    </NavUl>
  </Navbar>
  <slot></slot>
</div>





