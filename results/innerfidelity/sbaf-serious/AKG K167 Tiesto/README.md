# AKG K167 Tiesto

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.6; 28 5.2; 31 4.8; 34 4.5; 37 4.4; 41 4.3; 45 4.3; 49 4.4; 54 4.6; 60 5.1; 66 5.8; 72 6.0; 79 5.4; 87 4.8; 96 4.7; 106 4.6; 116 4.5; 128 4.2; 141 4.2; 155 4.4; 170 4.9; 187 3.9; 206 3.8; 227 4.1; 249 4.0; 274 4.1; 302 3.5; 332 3.0; 365 2.6; 402 2.3; 442 2.2; 486 1.8; 535 1.6; 588 1.6; 647 1.4; 712 1.0; 783 0.9; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.8; 1261 -0.8; 1387 -1.4; 1526 -2.3; 1678 -3.2; 1846 -3.2; 2031 -1.6; 2234 0.6; 2457 1.6; 2703 2.5; 2973 3.6; 3270 3.7; 3597 3.3; 3957 3.1; 4353 3.0; 4788 4.6; 5267 6.0; 5793 4.0; 6373 2.7; 7010 2.5; 7711 0.3; 8482 -1.1; 9330 -2.8; 10263 -0.8; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K167 Tiesto GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K167 Tiesto ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.12 | 4.4 dB  |
| Peaking | 72 Hz   | 0.72 | 4.5 dB  |
| Peaking | 243 Hz  | 0.82 | 3.3 dB  |
| Peaking | 4918 Hz | 1.8  | 5.3 dB  |
| Peaking | 15 Hz   | 0.75 | 0.8 dB  |
| Peaking | 1776 Hz | 1.62 | -6.9 dB |
| Peaking | 2640 Hz | 0.7  | 4.4 dB  |
| Peaking | 4327 Hz | 3.7  | -3.7 dB |
| Peaking | 9138 Hz | 3.91 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K167%20Tiesto/AKG%20K167%20Tiesto.png)