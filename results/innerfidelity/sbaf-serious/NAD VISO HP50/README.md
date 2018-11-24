# NAD VISO HP50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 -3.2; 23 -3.2; 25 -3.3; 28 -3.3; 31 -3.3; 34 -3.3; 37 -3.3; 41 -3.2; 45 -3.0; 49 -2.9; 54 -2.8; 60 -2.6; 66 -2.5; 72 -2.4; 79 -2.3; 87 -2.2; 96 -2.2; 106 -2.7; 116 -2.6; 128 -2.5; 141 -3.7; 155 -4.4; 170 -2.6; 187 -4.4; 206 -4.3; 227 -3.7; 249 -3.1; 274 -2.3; 302 -1.4; 332 -1.0; 365 -0.7; 402 -0.3; 442 0.0; 486 -0.1; 535 -0.0; 588 0.3; 647 0.2; 712 -0.0; 783 -0.1; 861 -0.2; 947 -0.0; 1042 -0.2; 1146 -0.5; 1261 -1.6; 1387 -2.3; 1526 -2.7; 1678 -2.8; 1846 -2.0; 2031 -1.3; 2234 -0.3; 2457 1.1; 2703 2.0; 2973 2.3; 3270 2.2; 3597 1.4; 3957 0.7; 4353 0.3; 4788 -1.3; 5267 2.3; 5793 4.9; 6373 5.0; 7010 2.6; 7711 -0.4; 8482 -1.5; 9330 -1.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD VISO HP50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.31 | -3.2 dB |
| Peaking | 193 Hz  | 1.28 | -3.8 dB |
| Peaking | 1541 Hz | 2.76 | 0.6 dB  |
| Peaking | 1607 Hz | 1.49 | -6.1 dB |
| Peaking | 2291 Hz | 0.41 | 3.0 dB  |
| Peaking | 2163 Hz | 5.22 | -0.6 dB |
| Peaking | 2825 Hz | 3.72 | 1.0 dB  |
| Peaking | 4804 Hz | 3.06 | -5.3 dB |
| Peaking | 6018 Hz | 2.18 | 6.7 dB  |
| Peaking | 8205 Hz | 2.39 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)