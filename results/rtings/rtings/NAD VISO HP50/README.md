# NAD VISO HP50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 21 0.0; 23 1.0; 25 0.9; 28 0.8; 31 0.8; 34 0.8; 37 0.9; 41 1.1; 45 1.2; 49 1.3; 54 1.3; 60 1.1; 66 0.7; 72 0.2; 79 -0.3; 87 -0.7; 96 -1.2; 106 -1.7; 116 -2.3; 128 -2.8; 141 -3.1; 155 -3.4; 170 -3.7; 187 -3.9; 206 -3.9; 227 -3.7; 249 -3.7; 274 -3.7; 302 -3.4; 332 -3.0; 365 -2.4; 402 -1.8; 442 -1.3; 486 -1.6; 535 -2.0; 588 -2.1; 647 -2.0; 712 -1.5; 783 -0.8; 861 -0.3; 947 -0.1; 1042 0.1; 1146 0.3; 1261 0.2; 1387 -0.3; 1526 -1.1; 1678 -1.9; 1846 -2.2; 2031 -2.0; 2234 -0.3; 2457 1.4; 2703 2.4; 2973 2.9; 3270 3.0; 3597 3.2; 3957 2.9; 4353 2.1; 4788 0.8; 5267 0.8; 5793 1.5; 6373 0.4; 7010 1.8; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD VISO HP50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 57 Hz   | 0.67 | 2.2 dB  |
| Peaking | 179 Hz  | 0.6  | -3.3 dB |
| Peaking | 260 Hz  | 0.38 | -1.1 dB |
| Peaking | 1945 Hz | 2.24 | -5.4 dB |
| Peaking | 2718 Hz | 0.89 | 4.3 dB  |
| Peaking | 439 Hz  | 4.18 | 1.1 dB  |
| Peaking | 619 Hz  | 2.52 | -0.9 dB |
| Peaking | 1030 Hz | 1.81 | 0.8 dB  |
| Peaking | 2349 Hz | 0.12 | -0.2 dB |
| Peaking | 3760 Hz | 7.11 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)