# -*- coding: utf-8 -*-
"""
TANKEKIT - Code Analyzer Module
Implementa 15 métodos de análisis de código para detectar posibles fallas,
errores y encontrar mejores prácticas
"""

import ast
import re
import os
from pathlib import Path
from collections import defaultdict
import logging


class CodeAnalyzer:
    """Analizador de código con 15 métodos de análisis para detectar problemas"""
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""
        self.tree = None
        self.lines = []
        self.issues = defaultdict(list)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
                self.lines = self.content.split('\n')
            self.tree = ast.parse(self.content)
        except Exception as e:
            logging.error(f"Error al analizar {file_path}: {e}")
    
    # MÉTODO 1: Análisis de imports y dependencias
    def analyze_imports(self):
        """Detecta imports no utilizados, imports redundantes y problemas de organización"""
        if not self.tree:
            return
        
        imported_names = set()
        used_names = set()
        import_lines = []
        
        for node in ast.walk(self.tree):
            # Recolectar imports
            if isinstance(node, ast.Import):
                for alias in node.names:
                    name = alias.asname if alias.asname else alias.name
                    imported_names.add(name)
                    import_lines.append((node.lineno, name))
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    name = alias.asname if alias.asname else alias.name
                    imported_names.add(name)
                    import_lines.append((node.lineno, name))
            # Recolectar nombres usados
            elif isinstance(node, ast.Name):
                used_names.add(node.id)
        
        # Detectar imports no utilizados
        unused = imported_names - used_names
        if unused:
            self.issues['imports'].append({
                'severity': 'warning',
                'message': f'Imports potencialmente no utilizados: {", ".join(unused)}',
                'suggestion': 'Remover imports innecesarios para mejorar rendimiento y legibilidad'
            })
        
        # Verificar organización de imports
        if len(import_lines) > 1:
            if import_lines != sorted(import_lines, key=lambda x: x[1]):
                self.issues['imports'].append({
                    'severity': 'info',
                    'message': 'Los imports no están ordenados alfabéticamente',
                    'suggestion': 'Ordenar imports según PEP8 (stdlib, third-party, local)'
                })
    
    # MÉTODO 2: Detección de código duplicado
    def analyze_code_duplication(self):
        """Detecta bloques de código duplicado que podrían refactorizarse"""
        if not self.tree:
            return
        
        function_bodies = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                body_str = ast.unparse(node.body) if hasattr(ast, 'unparse') else str(node.body)
                function_bodies.append((node.name, body_str, node.lineno))
        
        # Buscar similitudes (simplificado)
        for i, (name1, body1, line1) in enumerate(function_bodies):
            for name2, body2, line2 in function_bodies[i+1:]:
                if len(body1) > 100 and body1 == body2:
                    self.issues['duplication'].append({
                        'severity': 'warning',
                        'message': f'Código duplicado entre funciones {name1} (línea {line1}) y {name2} (línea {line2})',
                        'suggestion': 'Extraer código común a una función auxiliar'
                    })
    
    # MÉTODO 3: Análisis de complejidad ciclomática
    def analyze_complexity(self):
        """Detecta funciones con alta complejidad ciclomática"""
        if not self.tree:
            return
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                complexity = self._calculate_complexity(node)
                if complexity > 10:
                    self.issues['complexity'].append({
                        'severity': 'warning',
                        'message': f'Función "{node.name}" (línea {node.lineno}) tiene complejidad ciclomática de {complexity}',
                        'suggestion': 'Refactorizar en funciones más pequeñas (recomendado < 10)'
                    })
    
    def _calculate_complexity(self, node):
        """Calcula la complejidad ciclomática de un nodo"""
        complexity = 1
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1
        return complexity
    
    # MÉTODO 4: Detección de variables no utilizadas
    def analyze_unused_variables(self):
        """Detecta variables asignadas pero nunca usadas"""
        if not self.tree:
            return
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                assigned = set()
                used = set()
                
                for child in ast.walk(node):
                    if isinstance(child, ast.Assign):
                        for target in child.targets:
                            if isinstance(target, ast.Name):
                                assigned.add(target.id)
                    elif isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load):
                        used.add(child.id)
                
                unused = assigned - used - {'_'}  # Excluir variables desechables
                if unused:
                    self.issues['unused_variables'].append({
                        'severity': 'warning',
                        'message': f'Variables no utilizadas en "{node.name}" (línea {node.lineno}): {", ".join(unused)}',
                        'suggestion': 'Remover variables no utilizadas o usar underscore para variables desechables'
                    })
    
    # MÉTODO 5: Análisis de manejo de excepciones
    def analyze_exception_handling(self):
        """Detecta problemas en el manejo de excepciones"""
        if not self.tree:
            return
        
        for node in ast.walk(self.tree):
            # Detectar except bare (except:)
            if isinstance(node, ast.ExceptHandler) and node.type is None:
                self.issues['exceptions'].append({
                    'severity': 'error',
                    'message': f'Cláusula except genérica (bare except) en línea {node.lineno}',
                    'suggestion': 'Especificar tipo de excepción o usar "except Exception as e"'
                })
            
            # Detectar pass en except
            if isinstance(node, ast.ExceptHandler):
                if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                    self.issues['exceptions'].append({
                        'severity': 'warning',
                        'message': f'Excepción silenciada con pass en línea {node.lineno}',
                        'suggestion': 'Al menos agregar logging o comentario explicativo'
                    })
    
    # MÉTODO 6: Detección de funciones muy largas
    def analyze_function_length(self):
        """Detecta funciones excesivamente largas"""
        if not self.tree:
            return
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                # Calcular líneas de la función
                func_lines = 0
                if hasattr(node, 'end_lineno'):
                    func_lines = node.end_lineno - node.lineno
                else:
                    # Estimación conservadora: ~2 líneas por statement (incluyendo whitespace)
                    func_lines = len(node.body) * 2
                
                if func_lines > 50:
                    self.issues['function_length'].append({
                        'severity': 'warning',
                        'message': f'Función "{node.name}" (línea {node.lineno}) es muy larga (~{func_lines} líneas)',
                        'suggestion': 'Refactorizar en funciones más pequeñas (recomendado < 50 líneas)'
                    })
    
    # MÉTODO 7: Análisis de strings hardcoded
    def analyze_hardcoded_strings(self):
        """Detecta strings hardcoded que deberían estar en configuración"""
        if not self.tree:
            return
        
        sensitive_patterns = [
            (r'(password|pwd|passwd)\s*=\s*["\'][^"\']+["\']', 'contraseña'),
            (r'(api[_-]?key|apikey)\s*=\s*["\'][^"\']+["\']', 'API key'),
            (r'(token|auth)\s*=\s*["\'][^"\']+["\']', 'token'),
            (r'(secret)\s*=\s*["\'][^"\']+["\']', 'secreto'),
        ]
        
        for line_num, line in enumerate(self.lines, 1):
            for pattern, name in sensitive_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    self.issues['hardcoded_strings'].append({
                        'severity': 'critical',
                        'message': f'Posible {name} hardcoded en línea {line_num}',
                        'suggestion': 'Usar variables de entorno o archivo de configuración'
                    })
    
    # MÉTODO 8: Detección de posibles memory leaks
    def analyze_resource_leaks(self):
        """Detecta posibles fugas de recursos (archivos, conexiones, etc.)"""
        if not self.tree:
            return
        
        for node in ast.walk(self.tree):
            # Buscar open() sin context manager
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == 'open':
                    # Esta es una verificación simplificada - detectamos uso de open()
                    # En una verificación más completa, comprobaríamos el contexto AST
                    self.issues['resource_leaks'].append({
                        'severity': 'warning',
                        'message': f'Uso de open() en línea ~{getattr(node, "lineno", "?")}',
                        'suggestion': 'Usar context manager (with open(...)) para asegurar cierre del archivo'
                    })
    
    # MÉTODO 9: Análisis de seguridad
    def analyze_security(self):
        """Detecta posibles vulnerabilidades de seguridad"""
        if not self.tree:
            return
        
        dangerous_functions = {
            'eval': 'Permite ejecución de código arbitrario',
            'exec': 'Permite ejecución de código arbitrario',
            'compile': 'Puede compilar código malicioso',
            '__import__': 'Import dinámico puede ser peligroso'
        }
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id in dangerous_functions:
                    self.issues['security'].append({
                        'severity': 'critical',
                        'message': f'Función peligrosa "{node.func.id}" usada en línea {node.lineno}',
                        'suggestion': f'{dangerous_functions[node.func.id]}. Considerar alternativas más seguras'
                    })
        
        # Buscar SQL queries construidas con concatenación
        for line_num, line in enumerate(self.lines, 1):
            if re.search(r'(SELECT|INSERT|UPDATE|DELETE).*\+.*["\']', line, re.IGNORECASE):
                self.issues['security'].append({
                    'severity': 'critical',
                    'message': f'Posible SQL injection en línea {line_num}',
                    'suggestion': 'Usar consultas parametrizadas o ORM'
                })
    
    # MÉTODO 10: Validación de logging consistente
    def analyze_logging(self):
        """Verifica uso consistente de logging"""
        if not self.tree:
            return
        
        has_logging_import = False
        print_statements = []
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == 'logging':
                        has_logging_import = True
            
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == 'print':
                    print_statements.append(node.lineno)
        
        if print_statements and has_logging_import:
            self.issues['logging'].append({
                'severity': 'info',
                'message': f'Uso de print() encontrado en líneas {print_statements[:5]} (y más)',
                'suggestion': 'Considerar usar logging en lugar de print para mejor control de output'
            })
    
    # MÉTODO 11: Análisis de nomenclatura (PEP8)
    def analyze_naming_conventions(self):
        """Verifica convenciones de nomenclatura PEP8"""
        if not self.tree:
            return
        
        for node in ast.walk(self.tree):
            # Verificar nombres de funciones (snake_case)
            if isinstance(node, ast.FunctionDef):
                if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
                    self.issues['naming'].append({
                        'severity': 'info',
                        'message': f'Función "{node.name}" (línea {node.lineno}) no sigue snake_case',
                        'suggestion': 'Usar snake_case para funciones (ej: mi_funcion)'
                    })
            
            # Verificar nombres de clases (PascalCase)
            if isinstance(node, ast.ClassDef):
                if not re.match(r'^[A-Z][a-zA-Z0-9]*$', node.name):
                    self.issues['naming'].append({
                        'severity': 'info',
                        'message': f'Clase "{node.name}" (línea {node.lineno}) no sigue PascalCase',
                        'suggestion': 'Usar PascalCase para clases (ej: MiClase)'
                    })
    
    # MÉTODO 12: Detección de código muerto
    def analyze_dead_code(self):
        """Detecta código inalcanzable o no utilizado"""
        if not self.tree:
            return
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                # Buscar return seguido de código
                found_return = False
                for i, stmt in enumerate(node.body):
                    if found_return and not isinstance(stmt, (ast.Pass, ast.Expr)):
                        self.issues['dead_code'].append({
                            'severity': 'warning',
                            'message': f'Código inalcanzable después de return en "{node.name}" (línea ~{node.lineno + i})',
                            'suggestion': 'Remover código inalcanzable'
                        })
                    if isinstance(stmt, ast.Return):
                        found_return = True
    
    # MÉTODO 13: Análisis de performance
    def analyze_performance(self):
        """Detecta problemas comunes de rendimiento"""
        if not self.tree:
            return
        
        for node in ast.walk(self.tree):
            # Detectar loops anidados profundos
            if isinstance(node, (ast.For, ast.While)):
                depth = self._get_loop_depth(node)
                if depth > 2:
                    self.issues['performance'].append({
                        'severity': 'warning',
                        'message': f'Loop anidado de profundidad {depth} en línea {node.lineno}',
                        'suggestion': 'Considerar optimización o uso de comprehensions/itertools'
                    })
            
            # Detectar += en loops para strings
            if isinstance(node, ast.AugAssign) and isinstance(node.op, ast.Add):
                if isinstance(node.target, ast.Name):
                    self.issues['performance'].append({
                        'severity': 'info',
                        'message': f'Uso de += en línea {node.lineno}, puede ser ineficiente para strings',
                        'suggestion': 'Para concatenar strings, usar join() o list comprehension'
                    })
    
    def _get_loop_depth(self, node, depth=1):
        """Calcula la profundidad de anidamiento de loops"""
        max_depth = depth
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.For, ast.While)):
                max_depth = max(max_depth, self._get_loop_depth(child, depth + 1))
        return max_depth
    
    # MÉTODO 14: Validación de documentación
    def analyze_documentation(self):
        """Verifica existencia y calidad de docstrings"""
        if not self.tree:
            return
        
        for node in ast.walk(self.tree):
            # Verificar docstrings en funciones
            if isinstance(node, ast.FunctionDef):
                if not node.name.startswith('_'):  # Funciones públicas
                    has_docstring = (ast.get_docstring(node) is not None)
                    if not has_docstring:
                        self.issues['documentation'].append({
                            'severity': 'info',
                            'message': f'Función pública "{node.name}" (línea {node.lineno}) sin docstring',
                            'suggestion': 'Agregar docstring explicando propósito, parámetros y retorno'
                        })
            
            # Verificar docstrings en clases
            if isinstance(node, ast.ClassDef):
                has_docstring = (ast.get_docstring(node) is not None)
                if not has_docstring:
                    self.issues['documentation'].append({
                        'severity': 'info',
                        'message': f'Clase "{node.name}" (línea {node.lineno}) sin docstring',
                        'suggestion': 'Agregar docstring explicando propósito y uso de la clase'
                    })
    
    # MÉTODO 15: Análisis de type hints
    def analyze_type_hints(self):
        """Verifica uso de type hints para mejor mantenibilidad"""
        if not self.tree:
            return
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                # Verificar type hints en parámetros
                params_without_hints = []
                for arg in node.args.args:
                    if arg.annotation is None and arg.arg != 'self' and arg.arg != 'cls':
                        params_without_hints.append(arg.arg)
                
                if params_without_hints:
                    self.issues['type_hints'].append({
                        'severity': 'info',
                        'message': f'Función "{node.name}" (línea {node.lineno}) sin type hints en parámetros: {", ".join(params_without_hints)}',
                        'suggestion': 'Agregar type hints para mejor IDE support y documentación'
                    })
                
                # Verificar return type hint
                if node.returns is None and node.name != '__init__':
                    self.issues['type_hints'].append({
                        'severity': 'info',
                        'message': f'Función "{node.name}" (línea {node.lineno}) sin type hint de retorno',
                        'suggestion': 'Agregar type hint de retorno (-> Type)'
                    })
    
    def run_all_analyses(self):
        """Ejecuta todos los 15 métodos de análisis"""
        if not self.tree:
            return self.issues
        
        print(f"\n{'='*80}")
        print(f"Analizando: {self.file_path}")
        print(f"{'='*80}")
        
        analyses = [
            ("1. Análisis de Imports", self.analyze_imports),
            ("2. Detección de Código Duplicado", self.analyze_code_duplication),
            ("3. Análisis de Complejidad Ciclomática", self.analyze_complexity),
            ("4. Detección de Variables No Utilizadas", self.analyze_unused_variables),
            ("5. Análisis de Manejo de Excepciones", self.analyze_exception_handling),
            ("6. Detección de Funciones Largas", self.analyze_function_length),
            ("7. Análisis de Strings Hardcoded", self.analyze_hardcoded_strings),
            ("8. Detección de Resource Leaks", self.analyze_resource_leaks),
            ("9. Análisis de Seguridad", self.analyze_security),
            ("10. Validación de Logging", self.analyze_logging),
            ("11. Análisis de Nomenclatura", self.analyze_naming_conventions),
            ("12. Detección de Código Muerto", self.analyze_dead_code),
            ("13. Análisis de Performance", self.analyze_performance),
            ("14. Validación de Documentación", self.analyze_documentation),
            ("15. Análisis de Type Hints", self.analyze_type_hints),
        ]
        
        for name, analysis_func in analyses:
            try:
                analysis_func()
                print(f"✓ {name}")
            except Exception as e:
                logging.error(f"Error in {name}: {e}")
                print(f"✗ {name}: {e}")
        
        return self.issues
    
    def print_report(self):
        """Imprime un reporte formateado de los problemas encontrados"""
        if not self.issues:
            print("\n✓ No se encontraron problemas significativos")
            return
        
        severity_order = {'critical': 0, 'error': 1, 'warning': 2, 'info': 3}
        
        print("\n" + "="*80)
        print("REPORTE DE ANÁLISIS DE CÓDIGO")
        print("="*80)
        
        total_issues = sum(len(v) for v in self.issues.values())
        print(f"\nTotal de problemas encontrados: {total_issues}\n")
        
        for category, problems in sorted(self.issues.items()):
            if problems:
                print(f"\n{'─'*80}")
                print(f"Categoría: {category.upper().replace('_', ' ')}")
                print(f"{'─'*80}")
                
                for issue in sorted(problems, key=lambda x: severity_order.get(x['severity'], 99)):
                    severity_symbol = {
                        'critical': '🔴',
                        'error': '🟠',
                        'warning': '🟡',
                        'info': 'ℹ️'
                    }.get(issue['severity'], '•')
                    
                    print(f"\n{severity_symbol} [{issue['severity'].upper()}]")
                    print(f"   Problema: {issue['message']}")
                    print(f"   Sugerencia: {issue['suggestion']}")


