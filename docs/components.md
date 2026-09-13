# Components
One entry per component: what it is, then its props record as declared. The doc
comment is the one in the source, so the two cannot drift.

## Buttons and links

### Button

A tappable action. `variant` is how much ink it uses (solid, outline, ghost, link),
`action` what it means (primary, secondary, positive, negative), `size` sm | md | lg.
`loading` swaps the icon for a spinner and blocks taps; `disabled` dims and blocks.
One element to a screen reader: "<label>, button", dimmed when disabled.

```chuks
Button({ label: "Save", onPress: save })
Button({ label: "Delete", action: "negative", variant: "outline", onPress: remove })
Button({ label: "Sending", loading: sending.get(), onPress: send })
```

```chuks
export dataType ButtonProps {
    label: string,
    onPress: function?(): void,
    variant: string?,               // "solid" (default) | "outline" | "ghost" | "link"
    action: string?,                // "primary" (default) | "secondary" | "positive" | "negative"
    size: string?,                  // "sm" | "md" (default) | "lg"
    icon: Node?,                    // a glyph before the label
    iconRight: Node?,               // a glyph after it
    loading: bool?,
    disabled: bool?,
    full: bool?,                    // stretch to the parent's width
    ref: ViewRef?,                  // to anchor a Popover to this button
    a11yLabel: string?,
    extra: string?,
}
```

### IconButton

A button that is only a glyph. `a11yLabel` is required: the glyph says nothing to a
screen reader. Round by default.

```chuks
IconButton({ icon: lucide("x", 18, tk("text")), a11yLabel: "Close", onPress: close })
```

```chuks
export dataType IconButtonProps {
    icon: Node,
    a11yLabel: string,
    onPress: function?(): void,
    variant: string?,               // "ghost" (default) | "solid" | "outline" | "soft"
    action: string?,
    size: string?,
    disabled: bool?,
    ref: ViewRef?,
    extra: string?,
}
```

### Link

Inline text that goes somewhere. Underlined in the action colour; a screen reader
calls it a link.

```chuks
Link({ text: "Terms of service", onPress: function(): void { openUrl(terms) } })
```

```chuks
export dataType LinkProps {
    text: string,
    onPress: function?(): void,
    action: string?,
    size: string?,
    extra: string?,
}
```

### Fab

A floating action button: the screen's one main action, pinned to a corner of its
parent. Give the parent `grow: 1` so the corner is the screen's.

```chuks
Fab({ icon: lucide("plus", 24, tk("primaryText")), a11yLabel: "New post", onPress: compose })
```

```chuks
export dataType FabProps {
    icon: Node,
    a11yLabel: string,
    onPress: function?(): void,
    label: string?,                 // an extended FAB carries a word
    action: string?,
    position: string?,              // "bottom-right" (default) | "bottom-left"
    inset: int?,                    // distance from the edges (16)
    extra: string?,
}
```

## Surfaces and labels

### Card

A surface that groups content. `variant`: "elevated" (default: a border and a soft
shadow), "outline", "filled" (a tinted fill, no border), "ghost" (padding only).

```chuks
Card({ children: [ Heading({ text: "Today" }), Text({}, "3 walks") ] })
```

```chuks
export dataType CardProps {
    children: []Node,
    variant: string?,
    pad: string?,                   // "sm" | "md" (default) | "lg"
    onPress: function?(): void,     // a tappable card is a button to a screen reader
    extra: string?,
}
```

### Heading

A heading. `size`: "xs" | "sm" | "md" (default) | "lg" | "xl". A screen reader
jumps between headings, so use one for every section title.

```chuks
export dataType HeadingProps {
    text: string,
    size: string?,
    extra: string?,
}
```

### Badge

A small, quiet label above a group of rows. A header to a screen reader.

```chuks
export dataType SectionHeaderProps { text: string, extra: string? }
/** A small, quiet label above a group of rows. A header to a screen reader. */
export function SectionHeader(p: SectionHeaderProps): Node {
    return Text({ tw: "text-xs font-bold text-subtle uppercase tracking-wide p-sm " + (p.extra ?? ""), a11yRole: "header" }, p.text)
}

export dataType DividerProps { vertical: bool?, extra: string? }
/** A hairline. `vertical: true` for a column separator inside a Row. Decoration to a screen reader. */
export function Divider(p: DividerProps): Node {
    if (p.vertical ?? false) { return Row({ tw: "w-1 bg-borderSoft self-stretch " + (p.extra ?? ""), a11yHidden: true }, []) }
    return Row({ tw: "h-1 bg-borderSoft " + (p.extra ?? ""), a11yHidden: true }, [])
}

/**
 * A small status label. `action` colours it; `variant`: "soft" (default: a tint),
 * "solid", "outline".
 *
 * ```chuks
 * Badge({ text: "Live", action: "positive" })
 * Badge({ text: "3", variant: "solid" })
 * ```
 */
export dataType BadgeProps {
    text: string,
    action: string?,
    variant: string?,
    size: string?,
    extra: string?,
}
```

