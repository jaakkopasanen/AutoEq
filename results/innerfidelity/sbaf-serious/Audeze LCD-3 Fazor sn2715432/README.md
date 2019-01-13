# Audeze LCD-3 Fazor sn2715432
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.7; 37 5.4; 41 5.1; 45 4.5; 49 3.9; 54 3.3; 60 2.6; 66 2.3; 72 2.1; 79 1.9; 87 1.6; 96 1.2; 106 1.1; 116 0.8; 128 0.6; 141 0.3; 155 0.1; 170 0.0; 187 -0.1; 206 -0.2; 227 -0.2; 249 -0.4; 274 -0.3; 302 -0.3; 332 -0.4; 365 -0.4; 402 -0.5; 442 -0.3; 486 -0.4; 535 -0.3; 588 0.1; 647 -0.1; 712 0.1; 783 0.2; 861 -0.2; 947 -0.2; 1042 0.2; 1146 0.2; 1261 0.0; 1387 -1.0; 1526 -1.7; 1678 -1.7; 1846 -0.8; 2031 -0.7; 2234 0.2; 2457 1.7; 2703 2.4; 2973 3.2; 3270 3.9; 3597 4.8; 3957 5.9; 4353 5.5; 4788 3.7; 5267 2.4; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 Fazor sn2715432 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 Fazor sn2715432 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.59 | 6.3 dB  |
| Peaking | 266 Hz  | 0.81 | -0.6 dB |
| Peaking | 1651 Hz | 3.2  | -2.3 dB |
| Peaking | 3834 Hz | 1.87 | 5.7 dB  |
| Peaking | 6089 Hz | 5    | 5.3 dB  |
| Peaking | 1189 Hz | 7.7  | 0.5 dB  |
| Peaking | 1849 Hz | 6.29 | 0.3 dB  |
| Peaking | 2096 Hz | 7.2  | -1.1 dB |
| Peaking | 2543 Hz | 5.67 | 0.9 dB  |
| Peaking | 8389 Hz | 3.87 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20Fazor%20sn2715432/Audeze%20LCD-3%20Fazor%20sn2715432.png)