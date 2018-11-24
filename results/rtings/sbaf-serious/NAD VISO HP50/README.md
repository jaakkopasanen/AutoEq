# NAD VISO HP50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 0.0; 23 1.3; 25 1.2; 28 1.0; 31 0.8; 34 0.8; 37 0.8; 41 0.8; 45 0.9; 49 1.0; 54 1.0; 60 0.8; 66 0.5; 72 0.2; 79 -0.1; 87 -0.4; 96 -0.7; 106 -1.2; 116 -1.8; 128 -2.3; 141 -2.6; 155 -2.8; 170 -3.1; 187 -3.3; 206 -3.4; 227 -3.2; 249 -3.1; 274 -3.0; 302 -2.6; 332 -2.1; 365 -1.4; 402 -0.8; 442 -0.2; 486 -0.4; 535 -0.8; 588 -1.0; 647 -0.9; 712 -0.6; 783 -0.3; 861 -0.2; 947 -0.1; 1042 0.2; 1146 0.5; 1261 0.4; 1387 -0.3; 1526 -1.4; 1678 -2.3; 1846 -2.2; 2031 -1.6; 2234 0.1; 2457 1.9; 2703 3.0; 2973 4.0; 3270 4.8; 3597 5.4; 3957 4.1; 4353 2.1; 4788 0.6; 5267 1.2; 5793 2.9; 6373 2.9; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD VISO HP50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.31 | 1.4 dB  |
| Peaking | 189 Hz  | 0.74 | -4.0 dB |
| Peaking | 1807 Hz | 2.4  | -4.6 dB |
| Peaking | 2938 Hz | 0.56 | 2.5 dB  |
| Peaking | 3384 Hz | 2.99 | 3.4 dB  |
| Peaking | 443 Hz  | 5.25 | 1.1 dB  |
| Peaking | 628 Hz  | 3.21 | -0.7 dB |
| Peaking | 4911 Hz | 5.49 | -2.6 dB |
| Peaking | 6635 Hz | 2.19 | 4.0 dB  |
| Peaking | 7683 Hz | 1.92 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)