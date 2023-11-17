

### SOLID principles

#### Single Responsibility Principle
- A class should handle the single responsibility.
- It should not be given the responsibility not tied to the specification of the class.
- Otherwise class would be called as a God Object.
- Address "Seperation of concerns"

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

class Journal {
    private final List<String> entries = new ArrayList<>();
    private static int count = 0;

    public void addEntry(String text) {
        entries.add("" + (++count) + ": " + text);
    }

    public void removeEntry(int index) {
        entries.remove(index);
    }

    @Override
    public String toString() {
        return String.join(System.lineSeparator(), entries);
    }

    // voilating Single responsibility
    public void save(String filename) throws FileNotFoundException {
        try (PrintStream out = new PrintStream(filename)) {
            out.println(toString());
        }
    }

    // voilating Single responsibility
    public void load(String filename) {
    }

    // voilating Single responsibility
    public void load(URL url) {
    }
}

// To address save and load features, we create a new class
class Persistence {
    public void saveToFile(Journal journal, String filename, boolean overwrite) throws FileNotFoundException {
        if (overwrite || new File(filename).exists()) {
            try (PrintStream out = new PrintStream(filename)) {
                out.println(journal.toString());
            }
        }
    }

    public void load(String filename) {
    }

    public void load(URL url) {
    }
}

class Demo {
    public static void main(String[] args) throws Exception {
        Journal j = new Journal();
        j.addEntry("I cried today");
        j.addEntry("I ate a bug");
        System.out.println(j);

        Persistence p = new Persistence();
        String filename = "journal.txt";
        p.saveToFile(j, filename, true);
    }
}

```


### OCP + Specification
- Open-closed principle
- Open for extension, closed for modification.
- Let's understand it with Filters example.

```java
import java.util.List;
import java.util.stream.*;

enum Color {
    RED, BLUE, GREEN
}

enum Size {
    SMALL, MEDIUM, LARGE, YUGE
}

class Product {
    public String name;
    public Color color;
    public Size size;

    public Product(String name, Color color, Size size) {
        this.name = name;
        this.color = color;
        this.size = size;
    }
}

class ProductFilter {
    public Stream<Product> filterByColor(List<Product> products, Color color) {
        return products.stream().filter(p -> p.color == color);
    }

    public Stream<Product> filterBySize(List<Product> products, Size size) {
        return products.stream().filter(p -> p.size == size);
    }

    public Stream<Product> filterByColorAndSize(List<Product> products, Color color, Size size) {
        return products.stream().filter(p -> p.color == color && p.size == size);
    }
}

interface Specification<T> {
    boolean isSatisfied(T item);
}

interface Filter<T> {
    Stream<T> filter(List<T> items, Specification<T> spec);
}

class ColorSpecification implements Specification<Product> {
    private Color color;

    public ColorSpecification(Color color) {
        this.color = color;
    }

    @Override
    public boolean isSatisfied(Product item) {
        return item.color == color;
    }
}

class SizeSpecification implements Specification<Product> {
    private Size size;

    public SizeSpecification(Size size) {
        this.size = size;
    }

    @Override
    public boolean isSatisfied(Product item) {
        return item.size == size;
    }
}

class BetterFilter implements Filter<Product> {
    @Override
    public Stream<Product> filter(List<Product> items, Specification<Product> spec) {
        return items.stream().filter(p -> spec.isSatisfied(p));
    }
}

class AndSpecification<T> implements Specification<T> {
    private Specification<T> first, second;

    public AndSpecification(Specification<T> first, Specification<T> second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public boolean isSatisfied(T item) {
        return first.isSatisfied(item) && second.isSatisfied(item);
    }

}

class Demo {
    public static void main(String[] args) {
        Product apple = new Product("Apple", Color.GREEN, Size.SMALL);
        Product tree = new Product("Tree", Color.GREEN, Size.LARGE);
        Product house = new Product("House", Color.BLUE, Size.LARGE);

        List<Product> products = List.of(apple, tree, house);

        ProductFilter pf = new ProductFilter();
        System.out.println("Green products (old):");
        pf.filterByColor(products, Color.GREEN)
                .forEach(p -> System.out.println(" - " + p.name + " is green"));

        BetterFilter bf = new BetterFilter();
        System.out.println("Green products (new):");
        bf.filter(products, new ColorSpecification(Color.GREEN)).forEach(
                p -> System.out.println(" - " + p.name + " is green"));

        System.out.println("Large blue items:");
        bf.filter(products,
                new AndSpecification<>(new ColorSpecification(Color.BLUE), new SizeSpecification(Size.LARGE)))
                .forEach(p -> System.out.println(
                        " - " + p.name + " is large and blue"));

    }
}
```

### Liskov Substitution principle
- Objects of a superclass should be able to be replaced with objects of a subclass without affecting the correctness of the program.

```java
class Rectangle {
    int width;
    int height;

    public Rectangle() {
    }

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public int getArea() {
        return width * height;
    }

