# Koss ESP950 sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.1; 96 3.8; 106 3.1; 116 2.7; 128 2.7; 141 2.7; 155 2.7; 170 2.4; 187 2.3; 206 2.2; 227 2.3; 249 2.2; 274 2.3; 302 2.1; 332 2.1; 365 2.2; 402 2.1; 442 2.2; 486 2.0; 535 1.8; 588 1.8; 647 1.6; 712 1.4; 783 1.3; 861 0.8; 947 0.4; 1042 0.1; 1146 -0.2; 1261 -0.9; 1387 -1.3; 1526 -1.5; 1678 -0.9; 1846 1.0; 2031 3.1; 2234 4.6; 2457 5.5; 2703 3.1; 2973 1.7; 3270 2.1; 3597 4.0; 3957 6.0; 4353 6.0; 4788 5.8; 5267 5.6; 5793 5.4; 6373 4.2; 7010 2.5; 7711 0.3; 8482 -0.3; 9330 -0.4; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP950 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.32 | 6.1 dB  |
| Peaking | 74 Hz   | 2.92 | 1.8 dB  |
| Peaking | 383 Hz  | 0.94 | 2.0 dB  |
| Peaking | 2361 Hz | 5.52 | 5.3 dB  |
| Peaking | 4760 Hz | 1.72 | 6.6 dB  |
| Peaking | 1436 Hz | 2.09 | -3.9 dB |
| Peaking | 1524 Hz | 0.89 | 1.6 dB  |
| Peaking | 4888 Hz | 6.72 | -1.4 dB |
| Peaking | 6447 Hz | 2.6  | 2.9 dB  |
| Peaking | 7930 Hz | 1.93 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20ESP950%20sample%201/Koss%20ESP950%20sample%201.png)