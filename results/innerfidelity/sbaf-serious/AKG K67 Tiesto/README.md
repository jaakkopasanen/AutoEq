# AKG K67 Tiesto

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.3; 25 -0.1; 28 -0.6; 31 -0.9; 34 -1.0; 37 -1.1; 41 -1.1; 45 -0.9; 49 -0.5; 54 -0.3; 60 -0.4; 66 -0.7; 72 -0.9; 79 -1.6; 87 -2.1; 96 -2.4; 106 -2.7; 116 -2.7; 128 -2.5; 141 -1.7; 155 0.1; 170 1.8; 187 4.0; 206 5.2; 227 5.9; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 5.5; 442 4.9; 486 4.1; 535 3.7; 588 3.6; 647 3.0; 712 2.3; 783 1.8; 861 0.9; 947 0.3; 1042 -0.1; 1146 -0.3; 1261 -0.4; 1387 -0.4; 1526 -0.9; 1678 -0.5; 1846 0.7; 2031 2.4; 2234 3.4; 2457 4.6; 2703 5.7; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.7; 4788 5.4; 5267 4.4; 5793 1.9; 6373 3.6; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K67 Tiesto GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K67 Tiesto ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 0.56 | -3.3 dB |
| Peaking | 128 Hz  | 1.36 | -6.3 dB |
| Peaking | 223 Hz  | 0.49 | 9.2 dB  |
| Peaking | 1441 Hz | 1.06 | -3.7 dB |
| Peaking | 3281 Hz | 0.89 | 7.2 dB  |
| Peaking | 35 Hz   | 3.09 | -0.7 dB |
| Peaking | 3378 Hz | 8.07 | -0.4 dB |
| Peaking | 4886 Hz | 4.85 | 2.5 dB  |
| Peaking | 6630 Hz | 1.57 | -3.3 dB |
| Peaking | 6639 Hz | 4.85 | 4.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K67%20Tiesto/AKG%20K67%20Tiesto.png)