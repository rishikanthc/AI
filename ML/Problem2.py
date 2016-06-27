'''
Created on Nov 15, 2014

@author: nandini1986
'''

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as ax
from numpy import transpose
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import StratifiedKFold
from sklearn import svm
from sklearn.ensemble.forest import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeClassifier

A = []
B = []
class0_A = []
class1_A = []
class0_B = []
class1_B = []
label = []
AB = []
A_train_fold = []
B_train_fold = []
A_test_fold = []
B_test_fold = []
Z_test = []

def fileParse():
    file = open('chessboard.csv', 'r')
    content = file.read()
    lines = content.split('\n')
    temp = []
    for line in lines:
        temp.append(line.split('\r'))
    for data in temp[0]:
        row = data.split(',')
        if row[0]== 'A':
            continue
        A.append(float(row[0]))
        B.append(float(row[1]))
        label.append(float(row[2]))

    for i in range(len(A)):
        AB.append([float(A[i]),float(B[i])])
        if label[i] == 1 :
            class1_A.append(float(A[i]))
            class1_B.append(float(B[i]))
        elif label[i] == 0:
            class0_A.append(float(A[i]))
            class0_B.append(float(B[i]))

    plot0 = plt.scatter(class0_A, class0_B, marker='o', color = 'red')
    plot1 = plt.scatter(class1_A,class1_B, marker = 'o', color = 'black')
    plt.legend((plot0, plot1), ('label 0', 'label 1'), scatterpoints = 1)
    plt.title("Scatter Plot")
    plt.xlabel('A')
    plt.ylabel('B')
    plt.show()

def linearSVMStats():
    print "==================================Linear SVM=================================="
    CC = [1, 10, 50, 100]
    for c in CC:
        score = 0
        for train, test in skf:
            for i in xrange(len(train)):
                A_train_fold.append(A_train[i])
                B_train_fold.append(B_train[i])
            for i in xrange(len(test)):
                A_test_fold.append(A_train[i])
                B_test_fold.append(B_train[i])
            clf = svm.SVC(kernel = 'linear', C = c).fit(A_train_fold,B_train_fold)
            score = score + clf.score(A_test_fold, B_test_fold)
        del A_train_fold[:]
        del B_train_fold[:]
        del A_test_fold[:]
        del B_test_fold[:]
        print "Average score for C = ",c,"=",(score/float(n))*100,"%"

    for train, test in skf:
        for i in xrange(len(train)):
            A_train_fold.append(A_train[i])
            B_train_fold.append(B_train[i])
        for i in xrange(len(test)):
            A_test_fold.append(A_train[i])
            B_test_fold.append(B_train[i])
    clf = svm.SVC(kernel = 'linear', C = 10).fit(A_train_fold,B_train_fold)

    score = clf.score(A_test, B_test)
    print "Best parameter: C = 10", "score on test data: ",score*100,"%"

    Xplot = []
    Yplot = []
    Zplot = []

    clf = svm.SVC(kernel = 'linear', C = 10).fit(AB,label)
    Xplot = []
    Yplot = []
    Xplot, Yplot = np.meshgrid(np.arange(0, 4.2, 0.2),np.arange(0, 4.2, 0.2))
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    Z = clf.predict(np.c_[Xplot.ravel(), Yplot.ravel()])
    Z = Z.reshape(Xplot.shape)
    plot0 = plt.scatter(class0_A, class0_B, marker='o', color = 'red')
    plot1 = plt.scatter(class1_A,class1_B, marker = '+', color = 'black')
    plt.legend((plot0, plot1), ('label 0', 'label 1'), scatterpoints = 1)
    plt.xlabel('A')
    plt.ylabel('B')
    plt.title("Linear kernel")
    plt.contourf(Xplot, Yplot, Z, cmap=plt.cm.Paired, alpha=0.8)
    plt.show()