### Chip

A selectable pill (filters, tags). The parent owns `selected`. A button to a screen
reader that says whether it is selected.

```chuks
export dataType ChipProps {
    text: string,
    selected: bool?,
    onPress: function?(): void,
    icon: Node?,
    action: string?,
    extra: string?,
}
```

### Avatar

A round picture or initials. `src` shows the image; without it the `initials` show
on a tinted disc. `size`: "sm" (32) | "md" (40, default) | "lg" (56) | "xl" (80).

```chuks
export dataType AvatarProps {
    initials: string,
    src: string?,
    size: string?,
    a11yLabel: string?,             // the person's name
    extra: string?,
}
```

### Skeleton

The grey shape a card or row shows while its data loads; it pulses on the native
driver. Call it inside a `Comp` (it holds animation state). Hidden from screen
readers: the real content will speak for itself.

```chuks
export dataType SkeletonProps {
    h: int,
    w: int?,                        // omit to fill the available width
    radius: int?,
    extra: string?,
}
```

## Forms

### Input

A text field. `value` is yours; `onChange` gives you the new text on each edit.
`invalid` reddens the border (FormControl sets it from its `error`).

```chuks
Input({ value: email.get(), placeholder: "you@example.com", keyboardType: "email",
        onChange: function(v: string): void { email.set(v) } })
```

```chuks
export dataType InputProps {
    value: string?,
    onChange: function?(v: string): void,
    placeholder: string?,
    secure: bool?,                  // password: mask the text
    multiline: bool?,               // a taller text area
    keyboardType: string?,          // "email" | "number" | "decimal" | "phone" | "url"
    returnKeyType: string?,         // "done" | "send" | "search" | "next" | "go"
    autoCapitalize: string?,        // "none" | "sentences" | "words" | "characters"
    autoCorrect: bool?,
    maxLength: int?,
    editable: bool?,
    invalid: bool?,
    size: string?,
    onSubmit: function?(): void,
    onFocus: function?(): void,
    onBlur: function?(): void,
    a11yLabel: string?,
    extra: string?,
}
```

### FormControl

A label, a field, and the line under it: a helper by default, the error when there
is one. The field is any node; an `Input` inside takes `invalid` from `error` when
you pass it. Required fields carry an asterisk.

```chuks
FormControl({ label: "Email", required: true, error: emailError.get(),
              helper: "We never share it",
              field: Input({ value: email.get(), invalid: emailError.get() != "", onChange: setEmail }) })
```

```chuks
export dataType FormControlProps {
    label: string,
    field: Node,
    helper: string?,
    error: string?,                 // "" or null = no error
    required: bool?,
    extra: string?,
}
```

### Checkbox

A box with a label. The parent owns `checked`; `onChange` reports the flip. A
screen reader hears "<label>, checkbox, checked".

```chuks
Checkbox({ label: "I agree", checked: ok.get(), onChange: function(v: bool): void { ok.set(v) } })
```

```chuks
export dataType CheckboxProps {
    label: string,
    checked: bool,
    onChange: function?(v: bool): void,
    disabled: bool?,
    action: string?,
    size: string?,
    extra: string?,
}
```

### RadioGroup

One choice out of a list, as a column of radios. The parent owns `selected` (an
index; -1 = none); `onSelect` reports a tap. Each radio says "checked" or not.

```chuks
RadioGroup({ options: ["Card", "Cash"], selected: pay.get(),
             onSelect: function(i: int): void { pay.set(i) } })
```

```chuks
export dataType RadioGroupProps {
    options: []string,
    selected: int,
    onSelect: function?(i: int): void,
    disabled: bool?,
    horizontal: bool?,
    action: string?,
    extra: string?,
}
```

### Switch

The native on/off switch, tinted with the theme. Controlled: `on` is yours,
`onToggle` fires on a flip. Give it a `label` and the row is one element that says
"<label>, switch, on".

```chuks
export dataType SwitchProps {
    on: bool,
    onToggle: function?(): void,
    label: string?,
    disabled: bool?,
    extra: string?,
}
```

### Stepper

A number with minus and plus. Clamped to `min`/`max`, so the caller never has to
re-check what it hands back. The glyph buttons are named for a screen reader.

```chuks
export dataType StepperProps {
    value: int,
    onChange: function?(v: int): void,
    min: int?,
    max: int?,
    step: int?,
    extra: string?,
}
```

