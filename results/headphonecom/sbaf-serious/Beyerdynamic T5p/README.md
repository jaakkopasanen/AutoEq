# Beyerdynamic T5p

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.6; 23 -3.6; 25 -3.6; 28 -3.4; 31 -3.2; 34 -2.9; 37 -2.5; 41 -2.2; 45 -2.2; 49 -1.9; 54 -1.1; 60 -0.1; 66 0.8; 72 1.3; 79 0.4; 87 -2.3; 96 -4.0; 106 -3.7; 116 -4.3; 128 -3.9; 141 -3.2; 155 -2.3; 170 -2.7; 187 -2.8; 206 -2.0; 227 -1.5; 249 -1.0; 274 -0.6; 302 -0.3; 332 -0.2; 365 -0.2; 402 -0.3; 442 -0.6; 486 -0.9; 535 -0.9; 588 1.1; 647 2.1; 712 0.7; 783 0.6; 861 1.0; 947 0.8; 1042 -0.8; 1146 -3.8; 1261 -2.6; 1387 -2.9; 1526 -3.3; 1678 -3.3; 1846 -3.2; 2031 -5.1; 2234 -5.3; 2457 -2.0; 2703 0.4; 2973 0.7; 3270 -0.5; 3597 -0.7; 3957 -0.5; 4353 0.7; 4788 2.5; 5267 5.6; 5793 3.4; 6373 0.9; 7010 2.5; 7711 0.3; 8482 -0.6; 9330 -0.7; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T5p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.43 | -3.9 dB |
| Peaking | 126 Hz  | 1.51 | -4.1 dB |
| Peaking | 1451 Hz | 2.49 | -3.2 dB |
| Peaking | 2113 Hz | 4.98 | -5.4 dB |
| Peaking | 5338 Hz | 5.56 | 6.4 dB  |
| Peaking | 71 Hz   | 6.16 | 2.8 dB  |
| Peaking | 632 Hz  | 6.33 | 3.9 dB  |
| Peaking | 778 Hz  | 1.12 | -2.0 dB |
| Peaking | 858 Hz  | 3.26 | 3.4 dB  |
| Peaking | 8908 Hz | 7.86 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T5p/Beyerdynamic%20T5p.png)