# AKG K812
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 -0.8; 23 -1.1; 25 -1.4; 28 -1.7; 31 -1.9; 34 -2.1; 37 -2.3; 41 -2.5; 45 -2.6; 49 -2.8; 54 -2.9; 60 -3.2; 66 -3.5; 72 -3.5; 79 -3.6; 87 -3.9; 96 -4.1; 106 -4.4; 116 -4.7; 128 -4.9; 141 -5.2; 155 -5.3; 170 -5.2; 187 -5.3; 206 -5.3; 227 -5.3; 249 -5.0; 274 -5.0; 302 -4.6; 332 -4.4; 365 -4.0; 402 -3.8; 442 -3.6; 486 -3.3; 535 -2.9; 588 -2.5; 647 -2.0; 712 -1.5; 783 -0.9; 861 -0.6; 947 -0.3; 1042 0.1; 1146 0.9; 1261 1.2; 1387 0.7; 1526 -1.0; 1678 -0.6; 1846 0.5; 2031 0.3; 2234 -0.3; 2457 1.7; 2703 4.9; 2973 -0.3; 3270 -0.6; 3597 -1.6; 3957 -3.1; 4353 2.2; 4788 0.2; 5267 -3.6; 5793 -6.9; 6373 -6.6; 7010 0.0; 7711 0.1; 8482 -2.6; 9330 -6.0; 10263 -5.5; 11289 -0.3; 12418 0.0; 13660 0.0; 15026 -1.4; 16529 -1.1; 18182 0.0; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K812 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 100 Hz   | 0.29 | -2.8 dB  |
| Peaking | 252 Hz   | 0.52 | -3.2 dB  |
| Peaking | 3896 Hz  | 0.54 | 4.9 dB   |
| Peaking | 5798 Hz  | 0.67 | -7.4 dB  |
| Peaking | 19867 Hz | 4.73 | -6.8 dB  |
| Peaking | 3897 Hz  | 4.06 | -5.9 dB  |
| Peaking | 4394 Hz  | 5.62 | 5.6 dB   |
| Peaking | 6068 Hz  | 3.36 | -12.3 dB |
| Peaking | 7032 Hz  | 1.21 | 9.9 dB   |
| Peaking | 9450 Hz  | 3.35 | -8.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K812/AKG%20K812.png)