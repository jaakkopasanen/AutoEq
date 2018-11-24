# AKG K701 sample B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.5; 34 5.0; 37 4.5; 41 4.0; 45 3.6; 49 3.1; 54 2.7; 60 2.6; 66 3.2; 72 3.0; 79 1.5; 87 1.5; 96 0.3; 106 -0.3; 116 -0.6; 128 -1.0; 141 -1.3; 155 -1.5; 170 -1.6; 187 -1.7; 206 -1.9; 227 -1.7; 249 -1.7; 274 -1.7; 302 -1.5; 332 -1.1; 365 -1.0; 402 -0.8; 442 -0.2; 486 0.1; 535 0.3; 588 0.8; 647 1.2; 712 1.9; 783 2.3; 861 1.3; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -0.6; 1387 -0.8; 1526 -1.0; 1678 -1.7; 1846 -2.5; 2031 -3.2; 2234 -3.0; 2457 -2.7; 2703 -2.3; 2973 -1.0; 3270 0.7; 3597 0.3; 3957 -0.3; 4353 -1.9; 4788 -2.0; 5267 -1.1; 5793 -2.9; 6373 -4.8; 7010 -3.6; 7711 -3.8; 8482 -4.5; 9330 -3.2; 10263 -0.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.5; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 1.12 | 6.5 dB  |
| Peaking | 67 Hz    | 4.56 | 2.5 dB  |
| Peaking | 758 Hz   | 4.33 | 2.6 dB  |
| Peaking | 2097 Hz  | 2.38 | -3.3 dB |
| Peaking | 7358 Hz  | 1.64 | -4.5 dB |
| Peaking | 205 Hz   | 1.07 | -2.1 dB |
| Peaking | 2726 Hz  | 4.83 | -1.2 dB |
| Peaking | 3396 Hz  | 3.86 | 2.1 dB  |
| Peaking | 4481 Hz  | 7.92 | -1.3 dB |
| Peaking | 11408 Hz | 5.13 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K701%20sample%20B/AKG%20K701%20sample%20B.png)