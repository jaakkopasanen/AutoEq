# Mpow Jaws

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.4; 23 -2.5; 25 -2.7; 28 -2.8; 31 -2.9; 34 -3.1; 37 -3.2; 41 -3.4; 45 -3.5; 49 -3.6; 54 -3.9; 60 -4.3; 66 -4.6; 72 -4.8; 79 -5.1; 87 -5.4; 96 -5.9; 106 -6.5; 116 -7.0; 128 -7.6; 141 -8.0; 155 -8.2; 170 -8.2; 187 -8.2; 206 -8.1; 227 -8.0; 249 -7.7; 274 -7.0; 302 -5.9; 332 -4.6; 365 -3.9; 402 -3.7; 442 -3.4; 486 -2.7; 535 -2.0; 588 -1.2; 647 -0.3; 712 0.4; 783 0.8; 861 0.5; 947 0.1; 1042 0.2; 1146 0.0; 1261 0.0; 1387 0.2; 1526 0.5; 1678 1.0; 1846 1.9; 2031 3.0; 2234 4.5; 2457 5.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.7; 4353 3.7; 4788 4.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow Jaws GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow Jaws ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.32 | -2.9 dB |
| Peaking | 139 Hz  | 0.94 | -4.1 dB |
| Peaking | 244 Hz  | 1.05 | -5.1 dB |
| Peaking | 3006 Hz | 1.33 | 6.5 dB  |
| Peaking | 5772 Hz | 3.31 | 5.3 dB  |
| Peaking | 472 Hz  | 3.51 | -1.1 dB |
| Peaking | 754 Hz  | 3.72 | 1.2 dB  |
| Peaking | 1434 Hz | 0.28 | 0.4 dB  |
| Peaking | 1437 Hz | 2.01 | -1.3 dB |
| Peaking | 8401 Hz | 3.22 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Mpow%20Jaws/Mpow%20Jaws.png)