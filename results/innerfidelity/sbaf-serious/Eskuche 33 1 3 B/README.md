# Eskuche 33 1 3 B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.5; 34 4.5; 37 3.4; 41 2.2; 45 1.3; 49 0.7; 54 0.2; 60 -0.1; 66 -0.2; 72 -0.4; 79 -0.6; 87 -0.7; 96 -0.9; 106 -0.8; 116 -0.6; 128 -0.7; 141 -1.0; 155 -1.3; 170 -1.4; 187 -1.5; 206 -1.7; 227 -1.8; 249 -2.0; 274 -2.1; 302 -2.1; 332 -1.9; 365 -1.9; 402 -2.0; 442 -2.3; 486 -2.7; 535 -3.0; 588 -2.7; 647 -2.6; 712 -2.5; 783 -2.2; 861 -1.8; 947 -0.5; 1042 0.4; 1146 1.2; 1261 1.5; 1387 2.9; 1526 3.2; 1678 3.7; 1846 4.1; 2031 4.3; 2234 4.5; 2457 4.2; 2703 4.2; 2973 5.1; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 4.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Eskuche 33 1 3 B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Eskuche 33 1 3 B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.53 | 7.0 dB  |
| Peaking | 1414 Hz | 0.16 | -4.0 dB |
| Peaking | 1710 Hz | 0.92 | 6.3 dB  |
| Peaking | 3909 Hz | 1.06 | 7.9 dB  |
| Peaking | 6091 Hz | 3.69 | 4.5 dB  |
| Peaking | 13 Hz   | 1.63 | 1.2 dB  |
| Peaking | 70 Hz   | 1.53 | -0.6 dB |
| Peaking | 369 Hz  | 3.74 | 0.8 dB  |
| Peaking | 733 Hz  | 3.84 | -0.7 dB |
| Peaking | 4788 Hz | 7.09 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Eskuche%2033%201%203%20B/Eskuche%2033%201%203%20B.png)