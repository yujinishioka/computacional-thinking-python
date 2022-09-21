public class Pilha<E> {

    private Object[] vetor;
    private int topo;

    public Pilha<E> (int capacidade) {
        this.vetor = new Object[capacidade];
        this.topo = -1;
    }

    public boolean isEmpty() {
        if (topo == -1)
            return true;
        else
            return false;
    }

    public boolean isFull() {
        if (topo == vetor.length - 1)
            return true;
        else
            return false;
    }

    public void put(E info) {
        topo++;
        vetor[topo] = info;
    }

    public E pop() {
        return (E)vetor[topo--];
    }

    public E peek() {
        return (E)vetor[topo];
    }
}