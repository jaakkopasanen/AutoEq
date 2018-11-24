# AKG K601

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.3; 28 4.9; 31 4.5; 34 4.1; 37 3.8; 41 3.4; 45 3.2; 49 2.9; 54 2.6; 60 2.2; 66 1.9; 72 3.0; 79 2.6; 87 1.5; 96 1.6; 106 0.9; 116 0.5; 128 0.1; 141 -0.2; 155 -0.5; 170 -0.5; 187 -0.7; 206 -0.8; 227 -0.7; 249 -0.7; 274 -0.7; 302 -0.5; 332 -0.3; 365 -0.2; 402 -0.1; 442 0.0; 486 0.1; 535 0.1; 588 0.3; 647 0.8; 712 0.7; 783 0.8; 861 0.8; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -1.1; 1387 -1.7; 1526 -2.2; 1678 -2.1; 1846 -2.3; 2031 -1.7; 2234 -1.4; 2457 -1.4; 2703 -1.4; 2973 -1.1; 3270 -0.4; 3597 -0.7; 3957 -1.6; 4353 -2.0; 4788 -1.3; 5267 0.3; 5793 -2.0; 6373 -2.4; 7010 0.1; 7711 -0.1; 8482 -0.1; 9330 -0.6; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.69 | 5.9 dB  |
| Peaking | 75 Hz   | 4.27 | 2.1 dB  |
| Peaking | 1597 Hz | 2.89 | -2.1 dB |
| Peaking | 2262 Hz | 2.23 | -1.0 dB |
| Peaking | 4938 Hz | 1.21 | -1.3 dB |
| Peaking | 213 Hz  | 1.41 | -1.0 dB |
| Peaking | 747 Hz  | 2.54 | 1.1 dB  |
| Peaking | 5408 Hz | 7.27 | 3.3 dB  |
| Peaking | 6127 Hz | 3.74 | -4.0 dB |
| Peaking | 6844 Hz | 4.24 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K601/AKG%20K601.png)