# @chuks/ui

The component kit for Chuks Mobile: buttons, forms, feedback, overlays and data
display, styled through the app's theme roles, accessible by default, one props record
per component. Pure Chuks, no native code: install it, or replace it with a kit of your
own, and the framework never notices.

```
chuks add @chuks/ui
```

```chuks
import { Node, Column } from "pkg/@chuks/mobile/core/ui.chuks";
import { Button, Card, Heading, Input, FormControl, toast } from "pkg/@chuks/ui";

function Screen(): Node {
    return Column({ tw: "p-lg gap-lg" }, [
        Card({ children: [
            Heading({ text: "Sign in" }),
            FormControl({ label: "Email", required: true, field: Input({ placeholder: "you@example.com", keyboardType: "email" }) }),
            Button({ label: "Continue", onPress: function(): void { toast("Welcome back") } }),
        ] }),
    ])
}
```

Three words describe every component: `action` (primary, secondary, positive,
negative) says what it means, `variant` says how much ink it uses, `size` (sm, md, lg)
how big. Every colour is a theme role, so `setTheme` restyles the whole kit and a custom
theme reskins it.

- [docs/design.md](docs/design.md): the rules every component follows, and why.
- [docs/components.md](docs/components.md): the catalogue, one entry per component.

Verified on an iPhone and a Pixel, every component, including the ones a screen reader
has to get right.