### SearchBar

A search field with a leading icon slot and a clear button that appears once there
is text. Icon-agnostic: pass the glyph as a node.

```chuks
export dataType SearchBarProps {
    value: string,
    onChange: function?(v: string): void,
    placeholder: string?,
    icon: Node?,
    onClear: function?(): void,
    onSubmit: function?(): void,
    extra: string?,
}
```

### SegmentedControl

One choice out of a few, as a row of segments. Composed rather than the native
control, which themes poorly and differs in metrics across platforms. Each segment
is a tab to a screen reader.

```chuks
export dataType SegmentedControlProps {
    options: []string,
    selected: int,
    onSelect: function?(i: int): void,
    extra: string?,
}
```

### Tabs

Tabs with an underline, and the selected tab's panel under them when `panels` is
given (one node per tab, built lazily by index). The parent owns `selected`.

```chuks
Tabs({ tabs: ["Posts", "Likes"], selected: tab.get(), onSelect: function(i: int): void { tab.set(i) },
       panel: function(i: int): Node { return i == 0 ? Posts() : Likes() } })
```

```chuks
export dataType TabsProps {
    tabs: []string,
    selected: int,
    onSelect: function?(i: int): void,
    panel: function?(i: int): Node,
    action: string?,
    extra: string?,
}
```

## Feedback

### Alert

An inline banner: a message with a meaning. `action` colours it (positive for
success, negative for an error, primary for information, secondary for a note);
`variant`: "soft" (default) or "solid". Announced when it appears.

```chuks
Alert({ title: "Saved", body: "Your changes are live.", action: "positive" })
Alert({ title: "No connection", action: "negative", onClose: dismiss })
```

```chuks
export dataType AlertProps {
    title: string,
    body: string?,
    action: string?,
    variant: string?,
    icon: Node?,
    onClose: function?(): void,
    extra: string?,
}
```

### EmptyState

What a screen shows when it has nothing to show: an icon slot, a headline, a line
of explanation, and an optional action.

```chuks
export dataType EmptyStateProps {
    title: string,
    body: string?,
    icon: Node?,
    action: Node?,
    extra: string?,
}
```

### toast

Show a short message. Safe to call from any closure; messages queue.

```chuks
export dataType ToastItem { message: string; title: string; action: string; actionLabel: string; onAction: any }
var TOASTS: []ToastItem = []
var TOAST_MS: int = 2600

export dataType ToastOptions {
    message: string,
    title: string?,
    action: string?,
    actionLabel: string?,
    onAction: function?(): void,
}
```

### toastWith

A toast with a meaning, a title, or a button: `action` colours the edge (positive,
negative, primary, secondary), `actionLabel` + `onAction` add a tappable word
("Undo").

```chuks
toastWith({ message: "Post deleted", actionLabel: "Undo", onAction: restore, action: "negative" })
```

### setToastDuration

How long each message stays up, in milliseconds (default 2600).

### ToastHost

The surface toasts appear on. Mount once in the app shell; renders nothing when
 there is no message. Each toast is a polite live region.

## Overlays

### Tooltip

A short line anchored to a view, on a dark pill with a pointer. `anchor` is the
useViewRef() handle the anchored view carries as `ref`.

```chuks
const info: ViewRef = useViewRef()
IconButton({ ref: info, icon: lucide("info", 16, tk("muted")), a11yLabel: "About this", onPress: function(): void { tip.set(true) } })
Tooltip({ text: "Sent once a day", anchor: info, visible: tip.get(), onDismiss: function(): void { tip.set(false) } })
```

```chuks
export dataType TooltipProps {
    text: string,
    anchor: ViewRef,
    visible: bool,
    placement: string?,             // "top" (default) | "bottom" | "left" | "right" | "auto"
    onDismiss: function?(): void,
}
```

### AlertDialog

A themed confirm dialog: a title, a line, and two buttons. Unlike the framework's
native `Alert`, it looks like the rest of the app. `action` colours the confirm
button (negative for a destructive choice). Cancel, the scrim and Android back all
fire `onCancel`.

```chuks
AlertDialog({ visible: ask.get(), title: "Delete post?", body: "This cannot be undone.",
              confirmText: "Delete", action: "negative",
              onConfirm: remove, onCancel: function(): void { ask.set(false) } })
```

```chuks
export dataType AlertDialogProps {
    visible: bool,
    title: string,
    body: string?,
    confirmText: string?,           // "OK"
    cancelText: string?,            // "Cancel"; "" hides the button
    action: string?,
    onConfirm: function?(): void,
    onCancel: function?(): void,
}
```

### ActionSheet

