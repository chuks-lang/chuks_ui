# The design of @chuks/ui

A kit is a set of promises an app can rely on without reading the source. These are
the promises every component in this package keeps, and the reason each exists.

## One props record per component

Every component is a function taking one `dataType`. Required content is a plain
field; every option is a nullable one, so a caller writes only what it needs, by name,
and a typo is a compile error rather than a prop that silently does nothing.

```chuks
Button({ label: "Save", onPress: save })
Button({ label: "Delete", action: "negative", variant: "outline", size: "sm", onPress: remove })
```

Children are a field too (`Card({ children: [...] })`), not a second argument: a
single record is the whole contract, and it stays one when a component grows.

Every component also takes `extra`, a `tw` string appended last, so a one-off
adjustment never needs a fork of the component.

## Three words: action, variant, size

- `action` is what the component **means**: `primary` (the main thing), `secondary`
  (a quiet alternative), `positive` (success, confirmation), `negative` (danger,
  destruction). It picks the colour role.
- `variant` is how much **ink** it uses. A Button is `solid`, `outline`, `ghost` or
  `link`; a Badge is `soft`, `solid` or `outline`; a Card is `elevated`, `outline`,
  `filled` or `ghost`. Not every component has every variant; each declares its own.
- `size` is `sm`, `md` (default) or `lg`. A control is 36, 44 or 52 points tall, and
  its text and glyph scale with it.

The three resolve to classes in one place, `src/tokens.chuks`: `ink(action, variant)`
answers the container and text classes, `sizePad`/`sizeText`/`sizeHeight`/`sizeIcon`
the metrics. A component of your own that should colour like a Button calls the same
functions, which is how a custom component stays in the kit's language.

## Every colour is a theme role

Nothing in this package names a colour. `bg-primary`, `text-danger`, `border-border`,
`tk("surface")`: roles, resolved against the active theme at render time. That is the
whole reason `setTheme("dark")` reskins an app, and the reason a custom theme
(`registerTheme`) reskins the kit without touching it.

## Controlled, always

Every stateful component is owned by its parent: `Checkbox` takes `checked` and reports
`onChange(bool)`; `Tabs` takes `selected` and reports `onSelect(i)`; `AlertDialog`
takes `visible` and reports `onConfirm`/`onCancel`. The component never keeps the value
it reports. That is what lets a list recycle a row without carrying the previous row's
state, and what makes "what is on screen" a pure function of the app's state.

## Accessible by default

A screen reader gets the right answer without the app asking for it: a `Button` is a
button, a `Checkbox` says checked, a `Chip` says selected, a `Tabs` head is a tab, a
`Heading` is a heading, a `Stepper`'s glyph buttons are named "Decrease" and
"Increase", an `Alert` announces itself, a `Skeleton` and a `Divider` are hidden. The
components that cannot know the right words require them: `IconButton` and `Fab` make
`a11yLabel` a required field, because a glyph says nothing.

Every component takes the framework's six accessibility props through `LayoutProps`
where it passes layout through, so an app can always say more.

## Overlays

`AlertDialog`, `ActionSheet`, `Drawer`, `ImageViewer` and `Tooltip` are built on the
framework's `Modal` and `Popover`, which own the layer above the app: the scrim, the
safe area, Android's back button, and the rule that a tap on the content is the
content's while a tap on the scrim dismisses. A kit component never fakes an overlay
with an absolutely positioned view; it would sit under the tab bar and ignore back.

## Permissions

A toast goes away on its own, and the package imports `std/time` for that timer. A
package's imports are what an app consents to when it adds the package (`chuks add`
shows them, and records the consent in `chuks.lock`), so a kit keeps its imports to
what it needs and this one needs only the clock. There is no native code, no file
system, no network.

## What this kit is not

It does not wrap native controls that the framework already exposes (`Slider`,
`Select`, `DatePicker`, native `Alert`); use those directly. It does not render images
or video; it composes the framework's `Image`. And it is not the only kit an app can
have: the framework never imports it, so a community kit with the same three words
drops in beside it or instead of it.
