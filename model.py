from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def train_models(df):

    df['target'] = (df['return_1'].shift(-1) < 0).astype(int)
    df.dropna(inplace=True)

    features = [c for c in df.columns if c not in ['target']]

    X = df[features].values
    y = df['target'].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    lr = LogisticRegression(max_iter=1000)
    rf = RandomForestClassifier()

    lr.fit(X_scaled, y)
    rf.fit(X_scaled, y)

    today = X_scaled[-1:]

    prob_lr = lr.predict_proba(today)[0][1]
    prob_rf = rf.predict_proba(today)[0][1]

    return prob_lr, prob_rf