    @Override
    public String toString() {
        return "Rectangle [width=" + width + ", height=" + height + "]";
    }
}

class Square extends Rectangle {
    public Square() {

    }

    public Square(int size) {
        width = height = size;
    }

    // voilation of Liskov principle
    @Override
    public void setWidth(int width) {
        super.setWidth(width);
        super.setHeight(width);
    }

    // voilation of Liskov principle
    @Override
    public void setHeight(int height) {
        super.setWidth(height);
        super.setHeight(height);
    }
}

// Fixing Liskov principle
class RectangleFactory {
    public static Rectangle newRectangle(int width, int height) {
        return new Rectangle(width, height);
    }

    public static Rectangle newSquare(int side) {
        return new Rectangle(side, side);
    }
}

class Demo {
    static void useIt(Rectangle r) {
        int width = r.getWidth();
        r.setHeight(10);
        // area = width * 10
        System.out.println(
                "Expected area of " + (width * 10) + " , got " + r.getArea());
    }

    public static void main(String[] args) {
        Rectangle rc = new Rectangle(2, 3);
        useIt(rc);

        Rectangle sq = new Square(0);
        sq.setWidth(5);
        useIt(sq);
    }
}
```

### Interface Segregation Principle
- No code should be forced to depend on methods it does not use.
- YAGNI = You Ain't Going to Need it.

```java
class Document {

}

interface Machine {
    void print(Document d);

    void fax(Document d);

    void scan(Document d);
}

interface Printer {
    void print(Document d);
}

interface Scanner {
    void scan(Document d);
}

class MultiFunctionPrinter implements Machine {

    @Override
    public void fax(final Document d) {
        //
    }

    @Override
    public void print(final Document d) {
        //
    }

    @Override
    public void scan(final Document d) {
        //
    }

}

class OldFashionedPrinter implements Machine {

    @Override
    public void print(Document d) {
        //

    }

    @Override
    public void fax(Document d) {
        // ISSUE: Forcing implementation of fax
    }

    @Override
    public void scan(Document d) {
        // ISSUE: Forcing implementation of scan
    }

}

class JustAPrinter implements Printer {

    @Override
    public void print(Document d) {
        //
    }

}

class Photocopier implements Printer, Scanner {

    @Override
    public void print(Document d) {
        //
    }

    @Override
    public void scan(Document d) {
        //
    }

}

interface MultiFunctionDevice extends Printer, Scanner {
}

class MultiFunctionMachine implements MultiFunctionDevice {

    private Printer printer;
    private Scanner scanner;

    public MultiFunctionMachine(Printer printer, Scanner scanner) {
        this.printer = printer;
        this.scanner = scanner;
    }

    @Override
    public void print(Document d) {
        printer.print(d);

    }

    @Override
    public void scan(Document d) {
        scanner.scan(d);
    }

}
```

### Dependency Inversion Principle
- A. High-level modules should not depend on low-level modules. Both should depend on abstractions.
- B. Abstraction should not depend on details. Details should depend on abstractions.

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

import org.javatuples.Triplet;

enum Relationship {
    PARENT, CHILD, SIBLING
}

class Person {
    public String name;

    public Person(String name) {
        this.name = name;
    }
}

interface RelationshipBrowser {
    List<Person> findAllChildrenOf(String name);
}

class Relationships implements RelationshipBrowser { // low-level

    private List<Triplet<Person, Relationship, Person>> relations = new ArrayList<>();

    public List<Triplet<Person, Relationship, Person>> getRelations() {
        return relations;
    }

    public void addParentAndChild(Person person, Person child) {
        relations.add(new Triplet<Person, Relationship, Person>(person, Relationship.PARENT, child));
        relations.add(new Triplet<Person, Relationship, Person>(child, Relationship.CHILD, person));
    }

    @Override
    public List<Person> findAllChildrenOf(String name) {
        return relations.stream()
                .filter(x -> Objects.equals(x.getValue0().name, name)
                        && x.getValue1() == Relationship.PARENT)
                .map(Triplet::getValue2)
                .collect(Collectors.toList());
    }

}

class Research { // high level

    // Violation of Dependency inversion principle as high level module is getting
    // dependend on low level module
    // public Research(Relationships relationships) {
    //     List<Triplet<Person, Relationship, Person>> relations = relationships.getRelations();
    //     relations.stream()
    //             .filter(x -> x.getValue0().name.equals("John")
    //                     && x.getValue1() == Relationship.PARENT)
    //             .forEach(ch -> System.out.println("John has a child called " + ch.getValue2().name));
    // }

    public Research(RelationshipBrowser browser) {
        List<Person> children = browser.findAllChildrenOf("John");
        for (Person child : children) {
            System.out.println("John has a child called  " + child.name);
        }
    }
}

class Demo {
    public static void main(String[] args) {
        Person person1 = new Person("John");
        Person child1 = new Person("Mary");
        Person child2 = new Person("Sohan");

        Relationships relationship = new Relationships();
        relationship.addParentAndChild(person1, child1);
        relationship.addParentAndChild(person1, child2);

        new Research(relationship);
    }
}
```