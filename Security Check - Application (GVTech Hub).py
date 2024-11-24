import os
import zipfile
from tkinter import *
from tkinter import filedialog, messagebox

# Base folder structure
base_folder = "Security Check Management"
categories_folder = os.path.join(base_folder, "Categories")

# Preloaded reset links
reset_links = {
    "Email Services": {
        "Gmail": {"url": "https://accounts.google.com/signin/recovery", "folder": "Gmail_Reset"},
        "Outlook": {"url": "https://account.live.com/password/reset", "folder": "Outlook_Reset"},
        "Yahoo": {"url": "https://login.yahoo.com/forgot", "folder": "Yahoo_Reset"},
        "ProtonMail": {"url": "https://mail.proton.me/reset-password", "folder": "ProtonMail_Reset"},
        "Zoho": {"url": "https://accounts.zoho.com/password/reset", "folder": "Zoho_Reset"},
        "iCloud": {"url": "https://iforgot.apple.com/password/verify/appleid", "folder": "iCloud_Reset"},
        "AOL": {"url": "https://login.aol.com/forgot", "folder": "AOL_Reset"},
        "FastMail": {"url": "https://www.fastmail.com/go/password/reset", "folder": "FastMail_Reset"},
        "Tutanota": {"url": "https://mail.tutanota.com/reset/password", "folder": "Tutanota_Reset"}
    },

    "Cloud Storage": {
        "Google_Drive": {"url": "https://accounts.google.com/signin/recovery", "folder": "Google_Drive_Reset"},
        "Dropbox": {"url": "https://www.dropbox.com/forgot", "folder": "Dropbox_Reset"},
        "OneDrive": {"url": "https://account.live.com/password/reset", "folder": "OneDrive_Reset"},
        "iCloud_Drive": {"url": "https://iforgot.apple.com/password/verify/appleid", "folder": "iCloud_Drive_Reset"},
        "Box": {"url": "https://account.box.com/password/reset", "folder": "Box_Reset"},
        "Mega": {"url": "https://mega.nz/recovery", "folder": "Mega_Reset"},
        "pCloud": {"url": "https://www.pcloud.com/forgot-password", "folder": "pCloud_Reset"}
    },

    "Social Networks": {
        "Facebook": {"url": "https://www.facebook.com/recover/initiate", "folder": "Facebook_Reset"},
        "Twitter": {"url": "https://twitter.com/account/begin_password_reset", "folder": "Twitter_Reset"},
        "Instagram": {"url": "https://www.instagram.com/accounts/password/reset/", "folder": "Instagram_Reset"},
        "LinkedIn": {"url": "https://www.linkedin.com/uas/request-password-reset", "folder": "LinkedIn_Reset"},
        "Pinterest": {"url": "https://www.pinterest.com/password/reset/", "folder": "Pinterest_Reset"},
        "Reddit": {"url": "https://www.reddit.com/password", "folder": "Reddit_Reset"}
    },

    "Messaging Apps": {
        "WhatsApp": {"url": "https://www.whatsapp.com/forgot/", "folder": "WhatsApp_Reset"},
        "Telegram": {"url": "https://telegram.org/auth/reset", "folder": "Telegram_Reset"},
        "Discord": {"url": "https://discord.com/password-reset", "folder": "Discord_Reset"},
        "Viber": {"url": "https://account.viber.com/en/reset-password", "folder": "Viber_Reset"},
        "WeChat": {"url": "https://help.wechat.com/recover-account", "folder": "WeChat_Reset"}
    },

    "Video Platforms": {
        "YouTube": {"url": "https://accounts.google.com/signin/recovery", "folder": "YouTube_Reset"},
        "TikTok": {"url": "https://www.tiktok.com/forgot-password", "folder": "TikTok_Reset"},
        "Twitch": {"url": "https://www.twitch.tv/password/reset", "folder": "Twitch_Reset"},
        "Vimeo": {"url": "https://vimeo.com/forgot_password", "folder": "Vimeo_Reset"}
    },

    "General Shopping": {
        "Amazon": {"url": "https://www.amazon.com/ap/forgotpassword", "folder": "Amazon_Reset"},
        "eBay": {"url": "https://signin.ebay.com/ws/eBayISAPI.dll?ForgotPassword", "folder": "eBay_Reset"},
        "Walmart": {"url": "https://www.walmart.com/account/forgotpassword", "folder": "Walmart_Reset"},
        "Target": {"url": "https://www.target.com/account/password-reset", "folder": "Target_Reset"},
        "Costco": {"url": "https://www.costco.com/ForgotPasswordView", "folder": "Costco_Reset"}
    },

    "Fashion & Apparel": {
        "H&M": {"url": "https://www2.hm.com/en_us/password/reset", "folder": "HM_Reset"},
        "Zara": {"url": "https://www.zara.com/us/en/reset-password", "folder": "Zara_Reset"},
        "ASOS": {"url": "https://www.asos.com/identity/password/reset", "folder": "ASOS_Reset"},
        "Nike": {"url": "https://www.nike.com/reset-password", "folder": "Nike_Reset"},
        "Adidas": {"url": "https://www.adidas.com/us/passwordreset", "folder": "Adidas_Reset"}
    },

    "Electronics & Tech": {
        "Best_Buy": {"url": "https://www.bestbuy.com/identity/global/password/forgot", "folder": "Best_Buy_Reset"},
        "Newegg": {"url": "https://secure.newegg.com/identity/forgotpassword", "folder": "Newegg_Reset"},
        "BH_Photo": {"url": "https://www.bhphotovideo.com/find/forgotPassword.jsp", "folder": "BH_Photo_Reset"},
        "Micro_Center": {"url": "https://www.microcenter.com/account/forgot-password", "folder": "Micro_Center_Reset"},
        "Apple": {"url": "https://iforgot.apple.com/password/verify/appleid", "folder": "Apple_Reset"}
    },

    "Home & Garden": {
        "Home_Depot": {"url": "https://www.homedepot.com/auth/view/forgot-password", "folder": "Home_Depot_Reset"},
        "Lowes": {"url": "https://www.lowes.com/forgot-password", "folder": "Lowes_Reset"},
        "Wayfair": {"url": "https://www.wayfair.com/v/account/reset_password/new", "folder": "Wayfair_Reset"},
        "IKEA": {"url": "https://www.ikea.com/us/en/profile/forgot-password", "folder": "IKEA_Reset"}
    },

    "Luxury Retail": {
        "Nordstrom": {"url": "https://www.nordstrom.com/signin/forgot-password", "folder": "Nordstrom_Reset"},
        "Saks_Fifth_Avenue": {"url": "https://www.saksfifthavenue.com/account/forgotpassword", "folder": "Saks_Fifth_Avenue_Reset"},
        "Net_a_Porter": {"url": "https://www.net-a-porter.com/en-us/account/forgot-password", "folder": "Net_a_Porter_Reset"},
        "Bloomingdales": {"url": "https://www.bloomingdales.com/account/forgotpassword", "folder": "Bloomingdales_Reset"}
    }
}

