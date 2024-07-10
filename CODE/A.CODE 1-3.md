import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

public class OrderSystem {
    private Map<Integer, List<String>> orderList; // Liste des commandes

    public OrderSystem() {
        this.orderList = new HashMap<>();
    }

    public void addNewOrder(Integer customerID, String itemName) {
        List<String> items = orderList.getOrDefault(customerID, new ArrayList<>());
        items.add(itemName);
        orderList.put(customerID, items);
    }

    public void modifyOrder(Integer customerID, Integer itemIndex, String newItemName) {
        List<String> items = orderList.get(customerID);
        if (items != null && itemIndex < items.size()) {
            items.set(itemIndex, newItemName);
        }
    }

    public void removeOrder(Integer customerID, Integer itemIndex) {
        List<String> items = orderList.get(customerID);
        if (items != null && itemIndex < items.size()) {
            items.remove(itemIndex);
        }
    }

    public void printOrders() {
        for (Map.Entry<Integer, List<String>> entry : orderList.entrySet()) {
            System.out.println("Customer ID: " + entry.getKey());
            System.out.println("Items: " + String.join(", ", entry.getValue()));
            System.out.println();
        }
    }
}

//////////////////////////////////////////////////////////////////////////////////////////////:

public class OrderProcessor {
    private Database database;
    private EmailService emailService;
    private InventorySystem inventorySystem;
    private DiscountService discountService;

    public OrderProcessor(Database database, EmailService emailService, InventorySystem inventorySystem, DiscountService discountService) {
        this.database = database;
        this.emailService = emailService;
        this.inventorySystem = inventorySystem;
        this.discountService = discountService;
    }

    public void processOrder(Order order) throws ItemNotAvailableException {
        // Vérifier la disponibilité des articles en stock
        checkInventoryAvailability(order);

        // Enregistrer la commande dans la base de données
        database.saveOrder(order);

        // Envoyer un e-mail de confirmation au client
        sendOrderConfirmationEmail(order);

        // Mettre à jour l'inventaire
        updateInventory(order);

        // Appliquer une remise pour les clients fidèles
        applyDiscountIfLoyalCustomer(order);
    }

    private void checkInventoryAvailability(Order order) throws ItemNotAvailableException {
        for (Item item : order.getItems()) {
            if (!inventorySystem.isItemAvailable(item)) {
                throw new ItemNotAvailableException("Item not available in inventory: " + item.getName());
            }
        }
    }

    private void sendOrderConfirmationEmail(Order order) {
        String message = "Your order has been received and is being processed.";
        emailService.sendEmail(order.getCustomerEmail(), "Order Confirmation", message);
    }

    private void updateInventory(Order order) {
        for (Item item : order.getItems()) {
            inventorySystem.updateInventory(item, item.getQuantity() * -1);
        }
    }

    private void applyDiscountIfLoyalCustomer(Order order) {
        if (order instanceof LoyalCustomerOrder) {
            discountService.applyDiscount((LoyalCustomerOrder) order);
        }
    }
}

// Sert a gérer les exeption de l'inventaire 
public class ItemNotAvailableException extends Exception {
    public ItemNotAvailableException(String message) {
        super(message);
    }
}

// Remise client fideles
public class DiscountService {
    public void applyDiscount(LoyalCustomerOrder order) {
        order.setTotalPrice(order.getTotalPrice() * 0.9);
    }
}

public class LoyalCustomerOrder extends Order {
    @Override
    public void applyDiscount() {
        // Appliquer une remise de 10%
        setTotalPrice(getTotalPrice() * 0.9);
    }
}

