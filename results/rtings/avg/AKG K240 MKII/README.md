# AKG K240 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.7; 49 5.0; 54 4.2; 60 3.1; 66 2.2; 72 1.3; 79 0.5; 87 -0.5; 96 -1.3; 106 -2.2; 116 -2.8; 128 -3.4; 141 -3.9; 155 -4.1; 170 -4.1; 187 -4.0; 206 -3.5; 227 -3.4; 249 -3.3; 274 -3.5; 302 -3.6; 332 -3.6; 365 -3.5; 402 -3.4; 442 -3.3; 486 -2.3; 535 -1.5; 588 -1.8; 647 -1.6; 712 -1.2; 783 -0.9; 861 -0.5; 947 -0.2; 1042 0.2; 1146 0.7; 1261 1.0; 1387 1.5; 1526 2.2; 1678 1.8; 1846 0.9; 2031 -0.3; 2234 -1.1; 2457 -1.4; 2703 -1.7; 2973 -1.0; 3270 0.7; 3597 3.7; 3957 0.2; 4353 0.6; 4788 1.3; 5267 3.3; 5793 3.3; 6373 0.9; 7010 -0.8; 7711 -2.9; 8482 -5.4; 9330 -6.5; 10263 -4.3; 11289 -0.8; 12418 -0.0; 13660 -1.5; 15026 -1.1; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.46 | 7.0 dB  |
| Peaking | 137 Hz  | 0.7  | -5.4 dB |
| Peaking | 382 Hz  | 1.54 | -2.5 dB |
| Peaking | 5560 Hz | 2.95 | 4.2 dB  |
| Peaking | 9050 Hz | 2.69 | -7.1 dB |
| Peaking | 1592 Hz | 1.47 | 5.1 dB  |
| Peaking | 2349 Hz | 0.66 | -3.9 dB |
| Peaking | 3584 Hz | 5.86 | 5.6 dB  |
| Peaking | 3956 Hz | 7.14 | -1.4 dB |
| Peaking | 4999 Hz | 0.95 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K240%20MKII/AKG%20K240%20MKII.png)