def create_folders():
    """Create the initial folder structure and files"""
    os.makedirs(categories_folder, exist_ok=True)

    for category, sites in reset_links.items():
        category_path = os.path.join(categories_folder, category)
        os.makedirs(category_path, exist_ok=True)
        
        sites_path = os.path.join(category_path, "Sites")
        os.makedirs(sites_path, exist_ok=True)
        
        for site, details in sites.items():
            site_folder = os.path.join(sites_path, details['folder'])
            os.makedirs(site_folder, exist_ok=True)
            
            url_file = os.path.join(site_folder, f"{site}_Reset.url")
            with open(url_file, "w") as file:
                file.write(f"[InternetShortcut]\nURL={details['url']}")

class SecurityCheckManager:
    def __init__(self):
        self.root = Tk()
        self.root.title("Security Check Manager")
        self.root.geometry("1100x750")
        self.root.configure(bg="#1e1e2f")
        
        self.setup_variables()
        self.create_gui()
        
    def setup_variables(self):
        self.selected_category_name = StringVar()
        self.selected_site_name = StringVar()
        self.selected_reset_url = StringVar()
        self.selected_date = StringVar()
        self.selected_username = StringVar()
        self.selected_password = StringVar()
        
    def create_gui(self):
        # Header
        header = Frame(self.root, bg="#292942", height=80)
        header.pack(fill="x")
        Label(header, text="Security Check Manager", bg="#292942", fg="white", 
              font=("Arial", 28, "bold")).pack(pady=20)

        # Main container
        main_container = Frame(self.root, bg="#1e1e2f")
        main_container.pack(expand=True, fill="both", padx=20, pady=20)

        # Left panel for lists
        left_panel = Frame(main_container, bg="#1e1e2f")
        left_panel.pack(side="left", fill="both", expand=True)

        # Categories section
        Label(left_panel, text="Categories", bg="#1e1e2f", fg="white", 
              font=("Arial", 14)).pack(pady=5)
        
        self.category_list = Listbox(left_panel, bg="#292942", fg="white", 
                                   height=15, width=30, selectmode=SINGLE,
                                   selectbackground='#4a4a6a',
                                   selectforeground='white')
        self.category_list.pack(pady=5, padx=10)

        # Sites section
        Label(left_panel, text="Sites", bg="#1e1e2f", fg="white", 
              font=("Arial", 14)).pack(pady=5)
        
        self.sites_list = Listbox(left_panel, 
            bg="#292942", 
            fg="white", 
            height=15, 
            width=30, 
            selectmode=SINGLE,
            selectbackground='#4a4a6a',
            selectforeground='white',
            activestyle='none',  # Removes dotted line around selected item
            font=('Arial', 10)
        )
        self.sites_list.pack(pady=5, padx=10)

        # Right panel for details
        right_panel = Frame(main_container, bg="#292942")
        right_panel.pack(side="right", fill="both", expand=True, padx=10)

        # Details section
        Label(right_panel, text="Selected Site Details", bg="#292942", fg="white",
              font=("Arial", 14, "bold")).pack(pady=10)

        details_frame = Frame(right_panel, bg="#292942")
        details_frame.pack(fill="x", padx=10, pady=5)

        # Create details fields
        labels = [
            ("Category:", self.selected_category_name, False),
            ("Site Name:", self.selected_site_name, False),
            ("Reset Pass URL:", self.selected_reset_url, False),
            ("Date:", self.selected_date, True),
            ("Username:", self.selected_username, True),
            ("Password:", self.selected_password, True)
        ]

        for i, (label_text, variable, is_editable) in enumerate(labels):
            Label(details_frame, text=label_text, bg="#292942", fg="white", 
                  width=12, anchor="w").grid(row=i, column=0, pady=5, padx=5)
            
            if is_editable:
                Entry(details_frame, textvariable=variable, bg="#292942", fg="white",
                      width=40).grid(row=i, column=1, pady=5, padx=5, sticky="w")
            else:
                Label(details_frame, textvariable=variable, bg="#292942", fg="white",
                      width=40, anchor="w").grid(row=i, column=1, pady=5, padx=5)

        # Save button
        Button(right_panel, text="Save Credentials", command=self.save_credentials,
               bg="#292942", fg="white").pack(pady=10)

        # Bind events
        self.category_list.bind('<<ListboxSelect>>', self.on_category_select)
        self.sites_list.bind('<<ListboxSelect>>', self.on_site_select)

        # Initial population
        self.populate_categories()

    def populate_categories(self):
        self.category_list.delete(0, END)
        categories = [
            "Email Services",
            "Cloud Storage",
            "Social Networks",
            "Messaging Apps",
            "Video Platforms",
            "General Shopping",
            "Fashion & Apparel",
            "Electronics & Tech",
            "Home & Garden",
            "Luxury Retail"
        ]
        for category in categories:
            self.category_list.insert(END, category)

    def on_category_select(self, event):
        """Handle category selection"""
        self.sites_list.delete(0, END)
        
        if not self.category_list.curselection():
            return
        
        try:
            selected_category = self.category_list.get(self.category_list.curselection())
            sites_path = os.path.join(categories_folder, selected_category, "Sites")
            
            if os.path.exists(sites_path):
                for site_folder in os.listdir(sites_path):
                    folder_path = os.path.join(sites_path, site_folder)
                    if os.path.isdir(folder_path):
                        display_name = site_folder.replace("_Reset", "")
                        self.sites_list.insert(END, f"📁 {display_name}")
                        # Insert files with proper indentation and make them selectable
                        for file in os.listdir(folder_path):
                            if file.endswith('.url') or file.endswith('.txt'):
                                self.sites_list.insert(END, f"    📄 {file}")
                            
        except Exception as e:
            print(f"Error loading sites: {str(e)}")

    def on_site_select(self, event):
        """Handle site selection"""
        if not self.sites_list.curselection():
            return
        
        try:
            if not self.category_list.curselection():
                return
            
            selected_category = self.category_list.get(self.category_list.curselection())
            selected_item = self.sites_list.get(self.sites_list.curselection())
            
            # Allow selection of both folders and files
            if selected_item.startswith("📁"):
                # Handle folder selection
                site_name = selected_item.replace("📁 ", "")
                self.display_details(selected_category, site_name)
            elif selected_item.startswith("    📄"):
                # Handle file selection
                file_name = selected_item.replace("    📄 ", "")
                folder_name = self.get_parent_folder(self.sites_list.curselection()[0])
                if folder_name:
                    site_name = folder_name.replace("📁 ", "")
                    self.display_details(selected_category, site_name)
                
            # Keep the selection highlighted
            self.sites_list.selection_set(self.sites_list.curselection())
            
        except Exception as e:
            print(f"Error selecting site: {str(e)}")

    def get_parent_folder(self, current_index):
        """Get parent folder name for a file"""
        try:
            while current_index >= 0:
                item = self.sites_list.get(current_index)
                if item.startswith("📁"):
                    return item
                current_index -= 1
        except Exception as e:
            print(f"Error getting parent folder: {str(e)}")
        return None

    def display_details(self, category, site):
        try:
            site_folder = os.path.join(categories_folder, category, "Sites", f"{site}_Reset")
            url_file = os.path.join(site_folder, f"{site}_Reset.url")
            txt_file = os.path.join(site_folder, f"{site}_Credentials.txt")
            
            self.selected_category_name.set(category)
            self.selected_site_name.set(site)
            
            if os.path.exists(url_file):
                with open(url_file, 'r') as f:
                    content = f.read()
                    url = content.split('URL=')[1].strip() if 'URL=' in content else ''
                    self.selected_reset_url.set(url)
            
            if os.path.exists(txt_file):
                with open(txt_file, 'r') as f:
                    content = f.read()
                    for line in content.split('\n'):
                        if 'Date:' in line:
                            self.selected_date.set(line.split('Date:')[1].strip())
                        elif 'Username:' in line:
                            self.selected_username.set(line.split('Username:')[1].strip())
                        elif 'Password:' in line:
                            self.selected_password.set(line.split('Password:')[1].strip())
            else:
                self.selected_date.set('')
                self.selected_username.set('')
                self.selected_password.set('')
                
        except Exception as e:
            print(f"Error displaying details: {str(e)}")

    def save_credentials(self):
        try:
            category = self.selected_category_name.get()
            site = self.selected_site_name.get()
            if not category or not site:
                return
            
            site_folder = os.path.join(categories_folder, category, "Sites", f"{site}_Reset")
            txt_file = os.path.join(site_folder, f"{site}_Credentials.txt")
            
            with open(txt_file, 'w') as f:
                f.write(f"Date: {self.selected_date.get()}\n")
                f.write(f"Username: {self.selected_username.get()}\n")
                f.write(f"Password: {self.selected_password.get()}\n")
            
            messagebox.showinfo("Success", "Credentials saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save credentials: {str(e)}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    create_folders()
    app = SecurityCheckManager()
    app.run()
