public class DataProcessor {
    private List<Integer> data;
    
    public DataProcessor() {
        this.data = new ArrayList<>();
    }
    
    public void add(int item) {
        data.add(item);
    }
    
    public List<Integer> process() {
        return data.stream()
            .map(x -> x * 2)
            .collect(Collectors.toList());
    }
}
