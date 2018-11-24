# Soul by Ludacris SL100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.9; 25 0.5; 28 -0.1; 31 -0.6; 34 -1.0; 37 -1.3; 41 -1.8; 45 -2.1; 49 -2.4; 54 -2.7; 60 -2.6; 66 -2.5; 72 -3.2; 79 -4.4; 87 -5.4; 96 -6.2; 106 -6.5; 116 -6.8; 128 -7.1; 141 -7.2; 155 -7.4; 170 -7.7; 187 -7.9; 206 -7.8; 227 -7.5; 249 -7.2; 274 -7.1; 302 -7.2; 332 -7.6; 365 -7.2; 402 -6.9; 442 -6.4; 486 -5.8; 535 -5.1; 588 -3.8; 647 -2.2; 712 -0.5; 783 1.0; 861 1.2; 947 0.6; 1042 -0.7; 1146 -2.2; 1261 -3.5; 1387 -4.1; 1526 -4.1; 1678 -3.3; 1846 -1.6; 2031 0.2; 2234 1.7; 2457 3.8; 2703 4.7; 2973 5.5; 3270 6.0; 3597 6.0; 3957 6.0; 4353 -0.4; 4788 -2.7; 5267 -1.2; 5793 -2.2; 6373 1.4; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul by Ludacris SL100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul by Ludacris SL100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 2.86 | -0.5 dB |
| Peaking | 155 Hz  | 0.64 | -7.6 dB |
| Peaking | 386 Hz  | 1.62 | -4.8 dB |
| Peaking | 1503 Hz | 3.21 | -4.9 dB |
| Peaking | 3120 Hz | 2.26 | 7.0 dB  |
| Peaking | 16 Hz   | 2.12 | 1.9 dB  |
| Peaking | 841 Hz  | 4.8  | 3.2 dB  |
| Peaking | 4028 Hz | 4.78 | 7.9 dB  |
| Peaking | 4487 Hz | 2.62 | -7.0 dB |
| Peaking | 6760 Hz | 9.03 | 3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20by%20Ludacris%20SL100/Soul%20by%20Ludacris%20SL100.png)