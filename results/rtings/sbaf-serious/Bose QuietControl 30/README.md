# Bose QuietControl 30

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 21 -3.1; 23 -3.3; 25 -3.4; 28 -3.6; 31 -3.5; 34 -3.5; 37 -3.3; 41 -3.1; 45 -2.9; 49 -2.7; 54 -2.5; 60 -2.4; 66 -2.3; 72 -2.2; 79 -2.2; 87 -2.2; 96 -2.3; 106 -2.4; 116 -2.5; 128 -2.5; 141 -2.5; 155 -2.3; 170 -2.0; 187 -1.8; 206 -1.6; 227 -1.4; 249 -1.1; 274 -0.8; 302 -0.6; 332 -0.5; 365 -0.4; 402 -0.1; 442 0.4; 486 1.2; 535 1.8; 588 2.2; 647 2.4; 712 2.4; 783 2.1; 861 1.3; 947 0.4; 1042 -0.1; 1146 -0.2; 1261 -0.2; 1387 -0.5; 1526 -1.2; 1678 -2.2; 1846 -2.8; 2031 -2.7; 2234 -1.6; 2457 -0.3; 2703 0.5; 2973 1.0; 3270 1.7; 3597 1.9; 3957 0.1; 4353 -3.5; 4788 -2.4; 5267 -0.1; 5793 2.4; 6373 2.8; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietControl 30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietControl 30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.73 | -3.3 dB |
| Peaking | 152 Hz  | 0.49 | -2.4 dB |
| Peaking | 1754 Hz | 0.95 | -8.4 dB |
| Peaking | 1785 Hz | 0.33 | 5.9 dB  |
| Peaking | 4541 Hz | 5.57 | -6.5 dB |
| Peaking | 693 Hz  | 1.71 | 2.8 dB  |
| Peaking | 896 Hz  | 0.93 | -2.3 dB |
| Peaking | 1426 Hz | 3.21 | 1.9 dB  |
| Peaking | 6501 Hz | 3.65 | 3.0 dB  |
| Peaking | 7991 Hz | 1.33 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bose%20QuietControl%2030/Bose%20QuietControl%2030.png)