def analyze_project(project_path):
    """Analiza todos los archivos Python en el proyecto"""
    python_files = []
    
    for root, dirs, files in os.walk(project_path):
        # Ignorar directorios comunes
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'venv', 'env', '.venv']]
        
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    print(f"\n{'='*80}")
    print(f"ANÁLISIS DE PROYECTO TANKEKIT")
    print(f"{'='*80}")
    print(f"Archivos Python encontrados: {len(python_files)}\n")
    
    all_issues = {}
    
    for py_file in python_files:
        analyzer = CodeAnalyzer(py_file)
        issues = analyzer.run_all_analyses()
        analyzer.print_report()
        
        if issues:
            all_issues[py_file] = issues
    
    # Resumen general
    print("\n" + "="*80)
    print("RESUMEN GENERAL DEL PROYECTO")
    print("="*80)
    
    total_critical = 0
    total_errors = 0
    total_warnings = 0
    total_info = 0
    
    for file_issues in all_issues.values():
        for problems in file_issues.values():
            for issue in problems:
                if issue['severity'] == 'critical':
                    total_critical += 1
                elif issue['severity'] == 'error':
                    total_errors += 1
                elif issue['severity'] == 'warning':
                    total_warnings += 1
                elif issue['severity'] == 'info':
                    total_info += 1
    
    print(f"\n🔴 Críticos: {total_critical}")
    print(f"🟠 Errores: {total_errors}")
    print(f"🟡 Advertencias: {total_warnings}")
    print(f"ℹ️  Informativos: {total_info}")
    print(f"\nTotal de problemas: {total_critical + total_errors + total_warnings + total_info}")
    
    return all_issues


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.path.dirname(os.path.abspath(__file__))
    
    analyze_project(path)
