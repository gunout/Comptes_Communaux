import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class SaintDenisFinanceAnalyzer:
    def __init__(self):
        self.commune = "Saint-Denis"
        self.colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#F9A602', '#6A0572', 
                      '#AB83A1', '#5CAB7D', '#2A9D8F', '#E76F51', '#264653']
        
        self.start_year = 2002
        self.end_year = 2025
        
    def generate_financial_data(self):
        """Génère des données financières pour la commune de Saint-Denis"""
        print("🏛️ Génération des données financières pour Saint-Denis...")
        
        # Créer une base de données annuelle
        dates = pd.date_range(start=f'{self.start_year}-01-01', 
                             end=f'{self.end_year}-12-31', freq='Y')
        
        data = {'Annee': [date.year for date in dates]}
        
        # Données démographiques (préfecture, ville la plus peuplée)
        data['Population'] = self._simulate_population(dates)
        data['Menages'] = self._simulate_households(dates)
        
        # Recettes communales (budget important pour la préfecture)
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
        
        # Indicateurs financiers
        data['Epargne_Brute'] = self._simulate_gross_savings(dates)
        data['Dette_Totale'] = self._simulate_total_debt(dates)
        data['Taux_Endettement'] = self._simulate_debt_ratio(dates)
        data['Taux_Fiscalite'] = self._simulate_tax_rate(dates)
        
        # Investissements spécifiques (adaptés à Saint-Denis)
        data['Investissement_Administratif'] = self._simulate_administrative_investment(dates)
        data['Investissement_Universite'] = self._simulate_university_investment(dates)
        data['Investissement_Culture'] = self._simulate_culture_investment(dates)
        data['Investissement_Transport'] = self._simulate_transport_investment(dates)
        data['Investissement_Urbanisme'] = self._simulate_urban_planning_investment(dates)
        
        df = pd.DataFrame(data)
        
        # Ajouter des tendances spécifiques à Saint-Denis
        self._add_municipal_trends(df)
        
        return df
    
    def _simulate_population(self, dates):
        """Simule la population de Saint-Denis (préfecture, ville la plus peuplée)"""
        base_population = 135000  # population estimée en 2002
        
        population = []
        for i, date in enumerate(dates):
            # Croissance démographique modérée (ville mature)
            growth = 1 + 0.01 * i
            population.append(base_population * growth)
        
        return population
    
    def _simulate_households(self, dates):
        """Simule le nombre de ménages"""
        base_households = 45000  # ménages en 2002
        
        households = []
        for i, date in enumerate(dates):
            # Croissance démographique
            growth = 1 + 0.009 * i
            households.append(base_households * growth)
        
        return households
    
    def _simulate_total_revenue(self, dates):
        """Simule les recettes totales de la commune"""
        base_revenue = 120  # millions d'euros en 2002 (budget important)
        
        revenue = []
        for i, date in enumerate(dates):
            # Croissance régulière des recettes
            growth = 1 + 0.033 * i
            noise = np.random.normal(1, 0.05)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_tax_revenue(self, dates):
        """Simule les recettes fiscales"""
        base_tax = 55  # millions d'euros en 2002
        
        tax_revenue = []
        for i, date in enumerate(dates):
            # Croissance liée à l'activité économique
            growth = 1 + 0.035 * i
            noise = np.random.normal(1, 0.06)
            tax_revenue.append(base_tax * growth * noise)
        
        return tax_revenue
    
    def _simulate_state_grants(self, dates):
        """Simule les dotations de l'État"""
        base_grants = 45  # millions d'euros en 2002 (préfecture)
        
        grants = []
        for i, date in enumerate(dates):
            # Dotations importantes pour préfecture
            year = date.year
            if year >= 2008:  # Légère baisse après 2008
                reduction = 1 - 0.003 * (year - 2008)
            else:
                reduction = 1
            
            noise = np.random.normal(1, 0.04)
            grants.append(base_grants * reduction * noise)
        
        return grants
    
    def _simulate_other_revenue(self, dates):
        """Simule les autres recettes"""
        base_other = 20  # millions d'euros en 2002
        
        other_revenue = []
        for i, date in enumerate(dates):
            # Croissance modérée
            growth = 1 + 0.032 * i
            noise = np.random.normal(1, 0.07)
            other_revenue.append(base_other * growth * noise)
        
        return other_revenue
    
    def _simulate_total_expenses(self, dates):
        """Simule les dépenses totales"""
        base_expenses = 115  # millions d'euros en 2002
        
        expenses = []
        for i, date in enumerate(dates):
            # Croissance régulière des dépenses
            growth = 1 + 0.032 * i
            noise = np.random.normal(1, 0.05)
            expenses.append(base_expenses * growth * noise)
        
        return expenses
    
    def _simulate_operating_expenses(self, dates):
        """Simule les dépenses de fonctionnement"""
        base_operating = 70  # millions d'euros en 2002
        
        operating = []
        for i, date in enumerate(dates):
            # Croissance liée à l'inflation et aux services publics
            growth = 1 + 0.03 * i
            noise = np.random.normal(1, 0.04)
            operating.append(base_operating * growth * noise)
        
        return operating
    
    def _simulate_investment_expenses(self, dates):
        """Simule les dépenses d'investissement"""
        base_investment = 45  # millions d'euros en 2002
        
        investment = []
        for i, date in enumerate(dates):
            # Variation selon les projets
            year = date.year
            if year in [2005, 2010, 2015, 2020]:  # Années avec investissements
                multiplier = 1.6
            elif year in [2008, 2013, 2019]:  # Années avec moins d'investissements
                multiplier = 0.85
            else:
                multiplier = 1.0
            
            growth = 1 + 0.031 * i
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _simulate_debt_charges(self, dates):
        """Simule les charges de la dette"""
        base_debt_charge = 8  # millions d'euros en 2002
        
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
        base_staff = 50  # millions d'euros en 2002 (préfecture)
        
        staff_costs = []
        for i, date in enumerate(dates):
            # Croissance régulière
            growth = 1 + 0.029 * i
            noise = np.random.normal(1, 0.03)
            staff_costs.append(base_staff * growth * noise)
        
        return staff_costs
    
    def _simulate_gross_savings(self, dates):
        """Simule l'épargne brute"""
        savings = []
        for i, date in enumerate(dates):
            # Épargne modérée
            base_saving = 6  # millions d'euros en 2002
            
            year = date.year
            if year >= 2010:  # Amélioration progressive
                improvement = 1 + 0.014 * (year - 2010)
            else:
                improvement = 1
            
            noise = np.random.normal(1, 0.1)
            savings.append(base_saving * improvement * noise)
        
        return savings
    
    def _simulate_total_debt(self, dates):
        """Simule la dette totale"""
        base_debt = 90  # millions d'euros en 2002
        
        debt = []
        for i, date in enumerate(dates):
            # Évolution de la dette
            year = date.year
            if year in [2005, 2010, 2015, 2020]:  # Augmentation lors des investissements
                change = 1.16
            elif year in [2008, 2013, 2018, 2023]:  # Réduction de la dette
                change = 0.92
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
            base_ratio = 0.75  # 75% en 2002
            
            year = date.year
            if year >= 2010:  # Amélioration progressive
                improvement = 1 - 0.015 * (year - 2010)
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
            base_rate = 1.18  # en 2002
            
            year = date.year
            if year >= 2010:  # Légère augmentation
                increase = 1 + 0.005 * (year - 2010)
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.02)
            rates.append(base_rate * increase * noise)
        
        return rates
    
    def _simulate_administrative_investment(self, dates):
        """Simule l'investissement administratif (spécifique à Saint-Denis)"""
        base_investment = 8  # millions d'euros en 2002
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2006, 2011, 2016, 2021]:  # Gros investissements administratifs
                multiplier = 1.7
            else:
                multiplier = 1.0
            
            growth = 1 + 0.028 * i
            noise = np.random.normal(1, 0.12)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _simulate_university_investment(self, dates):
        """Simule l'investissement universitaire (spécifique à Saint-Denis)"""
        base_investment = 7  # millions d'euros en 2002
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2007, 2012, 2017, 2022]:  # Investissements universitaires
                multiplier = 1.8
            else:
                multiplier = 1.0
            
            growth = 1 + 0.032 * i
            noise = np.random.normal(1, 0.14)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _simulate_culture_investment(self, dates):
        """Simule l'investissement culturel (spécifique à Saint-Denis)"""
        base_investment = 5  # millions d'euros en 2002
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2008, 2013, 2018, 2023]:  # Investissements culturels
                multiplier = 1.9
            else:
                multiplier = 1.0
            
            growth = 1 + 0.03 * i
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _simulate_transport_investment(self, dates):
        """Simule l'investissement en transport (spécifique à Saint-Denis)"""
        base_investment = 6  # millions d'euros en 2002
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2005, 2010, 2015, 2020]:  # Gros investissements en transport
                multiplier = 1.8
            else:
                multiplier = 1.0
            
            growth = 1 + 0.031 * i
            noise = np.random.normal(1, 0.17)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _simulate_urban_planning_investment(self, dates):
        """Simule l'investissement en urbanisme (spécifique à Saint-Denis)"""
        base_investment = 7  # millions d'euros en 2002
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2009, 2014, 2019, 2024]:  # Investissements en urbanisme
                multiplier = 1.7
            else:
                multiplier = 1.0
            
            growth = 1 + 0.029 * i
            noise = np.random.normal(1, 0.16)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _add_municipal_trends(self, df):
        """Ajoute des tendances municipales réalistes pour Saint-Denis"""
        for i, row in df.iterrows():
            year = row['Annee']
            
            # Développement initial (2002-2005)
            if 2002 <= year <= 2005:
                df.loc[i, 'Investissement_Administratif'] *= 1.4
                df.loc[i, 'Investissement_Transport'] *= 1.3
            
            # Impact de la crise financière (2008-2009)
            if 2008 <= year <= 2009:
                df.loc[i, 'Recettes_Totales'] *= 0.95
                df.loc[i, 'Investissement'] *= 0.83
                df.loc[i, 'Autres_Recettes'] *= 0.9
            
            # Développement accéléré (2010-2015)
            elif 2010 <= year <= 2015:
                df.loc[i, 'Investissement_Universite'] *= 1.3
                df.loc[i, 'Investissement_Culture'] *= 1.25
            
            # Impact de la crise COVID-19 (2020-2021)
            if 2020 <= year <= 2021:
                if year == 2020:
                    # Baisse des recettes
                    df.loc[i, 'Autres_Recettes'] *= 0.87
                    df.loc[i, 'Impots_Locaux'] *= 0.94
            
            # Vieillissement de la population (augmentation des dépenses sociales)
            if year >= 2010:
                aging = 1 + 0.011 * (year - 2010)
                df.loc[i, 'Fonctionnement'] *= aging
            
            # Politique de développement universitaire (à partir de 2012)
            if year >= 2012:
                university_growth = 1 + 0.028 * (year - 2012)
                df.loc[i, 'Investissement_Universite'] *= university_growth
            
            # Développement culturel (spécifique à Saint-Denis)
            if year >= 2010:
                culture_growth = 1 + 0.026 * (year - 2010)
                df.loc[i, 'Investissement_Culture'] *= culture_growth
            
            # Plan de relance post-COVID (2022-2025)
            if year >= 2022:
                df.loc[i, 'Investissement'] *= 1.14
                df.loc[i, 'Investissement_Transport'] *= 1.16
                df.loc[i, 'Investissement_Urbanisme'] *= 1.15
    
    def create_financial_analysis(self, df):
        """Crée une analyse complète des finances communales"""
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 24))
        
        # 1. Évolution des recettes et dépenses
        ax1 = plt.subplot(4, 2, 1)
        self._plot_revenue_expenses(df, ax1)
        
        # 2. Structure des recettes
        ax2 = plt.subplot(4, 2, 2)
        self._plot_revenue_structure(df, ax2)
        
        # 3. Structure des dépenses
        ax3 = plt.subplot(4, 2, 3)
        self._plot_expenses_structure(df, ax3)
        
        # 4. Investissements communaux
        ax4 = plt.subplot(4, 2, 4)
        self._plot_investments(df, ax4)
        
        # 5. Dette et endettement
        ax5 = plt.subplot(4, 2, 5)
        self._plot_debt(df, ax5)
        
        # 6. Indicateurs de performance
        ax6 = plt.subplot(4, 2, 6)
        self._plot_performance_indicators(df, ax6)
        
        # 7. Démographie
        ax7 = plt.subplot(4, 2, 7)
        self._plot_demography(df, ax7)
        
        # 8. Investissements sectoriels
        ax8 = plt.subplot(4, 2, 8)
        self._plot_sectorial_investments(df, ax8)
        
        plt.suptitle(f'Analyse des Comptes Communaux de Saint-Denis ({self.start_year}-{self.end_year})', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig('saint_denis_financial_analysis.png', dpi=300, bbox_inches='tight')
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
        ax.plot(df['Annee'], df['Investissement_Administratif'], label='Administratif', 
               linewidth=2, color='#264653', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Universite'], label='Université', 
               linewidth=2, color='#2A9D8F', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Culture'], label='Culture', 
               linewidth=2, color='#E76F51', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Transport'], label='Transport', 
               linewidth=2, color='#F9A602', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Urbanisme'], label='Urbanisme', 
               linewidth=2, color='#6A0572', alpha=0.8)
        
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
    
    def _plot_demography(self, df, ax):
        """Plot de l'évolution démographique"""
        ax.plot(df['Annee'], df['Population'], label='Population', 
               linewidth=2, color='#264653', alpha=0.8)
        
        ax.set_title('Évolution Démographique', fontsize=12, fontweight='bold')
        ax.set_ylabel('Population', color='#264653')
        ax.tick_params(axis='y', labelcolor='#264653')
        ax.grid(True, alpha=0.3)
        
        # Nombre de ménages en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Menages'], label='Ménages', 
                linewidth=2, color='#E76F51', alpha=0.8)
        ax2.set_ylabel('Ménages', color='#E76F51')
        ax2.tick_params(axis='y', labelcolor='#E76F51')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_sectorial_investments(self, df, ax):
        """Plot des investissements sectoriels"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Investissement_Administratif', 'Investissement_Universite', 
                     'Investissement_Culture', 'Investissement_Transport', 'Investissement_Urbanisme']
        colors = ['#264653', '#2A9D8F', '#E76F51', '#F9A602', '#6A0572']
        labels = ['Administratif', 'Université', 'Culture', 'Transport', 'Urbanisme']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Répartition Sectorielle des Investissements (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _generate_financial_insights(self, df):
        """Génère des insights analytiques"""
        print(f"🏛️ INSIGHTS ANALYTIQUES - Commune de Saint-Denis")
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
        
        # 5. Spécificités de Saint-Denis
        print("\n5. 🏛️ SPÉCIFICITÉS COMMUNALES:")
        avg_admin_investment = df['Investissement_Administratif'].mean()
        admin_share = (df['Investissement_Administratif'].mean() / df['Investissement'].mean()) * 100
        university_share = (df['Investissement_Universite'].mean() / df['Investissement'].mean()) * 100
        
        print(f"Investissement administratif moyen: {avg_admin_investment:.2f} M€")
        print(f"Part de l'administration dans l'investissement: {admin_share:.1f}%")
        print(f"Part de l'université dans l'investissement: {university_share:.1f}%")
        
        # 6. Événements marquants
        print("\n6. 📅 ÉVÉNEMENTS MARQUANTS:")
        print("• 2002-2005: Développement initial de la préfecture")
        print("• 2006-2007: Investissements dans les infrastructures administratives")
        print("• 2008-2009: Impact de la crise financière mondiale")
        print("• 2010-2015: Développement de l'université et des infrastructures culturelles")
        print("• 2020-2021: Impact de la crise COVID-19 sur l'économie locale")
        print("• 2022-2025: Plan de relance axé sur les transports et l'urbanisme")
        
        # 7. Recommandations
        print("\n7. 💡 RECOMMANDATIONS STRATÉGIQUES:")
        print("• Capitaliser sur le statut de préfecture et de capitale administrative")
        print("• Développer le pôle universitaire et de recherche")
        print("• Améliorer les transports et la mobilité urbaine")
        print("• Renforcer l'attractivité culturelle (musées, festivals, patrimoine)")
        print("• Moderniser les infrastructures administratives")
        print("• Gérer la densification urbaine et développer les espaces verts")
        print("• Maintenir un équilibre entre développement économique et qualité de vie")

def main():
    """Fonction principale"""
    print("🏛️ ANALYSE DES COMPTES COMMUNAUX DE SAINT-DENIS (2002-2025)")
    print("=" * 60)
    
    # Initialiser l'analyseur
    analyzer = SaintDenisFinanceAnalyzer()
    
    # Générer les données
    financial_data = analyzer.generate_financial_data()
    
    # Sauvegarder les données
    output_file = 'saint_denis_financial_data_2002_2025.csv'
    financial_data.to_csv(output_file, index=False)
    print(f"💾 Données sauvegardées: {output_file}")
    
    # Aperçu des données
    print("\n👀 Aperçu des données:")
    print(financial_data[['Annee', 'Population', 'Recettes_Totales', 'Depenses_Totales', 'Dette_Totale']].head())
    
    # Créer l'analyse
    print("\n📈 Création de l'analyse financière...")
    analyzer.create_financial_analysis(financial_data)
    
    print(f"\n✅ Analyse des comptes communaux de Saint-Denis terminée!")
    print(f"📊 Période: {analyzer.start_year}-{analyzer.end_year}")
    print("📦 Données: Démographie, finances, investissements, dette")
    print("🏛️ Spécificité: Focus sur les investissements administratifs, universitaires et culturels")

if __name__ == "__main__":
    main()