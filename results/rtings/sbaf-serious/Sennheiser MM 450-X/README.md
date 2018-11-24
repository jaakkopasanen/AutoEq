# Sennheiser MM 450-X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.3; 31 3.9; 34 2.5; 37 1.3; 41 0.3; 45 -0.5; 49 -0.9; 54 -1.4; 60 -1.6; 66 -1.6; 72 -1.9; 79 -2.2; 87 -2.4; 96 -2.7; 106 -3.1; 116 -3.4; 128 -3.6; 141 -3.5; 155 -3.2; 170 -2.9; 187 -2.8; 206 -2.6; 227 -2.4; 249 -2.1; 274 -1.9; 302 -1.5; 332 -0.9; 365 -0.3; 402 0.2; 442 0.6; 486 1.1; 535 1.4; 588 1.4; 647 1.4; 712 1.2; 783 0.5; 861 0.0; 947 -0.0; 1042 0.0; 1146 -0.1; 1261 -0.5; 1387 -1.5; 1526 -2.6; 1678 -3.5; 1846 -4.5; 2031 -4.6; 2234 -5.8; 2457 -4.8; 2703 -2.8; 2973 -0.8; 3270 2.4; 3597 5.8; 3957 6.0; 4353 3.5; 4788 3.8; 5267 5.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 450-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 450-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.9  | 6.9 dB  |
| Peaking | 125 Hz  | 0.8  | -3.7 dB |
| Peaking | 2222 Hz | 1.92 | -6.5 dB |
| Peaking | 3741 Hz | 3.28 | 7.0 dB  |
| Peaking | 5799 Hz | 3.13 | 6.3 dB  |
| Peaking | 53 Hz   | 3.42 | -0.8 dB |
| Peaking | 577 Hz  | 2.16 | 2.0 dB  |
| Peaking | 1380 Hz | 1.53 | 1.0 dB  |
| Peaking | 1550 Hz | 3.23 | -1.8 dB |
| Peaking | 8245 Hz | 4.91 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20MM%20450-X/Sennheiser%20MM%20450-X.png)