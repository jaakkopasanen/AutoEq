# Meelectronics Air-Fi Matrix2 AF62 Wired

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.3dB
GraphicEQ: 21 0.0; 23 5.4; 25 4.3; 28 2.9; 31 1.6; 34 0.5; 37 -0.4; 41 -1.3; 45 -2.0; 49 -2.4; 54 -2.8; 60 -3.0; 66 -3.0; 72 -3.0; 79 -2.9; 87 -2.9; 96 -2.8; 106 -2.7; 116 -2.5; 128 -2.3; 141 -2.4; 155 -2.6; 170 -2.3; 187 -2.4; 206 -2.4; 227 -2.2; 249 -2.0; 274 -2.3; 302 -2.4; 332 -2.4; 365 -2.5; 402 -2.5; 442 -2.2; 486 -2.4; 535 -2.5; 588 -2.3; 647 -2.2; 712 -2.1; 783 -1.2; 861 -0.6; 947 -0.1; 1042 -0.1; 1146 0.0; 1261 -0.1; 1387 -0.2; 1526 0.2; 1678 0.9; 1846 2.2; 2031 2.9; 2234 3.3; 2457 3.5; 2703 4.0; 2973 3.3; 3270 2.8; 3597 3.7; 3957 4.8; 4353 5.5; 4788 6.0; 5267 4.3; 5793 4.1; 6373 4.9; 7010 2.5; 7711 0.1; 8482 -1.1; 9330 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meelectronics Air-Fi Matrix2 AF62 Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-73**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meelectronics Air-Fi Matrix2 AF62 Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.04 | 9.2 dB  |
| Peaking | 51 Hz   | 0.38 | -4.0 dB |
| Peaking | 444 Hz  | 0.69 | -2.3 dB |
| Peaking | 2382 Hz | 1.77 | 3.2 dB  |
| Peaking | 4776 Hz | 1.71 | 5.6 dB  |
| Peaking | 691 Hz  | 2.67 | -1.3 dB |
| Peaking | 893 Hz  | 1.04 | 1.1 dB  |
| Peaking | 1400 Hz | 3.38 | -1.0 dB |
| Peaking | 6585 Hz | 5.93 | 3.9 dB  |
| Peaking | 7749 Hz | 1.98 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Wired/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Wired.png)