# AKG Q701 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 5.2; 31 4.5; 34 3.8; 37 3.2; 41 2.6; 45 2.0; 49 1.4; 54 0.7; 60 0.0; 66 -0.4; 72 -0.6; 79 -0.4; 87 -1.4; 96 -2.3; 106 -2.7; 116 -2.2; 128 -3.1; 141 -3.6; 155 -3.9; 170 -3.8; 187 -4.1; 206 -4.2; 227 -4.1; 249 -4.1; 274 -4.0; 302 -3.7; 332 -3.4; 365 -3.1; 402 -3.0; 442 -2.6; 486 -2.4; 535 -2.0; 588 -0.8; 647 -1.1; 712 -0.9; 783 -0.7; 861 -0.7; 947 -0.2; 1042 0.2; 1146 0.3; 1261 -0.0; 1387 -1.1; 1526 -2.5; 1678 -3.2; 1846 -4.8; 2031 -5.6; 2234 -4.0; 2457 -2.8; 2703 -1.0; 2973 0.4; 3270 1.5; 3597 2.0; 3957 0.5; 4353 -1.4; 4788 -1.2; 5267 -2.7; 5793 -5.9; 6373 -6.5; 7010 -4.5; 7711 -4.7; 8482 -3.4; 9330 -0.8; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.2; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.89 | 6.2 dB  |
| Peaking | 201 Hz  | 0.58 | -4.5 dB |
| Peaking | 2012 Hz | 2.86 | -5.8 dB |
| Peaking | 3487 Hz | 2.98 | 3.3 dB  |
| Peaking | 6398 Hz | 2.1  | -6.6 dB |
| Peaking | 423 Hz  | 3.57 | -0.6 dB |
| Peaking | 1160 Hz | 2.33 | 1.4 dB  |
| Peaking | 1518 Hz | 4.62 | -1.2 dB |
| Peaking | 8269 Hz | 4.92 | -3.1 dB |
| Peaking | 9076 Hz | 1.78 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20Q701%20Quincy%20Jones/AKG%20Q701%20Quincy%20Jones.png)