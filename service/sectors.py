import copy

from model.sector import Sector


class Sectors:
    def __init__(self):
        self.sectors_data = []
        self.roots = []
        self.order = []
        self.final_sectors_data = {}
        self.main()

    def get_sectors_from_db(self):
        for sector in Sector.select():
            if not sector.root_sector_id:
                self.roots.append(sector)
            self.sectors_data.append(sector)
        return self.sectors_data

    def sort_sectors(self, roots):
        if not roots:
            return
        for root in range(len(roots)):
            self.order.append(roots[root])
            new_root = []
            for sector in self.sectors_data:
                if root + 1 < len(roots) and sector.root_sector_id and roots[root + 1].sector_id > \
                        sector.root_sector_id.sector_id == roots[root].sector_id:
                    new_root.append(sector)
                if root + 1 == len(roots) and sector.root_sector_id and sector.root_sector_id.sector_id == roots[
                    root].sector_id:
                    new_root.append(sector)
            self.sort_sectors(new_root)
        return

    def format_data(self):
        for s_id in range(len(self.order)):
            sector = self.order[s_id]
            self.final_sectors_data[s_id] = {}
            self.final_sectors_data[s_id]["id"] = sector.sector_id
            self.final_sectors_data[s_id]["name"] = sector.name
            self.final_sectors_data[s_id]["root_sector_id"] = sector.root_sector_id
            if sector.root_sector_id:
                self.final_sectors_data[s_id]["root_sector_id"] = sector.root_sector_id.sector_id
            self.final_sectors_data[s_id]["indent"] = 0
            self.final_sectors_data[s_id]["indent"] += self.get_root_sector_spacing_count(sector)

    def get_root_sector_spacing_count(self, sector):
        for s_key in self.final_sectors_data.keys():
            if sector.root_sector_id and self.final_sectors_data[s_key]["id"] == sector.root_sector_id.sector_id:
                return self.final_sectors_data[s_key]["indent"] + 1
        return 0

    def main(self):
        self.get_sectors_from_db()
        roots = copy.deepcopy(self.roots)
        self.sort_sectors(roots)
        self.format_data()

    def get_sectors(self):
        return self.final_sectors_data
