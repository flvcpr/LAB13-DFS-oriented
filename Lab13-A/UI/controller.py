import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        anni = DAO.getYears()
        for a in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(f"{a[0]}, {a[1]}"))
        self._view.update_page()

    def handle_graph(self, e):
        anno = (self._view.ddyear.value).split(",")[0]
        stati = DAO.getStates(anno)
        self._view.ddstato.options.clear()
        for a in stati:
            self._view.ddstato.options.append(ft.dropdown.Option(a.id))
        self._view.update_page()
        self._model.creaGrafo(anno,stati)
        self._view.txt_result.controls.append(ft.Text(self._model.stampa()))
        self._view.update_page()
    def handle_vicini(self,e):
        stato = self._model.idMap[self._view.ddstato.value]
        s,p = self._model.analisi(stato)
        self._view.txt_result.controls.append(ft.Text(f"precedenti: "))
        for pr in p:
            self._view.txt_result.controls.append(ft.Text(pr.id))
        self._view.txt_result.controls.append(ft.Text(f"successivi: "))
        for pr in s:
            self._view.txt_result.controls.append(ft.Text(pr.id))

        visited = self._model.getDFSNodes(stato)
        self._view.txt_result.controls.append(
            ft.Text(f"Da {stato.id} posso raggiungere "
                    f"{len(visited)}")
        )
        for v in visited:
            self._view.txt_result.controls.append(ft.Text(v.id))
        self._view.update_page()

    def handle_path(self, e):
        pass