import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class PossessionFinanceAnalyzer:
    def __init__(self):
        self.commune = "La Possession"
        self.colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#F9A602', '#6A0572', 
                      '#AB83A1', '#5CAB7D', '#2A9D8F', '#E76F51', '#264653']
        
        self.start_year = 2002
        self.end_year = 2025
        
    def generate_financial_data(self):
        """Génère des données financières pour la commune de La Possession"""
        print("🏛️ Génération des données financières pour La Possession...")
        
        # Créer une base de données annuelle (les comptes communaux sont annuels)
        dates = pd.date_range(start=f'{self.start_year}-01-01', 
                             end=f'{self.end_year}-12-31', freq='Y')
        
        data = {'Annee': [date.year for date in dates]}
        
        # Données démographiques
        data['Population'] = self._simulate_population(dates)
        data['Menages'] = self._simulate_households(dates)
        
        # Recettes communales
        data['Recettes_Totales'] = self._simulate_total_revenue(dates)
        data['Impots_Locaux'] = self._simulate_tax_revenue(dates)
        data['Dotations_Etat'] = self._simulate_state_grants(dates)
        data['Autres_Recettes'] = self._simulate_other_revenue(dates)
        
        # Dépenses communales
        data['Depenses_Totales'] = self._simulate_total_expenses(dates)
        data['Fonctionnement'] = self._simulate_operating_expenses(dates)
        data['Investissement'] = self._simulate_investment_expenses(dates)
        data['Charge_Dette'] = self._simulate_debt_charges(dates)
        data['Personnel'] = self._simulate_staff_costs(dates)
        
        # indicateurs financiers
        data['Epargne_Brute'] = self._simulate_gross_savings(dates)
        data['Dette_Totale'] = self._simulate_total_debt(dates)
        data['Taux_Endettement'] = self._simulate_debt_ratio(dates)
        data['Taux_Fiscalite'] = self._simulate_tax_rate(dates)
        
        # Investissements spécifiques
        data['Investissement_Equipements'] = self._simulate_equipment_investment(dates)
        data['Investissement_Urbanisme'] = self._simulate_urban_planning_investment(dates)
        data['Investissement_Voirie'] = self._simulate_road_investment(dates)
        data['Investissement_Culture'] = self._simulate_culture_investment(dates)
        
        df = pd.DataFrame(data)
        
        # Ajouter des tendances spécifiques à La Possession
        self._add_municipal_trends(df)
        
        return df
    
    def _simulate_population(self, dates):
        """Simule la population de La Possession"""
        base_population = 25000  # population estimée en 2002
        
        population = []
        for i, date in enumerate(dates):
            # Croissance démographique annuelle d'environ 1.2% (forte croissance)
            growth = 1 + 0.012 * i
            population.append(base_population * growth)
        
        return population
    
    def _simulate_households(self, dates):
        """Simule le nombre de ménages"""
        base_households = 9000  # ménages en 2002
        
        households = []
        for i, date in enumerate(dates):
            # Croissance un peu plus rapide que la population (réduction de la taille des ménages)
            growth = 1 + 0.013 * i
            households.append(base_households * growth)
        
        return households
    
    def _simulate_total_revenue(self, dates):
        """Simule les recettes totales de la commune"""
        base_revenue = 25  # millions d'euros en 2002
        
        revenue = []
        for i, date in enumerate(dates):
            # Croissance régulière des recettes
            growth = 1 + 0.03 * i
            noise = np.random.normal(1, 0.05)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_tax_revenue(self, dates):
        """Simule les recettes fiscales"""
        base_tax = 10  # millions d'euros en 2002
        
        tax_revenue = []
        for i, date in enumerate(dates):
            # Croissance liée à l'augmentation de la population et de la valeur immobilière
            growth = 1 + 0.035 * i
            noise = np.random.normal(1, 0.06)
            tax_revenue.append(base_tax * growth * noise)
        
        return tax_revenue
    
    def _simulate_state_grants(self, dates):
        """Simule les dotations de l'État"""
        base_grants = 9  # millions d'euros en 2002
        
        grants = []
        for i, date in enumerate(dates):
            # Stagnation ou légère baisse des dotations de l'État
            year = date.year
            if year >= 2008:  # Baisse après 2008 (crise financière)
                reduction = 1 - 0.008 * (year - 2008)
            else:
                reduction = 1
            
            noise = np.random.normal(1, 0.04)
            grants.append(base_grants * reduction * noise)
        
        return grants
    
    def _simulate_other_revenue(self, dates):
        """Simule les autres recettes"""
        base_other = 6  # millions d'euros en 2002
        
        other_revenue = []
        for i, date in enumerate(dates):
            # Croissance modérée
            growth = 1 + 0.02 * i
            noise = np.random.normal(1, 0.07)
            other_revenue.append(base_other * growth * noise)
        
        return other_revenue
    
    def _simulate_total_expenses(self, dates):
        """Simule les dépenses totales"""
        base_expenses = 24  # millions d'euros en 2002
        
        expenses = []
        for i, date in enumerate(dates):
            # Croissance régulière des dépenses
            growth = 1 + 0.031 * i
            noise = np.random.normal(1, 0.05)
            expenses.append(base_expenses * growth * noise)
        
        return expenses
    
    def _simulate_operating_expenses(self, dates):
        """Simule les dépenses de fonctionnement"""
        base_operating = 16  # millions d'euros en 2002
        
        operating = []
        for i, date in enumerate(dates):
            # Croissance liée à l'inflation et à l'augmentation de la population
            growth = 1 + 0.025 * i
            noise = np.random.normal(1, 0.04)
            operating.append(base_operating * growth * noise)
        
        return operating
    
    def _simulate_investment_expenses(self, dates):
        """Simule les dépenses d'investissement"""
        base_investment = 8  # millions d'euros en 2002
        
        investment = []
        for i, date in enumerate(dates):
            # Variation plus importante selon les projets
            year = date.year
            if year in [2005, 2012, 2018, 2022]:  # Années avec gros investissements
                multiplier = 1.5
            elif year in [2008, 2014, 2020]:  # Années avec moins d'investissements (crises)
                multiplier = 0.7
            else:
                multiplier = 1.0
            
            growth = 1 + 0.02 * i
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _simulate_debt_charges(self, dates):
        """Simule les charges de la dette"""
        base_debt_charge = 2.0  # millions d'euros en 2002
        
        debt_charges = []
        for i, date in enumerate(dates):
            # Évolution selon le niveau d'endettement
            year = date.year
            if year >= 2005:
                increase = 1 + 0.01 * (year - 2005)
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.08)
            debt_charges.append(base_debt_charge * increase * noise)
        
        return debt_charges
    
    def _simulate_staff_costs(self, dates):
        """Simule les dépenses de personnel"""
        base_staff = 9  # millions d'euros en 2002
        
        staff_costs = []
        for i, date in enumerate(dates):
            # Croissance régulière
            growth = 1 + 0.026 * i
            noise = np.random.normal(1, 0.03)
            staff_costs.append(base_staff * growth * noise)
        
        return staff_costs
    
    def _simulate_gross_savings(self, dates):
        """Simule l'épargne brute"""
        savings = []
        for i, date in enumerate(dates):
            # Calculée comme recettes de fonctionnement - dépenses de fonctionnement
            base_saving = 2  # millions d'euros en 2002
            
            year = date.year
            if year >= 2010:  # Amélioration de la gestion
                improvement = 1 + 0.02 * (year - 2010)
            else:
                improvement = 1
            
            noise = np.random.normal(1, 0.1)
            savings.append(base_saving * improvement * noise)
        
        return savings
    
    def _simulate_total_debt(self, dates):
        """Simule la dette totale"""
        base_debt = 20  # millions d'euros en 2002
        
        debt = []
        for i, date in enumerate(dates):
            # Évolution de la dette
            year = date.year
            if year in [2005, 2012, 2018, 2022]:  # Augmentation lors des gros investissements
                change = 1.15
            elif year in [2010, 2015, 2020]:  # Réduction de la dette
                change = 0.9
            else:
                change = 1.0
            
            noise = np.random.normal(1, 0.07)
            debt.append(base_debt * change * noise)
        
        return debt
    
    def _simulate_debt_ratio(self, dates):
        """Simule le taux d'endettement"""
        ratios = []
        for i, date in enumerate(dates):
            # Taux d'endettement (dette/recettes)
            base_ratio = 0.8  # 80% en 2002
            
            year = date.year
            if year >= 2010:  # Amélioration progressive
                improvement = 1 - 0.02 * (year - 2010)
            else:
                improvement = 1
            
            noise = np.random.normal(1, 0.05)
            ratios.append(base_ratio * improvement * noise)
        
        return ratios
    
    def _simulate_tax_rate(self, dates):
        """Simule le taux de fiscalité (moyen)"""
        rates = []
        for i, date in enumerate(dates):
            # Taux de fiscalité moyen
            base_rate = 1.1  # en 2002
            
            year = date.year
            if year >= 2010:  # Légère augmentation
                increase = 1 + 0.005 * (year - 2010)
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.02)
            rates.append(base_rate * increase * noise)
        
        return rates
    
    def _simulate_equipment_investment(self, dates):
        """Simule l'investissement en équipements"""
        base_investment = 2.0  # millions d'euros en 2002
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2005, 2013, 2019, 2024]:  # Gros investissements
                multiplier = 1.8
            else:
                multiplier = 1.0
            
            growth = 1 + 0.015 * i
            noise = np.random.normal(1, 0.12)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _simulate_urban_planning_investment(self, dates):
        """Simule l'investissement en urbanisme"""
        base_investment = 1.5  # millions d'euros en 2002
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2006, 2015, 2021, 2025]:  # Gros investissements
                multiplier = 2.0
            else:
                multiplier = 1.0
            
            growth = 1 + 0.02 * i
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _simulate_road_investment(self, dates):
        """Simule l'investissement en voirie"""
        base_investment = 1.3  # millions d'euros en 2002
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2004, 2007, 2014, 2017, 2022, 2025]:  # Gros investissements
                multiplier = 1.7
            else:
                multiplier = 1.0
            
            growth = 1 + 0.018 * i
            noise = np.random.normal(1, 0.13)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _simulate_culture_investment(self, dates):
        """Simule l'investissement culturel"""
        base_investment = 0.5  # millions d'euros en 2002
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2008, 2016, 2020, 2024]:  # Gros investissements culturels
                multiplier = 2.5
            else:
                multiplier = 1.0
            
            growth = 1 + 0.025 * i
            noise = np.random.normal(1, 0.2)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _add_municipal_trends(self, df):
        """Ajoute des tendances municipales réalistes"""
        for i, row in df.iterrows():
            year = row['Annee']
            
            # Développement initial (2002-2005)
            if 2002 <= year <= 2005:
                df.loc[i, 'Investissement_Urbanisme'] *= 1.3
                df.loc[i, 'Investissement_Voirie'] *= 1.4
            
            # Impact de la crise financière (2008-2009)
            if 2008 <= year <= 2009:
                df.loc[i, 'Recettes_Totales'] *= 0.95
                df.loc[i, 'Investissement'] *= 0.85
                df.loc[i, 'Autres_Recettes'] *= 0.9
            
            # Développement urbain accéléré (2010-2015)
            elif 2010 <= year <= 2015:
                df.loc[i, 'Investissement_Urbanisme'] *= 1.2
                df.loc[i, 'Investissement_Voirie'] *= 1.15
                df.loc[i, 'Population'] *= 1.02  # Accélération démographique
            
            # Impact de la crise COVID-19 (2020-2021)
            if 2020 <= year <= 2021:
                if year == 2020:
                    # Baisse des recettes fiscales, augmentation des dépenses sociales
                    df.loc[i, 'Impots_Locaux'] *= 0.95
                    df.loc[i, 'Autres_Recettes'] *= 0.9
                    df.loc[i, 'Fonctionnement'] *= 1.05
            
            # Vieillissement de la population (augmentation des dépenses sociales)
            if year >= 2010:
                aging = 1 + 0.01 * (year - 2010)
                df.loc[i, 'Fonctionnement'] *= aging
            
            # Politique de développement culturel (à partir de 2012)
            if year >= 2012:
                culture_growth = 1 + 0.03 * (year - 2012)
                df.loc[i, 'Investissement_Culture'] *= culture_growth
            
            # Plan de relance post-COVID (2022-2025)
            if year >= 2022:
                df.loc[i, 'Investissement'] *= 1.1
                df.loc[i, 'Investissement_Equipements'] *= 1.05
    
    def create_financial_analysis(self, df):
        """Crée une analyse complète des finances communales"""
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 20))
        
        # 1. Évolution des recettes et dépenses
        ax1 = plt.subplot(3, 2, 1)
        self._plot_revenue_expenses(df, ax1)
        
        # 2. Structure des recettes
        ax2 = plt.subplot(3, 2, 2)
        self._plot_revenue_structure(df, ax2)
        
        # 3. Structure des dépenses
        ax3 = plt.subplot(3, 2, 3)
        self._plot_expenses_structure(df, ax3)
        
        # 4. Investissements communaux
        ax4 = plt.subplot(3, 2, 4)
        self._plot_investments(df, ax4)
        
        # 5. Dette et endettement
        ax5 = plt.subplot(3, 2, 5)
        self._plot_debt(df, ax5)
        
        # 6. Indicateurs de performance
        ax6 = plt.subplot(3, 2, 6)
        self._plot_performance_indicators(df, ax6)
        
        plt.suptitle(f'Analyse des Comptes Communaux de La Possession ({self.start_year}-{self.end_year})', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig('possession_financial_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Générer les insights
        self._generate_financial_insights(df)
    
    def _plot_revenue_expenses(self, df, ax):
        """Plot de l'évolution des recettes et dépenses"""
        ax.plot(df['Annee'], df['Recettes_Totales'], label='Recettes Totales', 
               linewidth=2, color='#2A9D8F', alpha=0.8)
        ax.plot(df['Annee'], df['Depenses_Totales'], label='Dépenses Totales', 
               linewidth=2, color='#E76F51', alpha=0.8)
        
        ax.set_title('Évolution des Recettes et Dépenses (M€)', 
                    fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_revenue_structure(self, df, ax):
        """Plot de la structure des recettes"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Impots_Locaux', 'Dotations_Etat', 'Autres_Recettes']
        colors = ['#264653', '#2A9D8F', '#E76F51']
        labels = ['Impôts Locaux', 'Dotations État', 'Autres Recettes']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Recettes (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_expenses_structure(self, df, ax):
        """Plot de la structure des dépenses"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Fonctionnement', 'Investissement', 'Charge_Dette', 'Personnel']
        colors = ['#264653', '#2A9D8F', '#E76F51', '#F9A602']
        labels = ['Fonctionnement', 'Investissement', 'Charge Dette', 'Personnel']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Dépenses (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_investments(self, df, ax):
        """Plot des investissements communaux"""
        ax.plot(df['Annee'], df['Investissement_Equipements'], label='Équipements', 
               linewidth=2, color='#264653', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Urbanisme'], label='Urbanisme', 
               linewidth=2, color='#2A9D8F', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Voirie'], label='Voirie', 
               linewidth=2, color='#E76F51', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Culture'], label='Culture', 
               linewidth=2, color='#F9A602', alpha=0.8)
        
        ax.set_title('Répartition des Investissements (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_debt(self, df, ax):
        """Plot de la dette et du taux d'endettement"""
        # Dette totale
        ax.bar(df['Annee'], df['Dette_Totale'], label='Dette Totale (M€)', 
              color='#264653', alpha=0.7)
        
        ax.set_title('Dette Communale et Taux d\'Endettement', fontsize=12, fontweight='bold')
        ax.set_ylabel('Dette (M€)', color='#264653')
        ax.tick_params(axis='y', labelcolor='#264653')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Taux d'endettement en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Taux_Endettement'], label='Taux d\'Endettement', 
                linewidth=3, color='#E76F51')
        ax2.set_ylabel('Taux d\'Endettement', color='#E76F51')
        ax2.tick_params(axis='y', labelcolor='#E76F51')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_performance_indicators(self, df, ax):
        """Plot des indicateurs de performance"""
        # Épargne brute
        ax.bar(df['Annee'], df['Epargne_Brute'], label='Épargne Brute (M€)', 
              color='#2A9D8F', alpha=0.7)
        
        ax.set_title('Indicateurs de Performance', fontsize=12, fontweight='bold')
        ax.set_ylabel('Épargne Brute (M€)', color='#2A9D8F')
        ax.tick_params(axis='y', labelcolor='#2A9D8F')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Taux de fiscalité en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Taux_Fiscalite'], label='Taux de Fiscalité', 
                linewidth=3, color='#F9A602')
        ax2.set_ylabel('Taux de Fiscalité', color='#F9A602')
        ax2.tick_params(axis='y', labelcolor='#F9A602')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _generate_financial_insights(self, df):
        """Génère des insights analytiques"""
        print(f"🏛️ INSIGHTS ANALYTIQUES - Commune de La Possession")
        print("=" * 60)
        
        # 1. Statistiques de base
        print("\n1. 📈 STATISTIQUES GÉNÉRALES:")
        avg_revenue = df['Recettes_Totales'].mean()
        avg_expenses = df['Depenses_Totales'].mean()
        avg_savings = df['Epargne_Brute'].mean()
        avg_debt = df['Dette_Totale'].mean()
        
        print(f"Recettes moyennes annuelles: {avg_revenue:.2f} M€")
        print(f"Dépenses moyennes annuelles: {avg_expenses:.2f} M€")
        print(f"Épargne brute moyenne: {avg_savings:.2f} M€")
        print(f"Dette moyenne: {avg_debt:.2f} M€")
        
        # 2. Croissance
        print("\n2. 📊 TAUX DE CROISSANCE:")
        revenue_growth = ((df['Recettes_Totales'].iloc[-1] / 
                          df['Recettes_Totales'].iloc[0]) - 1) * 100
        population_growth = ((df['Population'].iloc[-1] / 
                             df['Population'].iloc[0]) - 1) * 100
        
        print(f"Croissance des recettes ({self.start_year}-{self.end_year}): {revenue_growth:.1f}%")
        print(f"Croissance de la population ({self.start_year}-{self.end_year}): {population_growth:.1f}%")
        
        # 3. Structure financière
        print("\n3. 📋 STRUCTURE FINANCIÈRE:")
        tax_share = (df['Impots_Locaux'].mean() / df['Recettes_Totales'].mean()) * 100
        state_share = (df['Dotations_Etat'].mean() / df['Recettes_Totales'].mean()) * 100
        investment_share = (df['Investissement'].mean() / df['Depenses_Totales'].mean()) * 100
        
        print(f"Part des impôts locaux dans les recettes: {tax_share:.1f}%")
        print(f"Part des dotations de l'État dans les recettes: {state_share:.1f}%")
        print(f"Part de l'investissement dans les dépenses: {investment_share:.1f}%")
        
        # 4. Dette et fiscalité
        print("\n4. 💰 ENDETTEMENT ET FISCALITÉ:")
        avg_debt_ratio = df['Taux_Endettement'].mean() * 100
        avg_tax_rate = df['Taux_Fiscalite'].mean()
        last_debt_ratio = df['Taux_Endettement'].iloc[-1] * 100
        
        print(f"Taux d'endettement moyen: {avg_debt_ratio:.1f}%")
        print(f"Taux d'endettement final: {last_debt_ratio:.1f}%")
        print(f"Taux de fiscalité moyen: {avg_tax_rate:.2f}")
        
        # 5. Événements marquants
        print("\n5. 📅 ÉVÉNEMENTS MARQUANTS:")
        print("• 2002-2005: Développement initial de la commune")
        print("• 2008-2009: Impact de la crise financière mondiale")
        print("• 2010-2015: Accélération du développement urbain")
        print("• 2020-2021: Gestion de la crise COVID-19")
        print("• 2022-2025: Plan de relance post-COVID")
        
        # 6. Recommandations
        print("\n6. 💡 RECOMMANDATIONS STRATÉGIQUES:")
        print("• Maintenir une politique d'investissement équilibrée")
        print("• Diversifier les sources de recettes face à la baisse des dotations de l'État")
        print("• Optimiser la gestion de la dette")
        print("• Adapter les services aux besoins d'une population croissante")
        print("• Développer des partenariats public-privé pour les grands projets")
        print("• Renforcer la transparence budgétaire auprès des citoyens")

def main():
    """Fonction principale"""
    print("🏛️ ANALYSE DES COMPTES COMMUNAUX DE LA POSSESSION (2002-2025)")
    print("=" * 60)
    
    # Initialiser l'analyseur
    analyzer = PossessionFinanceAnalyzer()
    
    # Générer les données
    financial_data = analyzer.generate_financial_data()
    
    # Sauvegarder les données
    output_file = 'possession_financial_data_2002_2025.csv'
    financial_data.to_csv(output_file, index=False)
    print(f"💾 Données sauvegardées: {output_file}")
    
    # Aperçu des données
    print("\n👀 Aperçu des données:")
    print(financial_data[['Annee', 'Population', 'Recettes_Totales', 'Depenses_Totales', 'Dette_Totale']].head())
    
    # Créer l'analyse
    print("\n📈 Création de l'analyse financière...")
    analyzer.create_financial_analysis(financial_data)
    
    print(f"\n✅ Analyse des comptes communaux de La Possession terminée!")
    print(f"📊 Période: {analyzer.start_year}-{analyzer.end_year}")
    print("📦 Données: Démographie, finances, investissements, dette")

if __name__ == "__main__":
    main()