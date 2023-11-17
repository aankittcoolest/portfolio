

## Builder pattern


### Motivation
- Some objects are simple and can be created with a single initializer call.
- Other objects require a lot of ceremony to create.
- Having to create with 10 arguments is not productive.
- Instead, opt for piecewise construction.
- Builder provides an API for constructing an object step by step.

### Definition
- Builder: When piecewise object construction is complicated, provide an API for doing it succinctly.


### Complication
- When we need to create different objects doing different tasks and we want to create all of them via builder pattern.



#### Example

```py
# Easy task
text = 'hello'
parts = ['<p>', text, '</p>']
print(''.join(parts))


# Complicated task
words = ['hello', 'world']
parts = ['<ul>']

for w in words:
    parts.append(f' <li>{w}</li>')
parts.append('</ul>')

print('\n'.join(parts))


class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent+1) * self.indent_size)
            lines.append(f'{i1}<{self.text}>')

        for e in self.elements:
            lines.append(e.__str(indent+1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self) -> str:
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    __root = HtmlElement()

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def clear(self):
        self.__root = HtmlElement(name=self.root_name)

    def __str__(self) -> str:
        return str(self.__root)


# builder = HtmlBuilder('ul')
builder = HtmlElement.create('ul')
builder.add_child('li', 'hello')
builder.add_child('li', 'world')
print('Ordinary Child')
print(builder)

builder.clear()
print('Fluent Child')
builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world')
print(builder)
```
