'''
Support Vector Machine Project
Iris Flower Data Set
'''
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV

def load_data():
    iris = sns.load_dataset('iris')
    print(iris.info())
    return iris

def explore_data(dataframe):
    sns.pairplot(dataframe, hue = 'species')
    plt.show()
    setosa = dataframe[dataframe['species']=='setosa']
    sns.jointplot('sepal_length', 'sepal_width', data = setosa, kind = 'kde')
    plt.show()

def split_data(dataframe):
    X= dataframe.drop('species', axis = 1)
    y = dataframe['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    model = SVC()
    model.fit(X_train, y_train)
    return model

def model_evaluation(model, X_test, y_test):
    predictions = model.predict(X_test)
    print(confusion_matrix(y_test, predictions))
    print('\n')
    print(classification_report(y_test, predictions))

def grid_search(X_train,X_test,y_train, y_test):
    param_grid = {'C': [0.1,1,10,100,1000], 'gamma': [0.1,0.01,0.001,0.0001]}
    grid = GridSearchCV(SVC(), param_grid, verbose=3)
    grid.fit(X_train, y_train)
    grid_predictions = grid.predict(X_test)
    print(classification_report(y_test, grid_predictions))
    print('\n')
    print(confusion_matrix(y_test, grid_predictions))


if __name__ == '__main__':
    iris = load_data()
    explore = input('Would you like to explore the data?')
    if explore == 'yes':
        explore_data(iris)
    data = split_data(iris)
    X_train = data[0]
    X_test = data[1]
    y_train = data[2]
    y_test = data[3]
    model = train_model(X_train, y_train)
    model_evaluation(model, X_test, y_test)
    grid = input('Would you like to run a grid search for the model?')
    if grid == 'yes':
        grid_search(X_train, X_test, y_train, y_test)