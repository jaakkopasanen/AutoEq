# Shure SE210
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.8; 54 5.3; 60 4.7; 66 4.2; 72 3.7; 79 3.2; 87 2.7; 96 2.3; 106 1.9; 116 1.7; 128 1.1; 141 0.8; 155 0.6; 170 0.3; 187 0.0; 206 -0.0; 227 -0.1; 249 -0.1; 274 -0.1; 302 -0.2; 332 -0.1; 365 0.1; 402 0.2; 442 0.2; 486 0.1; 535 0.3; 588 0.5; 647 0.8; 712 0.7; 783 0.7; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.8; 1387 -1.6; 1526 -2.7; 1678 -3.3; 1846 -3.1; 2031 -2.5; 2234 -1.5; 2457 -0.0; 2703 1.8; 2973 3.6; 3270 5.4; 3597 6.0; 3957 5.0; 4353 3.1; 4788 2.8; 5267 4.3; 5793 5.1; 6373 3.7; 7010 -0.0; 7711 -3.8; 8482 -4.4; 9330 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE210 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.57 | 6.6 dB  |
| Peaking | 1819 Hz | 2.17 | -4.1 dB |
| Peaking | 3480 Hz | 2.39 | 6.3 dB  |
| Peaking | 5885 Hz | 3.19 | 5.2 dB  |
| Peaking | 8010 Hz | 4.54 | -6.2 dB |
| Peaking | 20 Hz   | 0.38 | 1.6 dB  |
| Peaking | 31 Hz   | 1.5  | -2.1 dB |
| Peaking | 207 Hz  | 1.05 | -0.7 dB |
| Peaking | 717 Hz  | 2.07 | 1.0 dB  |
| Peaking | 9533 Hz | 9.83 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE210/Shure%20SE210.png)