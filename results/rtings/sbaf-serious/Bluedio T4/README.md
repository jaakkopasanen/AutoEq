# Bluedio T4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.9; 23 -3.3; 25 -2.8; 28 -1.9; 31 -1.0; 34 -0.2; 37 0.6; 41 1.4; 45 2.1; 49 2.8; 54 3.5; 60 4.2; 66 4.8; 72 5.5; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 6.0; 647 6.0; 712 6.0; 783 3.9; 861 1.8; 947 0.2; 1042 -0.4; 1146 -2.0; 1261 -1.7; 1387 -0.6; 1526 -0.9; 1678 -1.6; 1846 -2.2; 2031 -2.4; 2234 -2.8; 2457 -1.7; 2703 0.0; 2973 1.4; 3270 3.1; 3597 4.6; 3957 3.3; 4353 -0.4; 4788 0.3; 5267 2.4; 5793 2.7; 6373 4.9; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.92 | -5.2 dB |
| Peaking | 125 Hz   | 0.35 | 6.5 dB  |
| Peaking | 536 Hz   | 1.66 | 4.6 dB  |
| Peaking | 6272 Hz  | 3.6  | 4.6 dB  |
| Peaking | 24000 Hz | 2.24 | 2.4 dB  |
| Peaking | 348 Hz   | 1.13 | 3.4 dB  |
| Peaking | 685 Hz   | 0.41 | -3.8 dB |
| Peaking | 715 Hz   | 2.85 | 5.2 dB  |
| Peaking | 2192 Hz  | 4.54 | -2.2 dB |
| Peaking | 3550 Hz  | 4.21 | 5.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bluedio%20T4/Bluedio%20T4.png)