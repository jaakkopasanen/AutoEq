# PSB M4U 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 21 -1.0; 23 -1.0; 25 -0.9; 28 -0.8; 31 -0.7; 34 -0.5; 37 -0.3; 41 0.0; 45 0.3; 49 0.6; 54 1.0; 60 1.4; 66 1.8; 72 2.2; 79 2.3; 87 1.1; 96 -1.6; 106 -2.7; 116 -2.1; 128 -2.3; 141 -2.8; 155 -2.2; 170 -1.7; 187 -2.7; 206 -2.1; 227 -1.6; 249 -1.1; 274 -0.4; 302 0.9; 332 0.7; 365 0.4; 402 1.9; 442 2.8; 486 1.7; 535 1.9; 588 2.7; 647 2.7; 712 1.7; 783 1.3; 861 0.1; 947 -0.1; 1042 0.0; 1146 -0.1; 1261 -0.4; 1387 -0.9; 1526 -1.3; 1678 -1.6; 1846 -1.6; 2031 -1.4; 2234 -1.4; 2457 -1.3; 2703 -1.5; 2973 -1.9; 3270 -2.2; 3597 -3.3; 3957 -3.7; 4353 -3.9; 4788 -2.1; 5267 -0.4; 5793 2.0; 6373 2.0; 7010 -0.2; 7711 -3.7; 8482 -5.8; 9330 -4.9; 10263 -0.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PSB M4U 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 74 Hz   | 1.46 | 7.0 dB  |
| Peaking | 99 Hz   | 0.67 | -5.4 dB |
| Peaking | 501 Hz  | 1.4  | 3.0 dB  |
| Peaking | 3688 Hz | 2.02 | -3.6 dB |
| Peaking | 8693 Hz | 5.2  | -6.7 dB |
| Peaking | 21 Hz   | 1.71 | -0.9 dB |
| Peaking | 642 Hz  | 7.21 | 1.1 dB  |
| Peaking | 1703 Hz | 1.86 | -1.5 dB |
| Peaking | 6211 Hz | 4.49 | 3.8 dB  |
| Peaking | 7666 Hz | 7.08 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%201/PSB%20M4U%201.png)