def polynomialSVM():
    print "==================================Polynomial SVM=================================="

    CC = [10**-2, 1, 10**2]
    D = [2, 3, 4, 5, 6]

    for c in CC:
        for d in D:
            score = 0
            #print len(skf)
            #print skf
            for train, test in skf:
                for i in xrange(len(train)):
                    A_train_fold.append(A_train[i])
                    B_train_fold.append(B_train[i])
                for i in xrange(len(test)):
                    A_test_fold.append(A_train[i])
                    B_test_fold.append(B_train[i])
                clf = svm.SVC(kernel = 'poly', C = c, degree = d).fit(A_train_fold,B_train_fold)
                score = score + clf.score(A_test_fold, B_test_fold)
            del A_train_fold[:]
            del B_train_fold[:]
            del A_test_fold[:]
            del B_test_fold[:]
            print "Average score for C = ",c,"& d = ",d," is",(score/float(n))

    for train, test in skf:
        for i in xrange(len(train)):
            A_train_fold.append(A_train[i])
            B_train_fold.append(B_train[i])
        for i in xrange(len(test)):
            A_test_fold.append(A_train[i])
            B_test_fold.append(B_train[i])
    clf = clf = svm.SVC(kernel = 'poly', C = 1, degree = 4).fit(A_train_fold,B_train_fold)

    score = clf.score(A_test, B_test)
    print "Best parameter: C = 1, d=4 ", "score on test data: ",score*100,"%"

    clf = svm.SVC(kernel = 'poly', C = 1, degree = 4).fit(AB,label)
    Xplot = []
    Yplot = []
    Xplot, Yplot = np.meshgrid(np.arange(0, 4.2, 0.2),np.arange(0, 4.2, 0.2))
    plt.title("Polynomial kernel")
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    Z = clf.predict(np.c_[Xplot.ravel(), Yplot.ravel()])
    Z = Z.reshape(Xplot.shape)
    plot0 = plt.scatter(class0_A, class0_B, marker='o', color = 'red')
    plot1 = plt.scatter(class1_A,class1_B, marker = '+', color = 'black')
    plt.legend((plot0, plot1), ('label 0', 'label 1'), scatterpoints = 1)
    plt.xlabel('A')
    plt.ylabel('B')
    plt.contourf(Xplot, Yplot, Z, cmap=plt.cm.Paired, alpha=0.8)
    plt.show()

def rbf():
    print "==================================RBF SVM=================================="
    CC = [10**-2, 1, 100, 1000]
    gamma = [0.001, 0.01, 0.1, 1]
    for c in CC:
        for g in gamma:
            score = 0
            for train, test in skf:
                for i in xrange(len(train)):
                    A_train_fold.append(A_train[i])
                    B_train_fold.append(B_train[i])
                for i in xrange(len(test)):
                    A_test_fold.append(A_train[i])
                    B_test_fold.append(B_train[i])
                clf = svm.SVC(kernel = 'rbf', C = c, gamma = g).fit(A_train_fold,B_train_fold)
                score = score + clf.score(A_test_fold, B_test_fold)
            del A_train_fold[:]
            del B_train_fold[:]
            del A_test_fold[:]
            del B_test_fold[:]
            print "Average score for C = ",c,"& gamma = ",g," is",(score/float(n)*100),"%"


    for train, test in skf:
        for i in xrange(len(train)):
            A_train_fold.append(A_train[i])
            B_train_fold.append(B_train[i])
        for i in xrange(len(test)):
            A_test_fold.append(A_train[i])
            B_test_fold.append(B_train[i])
    clf = svm.SVC(kernel = 'rbf', C = 100, gamma = 1).fit(A_train_fold,B_train_fold)

    score = clf.score(A_test, B_test)
    print "Best parameter: C = 100, gamma=1", "score on test data: ",score*100,"%"

    clf = svm.SVC(kernel = 'rbf', C = 100, gamma = 1).fit(AB,label)
    Xplot = []
    Yplot = []
    Xplot, Yplot = np.meshgrid(np.arange(0, 4.2, 0.2),
                     np.arange(0, 4.2, 0.2))
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    Z = clf.predict(np.c_[Xplot.ravel(), Yplot.ravel()])
    Z = Z.reshape(Xplot.shape)
    plot0 = plt.scatter(class0_A, class0_B, marker='o', color = 'red')
    plot1 = plt.scatter(class1_A,class1_B, marker = '+', color = 'black')
    plt.legend((plot0, plot1), ('label 0', 'label 1'), scatterpoints = 1)
    plt.xlabel('A')
    plt.ylabel('B')
    plt.title("RBF kernel")
    plt.contourf(Xplot, Yplot, Z, cmap=plt.cm.Paired, alpha=0.8)
    plt.show()