A sheet of choices from the bottom. `onSelect` reports the tapped index; the
`destructive` index is red. The scrim, a swipe down, Android back and the cancel
row all fire `onDismiss`.

```chuks
ActionSheet({ visible: menu.get(), title: "Photo", items: ["Save", "Share", "Delete"], destructive: 2,
              onSelect: function(i: int): void { menu.set(false); act(i) },
              onDismiss: function(): void { menu.set(false) } })
```

```chuks
export dataType ActionSheetProps {
    visible: bool,
    items: []string,
    onSelect: function?(i: int): void,
    onDismiss: function?(): void,
    title: string?,
    destructive: int?,              // index of the red item (-1 = none)
    cancelText: string?,            // "Cancel"
}
```

### Drawer

A panel that slides in from a side, over a scrim. `side`: "left" (default) or
"right"; `width` defaults to 300. Tapping the scrim, Android back, fire `onDismiss`.

```chuks
Drawer({ visible: nav.get(), onDismiss: function(): void { nav.set(false) },
         children: [ Heading({ text: "Menu" }), ListItem({ title: "Settings", onPress: openSettings }) ] })
```

```chuks
export dataType DrawerProps {
    visible: bool,
    children: []Node,
    onDismiss: function?(): void,
    side: string?,
    width: int?,
}
```

### ImageViewer

A picture, full screen, on a dark scrim. Tap anywhere to close.

```chuks
export dataType ImageViewerProps {
    visible: bool,
    src: string,
    onDismiss: function?(): void,
    a11yLabel: string?,
}
```

## Data display

### Accordion

A titled row that expands to reveal its children. The open state stays with the
caller, so a set of them can be driven together or independently. The header says
expanded or collapsed.

```chuks
export dataType ListItemProps {
    title: string,
    subtitle: string?,
    trailing: string?,
    trailingNode: Node?,
    leading: Node?,
    onPress: function?(): void,
    extra: string?,
}
export dataType CarouselProps {
    children: []Node,
    page: int,
    onPage: function?(i: int): void,
    h: int,
    itemWidth: int?,                // page width; defaults to the viewport width
    dots: bool?,                    // default true
    extra: string?,
}
const DOTS_H: int = 20
export dataType MonthViewProps {
    year: int,
    month: int,
    selected: string?,
    onSelect: function?(iso: string): void,
    onMonth: function?(y: int, m: int): void,
    sundayFirst: bool?,
    extra: string?,
}
const MONTHS: []string = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
/**
 * A row with a title, an optional subtitle, and a trailing text or node. Tappable when
 * `onPress` is passed, and then one button to a screen reader.
 */
export function ListItem(p: ListItemProps): Node {
    var kids: []Node = []
    if (p.leading != null) { kids.push(p.leading) }
    var textKids: []Node = [ Text({ tw: "text-base font-semibold text-text" }, p.title) ]
    if (p.subtitle != null) { textKids.push(Text({ tw: "text-sm text-muted" }, p.subtitle)) }
    kids.push(Column({ tw: "grow gap-xs", justify: "start", align: "start" }, textKids))
    if (p.trailing != null) { kids.push(Text({ tw: "text-sm text-subtle" }, p.trailing)) }
    if (p.trailingNode != null) { kids.push(p.trailingNode) }
    return Row({ tw: "items-center gap-md p-md bg-surface rounded-lg " + (p.extra ?? ""), onPress: p.onPress,
                 a11yRole: p.onPress != null ? "button" : "" }, kids)
}

export dataType AccordionProps {
    title: string,
    open: bool,
    onToggle: function?(): void,
    children: []Node,
    extra: string?,
}
```

### Table

A grid of text. `columns` are the headers, `rows` the cells; `widths` fixes column
widths in points (omit for equal shares). Long tables scroll sideways when wider
than the screen.

```chuks
Table({ columns: ["Day", "Steps"], rows: [["Mon", "8,412"], ["Tue", "10,003"]] })
```

```chuks
export dataType TableProps {
    columns: []string,
    rows: [][]string,
    widths: ([]int)?,
    striped: bool?,
    extra: string?,
}
```

### Carousel

A paged horizontal strip with page dots. One child per page; each fills the
carousel's width. `page` is yours to hold.

### MonthView

A month. `year`/`month` (1-12) say which; `selected` is an ISO date ("2026-09-13")
or ""; `onSelect` gets the tapped day's ISO date; `onMonth` gets the month the
arrows move to. Weeks start on Monday unless `sundayFirst`.

```chuks
MonthView({ year: 2026, month: 9, selected: day.get(),
           onSelect: function(iso: string): void { day.set(iso) },
           onMonth: function(y: int, m: int): void { ym.set(string(y) + "-" + string(m)) } })
```
