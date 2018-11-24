# Yuin PK2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 5.9; 170 5.7; 187 5.3; 206 5.2; 227 5.1; 249 4.8; 274 5.0; 302 4.9; 332 4.9; 365 4.6; 402 4.0; 442 2.8; 486 3.6; 535 2.4; 588 2.5; 647 2.2; 712 1.7; 783 1.4; 861 0.8; 947 0.1; 1042 -0.3; 1146 -0.8; 1261 -1.8; 1387 -3.0; 1526 -4.4; 1678 -6.0; 1846 -6.8; 2031 -7.0; 2234 -8.3; 2457 -7.9; 2703 -5.9; 2973 -3.6; 3270 -1.1; 3597 -0.5; 3957 -1.0; 4353 -3.5; 4788 -4.1; 5267 -4.3; 5793 -5.7; 6373 -8.7; 7010 -7.6; 7711 -6.3; 8482 -5.6; 9330 -6.2; 10263 -6.0; 11289 -2.3; 12418 0.0; 13660 -2.0; 15026 -6.1; 16529 -4.6; 18182 -1.0; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin PK2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.11 | 5.9 dB  |
| Peaking | 241 Hz   | 0.39 | 4.1 dB  |
| Peaking | 2045 Hz  | 1.65 | -8.4 dB |
| Peaking | 7244 Hz  | 1.37 | -7.6 dB |
| Peaking | 15702 Hz | 3    | -6.2 dB |
| Peaking | 2550 Hz  | 5.88 | -2.1 dB |
| Peaking | 3525 Hz  | 3.77 | 3.4 dB  |
| Peaking | 8136 Hz  | 2.93 | 5.2 dB  |
| Peaking | 9802 Hz  | 1.08 | -5.6 dB |
| Peaking | 12185 Hz | 2.86 | 5.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yuin%20PK2/Yuin%20PK2.png)