def logistic():
    print "==================================Logistic Regression=================================="
    CC = [1, 100, 1000]
    for c in CC:
            score = 0
            for train, test in skf:
                for i in xrange(len(train)):
                    A_train_fold.append(A_train[i])
                    B_train_fold.append(B_train[i])
                for i in xrange(len(test)):
                    A_test_fold.append(A_train[i])
                    B_test_fold.append(B_train[i])
                logreg = LogisticRegression(C=c).fit(A_train_fold,B_train_fold)
                score = score + logreg.score(A_test_fold, B_test_fold)
            del A_train_fold[:]
            del B_train_fold[:]
            del A_test_fold[:]
            del B_test_fold[:]
            print "Average score for C = ",c,"is", (score/float(n)*100),"%"


    for train, test in skf:
        for i in xrange(len(train)):
            A_train_fold.append(A_train[i])
            B_train_fold.append(B_train[i])
        for i in xrange(len(test)):
            A_test_fold.append(A_train[i])
            B_test_fold.append(B_train[i])
    clf = LogisticRegression(C=1).fit(A_train_fold,B_train_fold)

    score = clf.score(A_test, B_test)
    print "Best parameter: C = 1", "score on test data: ",score*100,"%"


    clf = LogisticRegression(C=50).fit(AB,label)
    Xplot = []
    Yplot = []
    Xplot, Yplot = np.meshgrid(np.arange(0, 4.2, 0.2),np.arange(0, 4.2, 0.2))
    Z = clf.predict(np.c_[Xplot.ravel(), Yplot.ravel()])
    Z = Z.reshape(Xplot.shape)

    plot0 = plt.scatter(class0_A, class0_B, marker='o', color = 'red')
    plot1 = plt.scatter(class1_A,class1_B, marker = '+', color = 'black')
    plt.title("Logistic Regression")
    plt.legend((plot0, plot1), ('label 0', 'label 1'), scatterpoints = 1)
    plt.xlabel('A')
    plt.ylabel('B')
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    plt.contourf(Xplot, Yplot, Z, cmap=plt.cm.Paired, alpha=0.8)
    plt.show()


def decisionTree():
    print "=======================================Decision Tree======================================="
    depth = [10**-1, 10**-2, 1, 10, 100, 1000]
    for c in depth:
            score = 0
            for train, test in skf:
                for i in xrange(len(train)):
                    A_train_fold.append(A_train[i])
                    B_train_fold.append(B_train[i])
                for i in xrange(len(test)):
                    A_test_fold.append(A_train[i])
                    B_test_fold.append(B_train[i])
                logreg = DecisionTreeClassifier(max_depth=c).fit(A_train_fold,B_train_fold)
                score = score + logreg.score(A_test_fold, B_test_fold)
            del A_train_fold[:]
            del B_train_fold[:]
            del A_test_fold[:]
            del B_test_fold[:]
            print "Average score for C = ",c,"is", (score/float(n)*100),"%"



#Plotting Logistic Regression for now with the best params
    for train, test in skf:
        for i in xrange(len(train)):
            A_train_fold.append(A_train[i])
            B_train_fold.append(B_train[i])
        for i in xrange(len(test)):
            A_test_fold.append(A_train[i])
            B_test_fold.append(B_train[i])
    clf = DecisionTreeClassifier(max_depth=10).fit(A_train_fold,B_train_fold)

    score = clf.score(A_test, B_test)
    print "Best Paremeter: depth=10, score on test data: ",float(score)*100.0,"%"


    clf = DecisionTreeClassifier(max_depth=10).fit(AB,label)
    Xplot = []
    Yplot = []
    Xplot, Yplot = np.meshgrid(np.arange(0, 4.2, 0.2),np.arange(0, 4.2, 0.2))
    Z = clf.predict(np.c_[Xplot.ravel(), Yplot.ravel()])
    Z = Z.reshape(Xplot.shape)

    plot0 = plt.scatter(class0_A, class0_B, marker='o', color = 'red')
    plot1 = plt.scatter(class1_A,class1_B, marker = '+', color = 'black')
    plt.title("Decision Tree")
    plt.legend((plot0, plot1), ('label 0', 'label 1'), scatterpoints = 1)
    plt.xlabel('A')
    plt.ylabel('B')
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    plt.contourf(Xplot, Yplot, Z, cmap=plt.cm.Paired, alpha=0.8)
    plt.show()


if __name__ == '__main__':
    fileParse()
    n=5
    A_train, A_test, B_train, B_test = train_test_split(AB, label, test_size=0.4, random_state=42)
    skf = StratifiedKFold(B_train, n_folds=5)
    # linearSVMStats()
    # polynomialSVM()
    rbf()
    logistic()
    decisionTree()




