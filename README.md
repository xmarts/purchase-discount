# purchase-discount (Xmarts fork)

> Fork interno de Xmarts del módulo OCA `purchase_discount` sobre la rama `14.0`.

## Relación con upstream

| Propiedad | Valor |
|---|---|
| Upstream canónico | [`OCA/purchase-workflow/14.0/purchase_discount`](https://github.com/OCA/purchase-workflow/tree/14.0/purchase_discount) |
| License | AGPL-3 (ver [LICENSE](LICENSE)) |
| Branch convención | `<odoo-version>.0` (este repo está en `14.0`) |
| Estado del fork | maintenance-only · sin features adicionales sobre upstream |
| Soporte Odoo | 14.0 (este branch) |

Este repo se mantiene para que clientes Xmarts con stack Odoo v14 puedan instalar el módulo sin tener que clonar el repo grande de OCA (`OCA/purchase-workflow`, ~80 módulos). El módulo en sí es funcionalmente equivalente al upstream OCA.

## Política de cambios

- **Bug fixes locales:** permitidos siempre que se intente upstream a OCA primero. Si OCA rechaza o demora, se aplica acá con `[FIX]` en el commit y referencia al PR upstream en el cuerpo.
- **Features nuevas:** PROHIBIDAS sin discusión previa con maintainers. Si necesitás un comportamiento distinto, mejor crear módulo nuevo (`xma_purchase_discount_*`) que dependa de éste.
- **Upgrades de versión Odoo:** se considera repo separado por versión. No mergear branches `14.0` → `15.0`.

## Estado actual (2026-05-25)

- ✅ License AGPL-3 declarada (manifest + archivo `LICENSE` desde [PR #1](https://github.com/xmarts/purchase-discount/pull/1))
- ✅ Branch `14.0` se mantiene como default
- ⬜ Tests OCA originales presentes pero sin CI configurado (TBD Wave 3 si se decide mantener fork v14 vs port a v19)
- ⬜ Decisión pendiente: upgrade a Odoo 19 (port + nuevo repo `xmarts/purchase-discount-19` o equivalente) **vs.** archive (cliente Xmarts típico ya migró a v19 con módulo nativo / OCA upstream).

## Maintainers

Ver [CODEOWNERS](CODEOWNERS).

## Cómo usar (deployment)

```bash
# Como submodule en addons path:
git clone https://github.com/xmarts/purchase-discount.git addons/purchase-discount

# Asegurar que addons-path apunta a addons/purchase-discount/
# Instalar desde Apps en Odoo (buscar "Purchase Discount")
```

## Atribución OCA

Este módulo es desarrollado y mantenido upstream por [Tecnativa](https://www.tecnativa.com/) y otros contribuyentes OCA. El fork Xmarts respeta la licencia AGPL-3 y mantiene los créditos originales en `__manifest__.py`. Cualquier cliente o integrador que use este código debe respetar AGPL-3 también.

---

_Última actualización: 2026-05-25 — Wave 3 Sprint 1 (audit Xmarts-Github-Org)._
