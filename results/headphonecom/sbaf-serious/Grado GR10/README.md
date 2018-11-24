# Grado GR10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.5; 25 3.4; 28 3.3; 31 3.3; 34 3.2; 37 3.1; 41 2.8; 45 2.7; 49 2.5; 54 2.3; 60 2.0; 66 1.7; 72 1.3; 79 0.9; 87 0.6; 96 0.3; 106 0.0; 116 -0.2; 128 -0.5; 141 -0.8; 155 -1.0; 170 -1.2; 187 -1.3; 206 -1.4; 227 -1.5; 249 -1.5; 274 -1.5; 302 -1.4; 332 -1.2; 365 -1.1; 402 -1.0; 442 -0.9; 486 -0.8; 535 -0.6; 588 -0.4; 647 -0.4; 712 -0.1; 783 0.6; 861 0.7; 947 0.4; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.2; 1526 -1.7; 1678 -1.9; 1846 -1.7; 2031 -1.5; 2234 -1.3; 2457 -1.2; 2703 -1.1; 2973 0.6; 3270 5.3; 3597 6.0; 3957 5.4; 4353 -0.4; 4788 1.3; 5267 4.1; 5793 5.3; 6373 3.8; 7010 -0.9; 7711 -5.2; 8482 -4.9; 9330 -1.6; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GR10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.27 | 3.5 dB  |
| Peaking | 50 Hz   | 2.09 | 2.0 dB  |
| Peaking | 3607 Hz | 2.76 | 12.4 dB |
| Peaking | 4673 Hz | 0.64 | -7.4 dB |
| Peaking | 5725 Hz | 3.32 | 11.4 dB |
| Peaking | 247 Hz  | 0.89 | -1.6 dB |
| Peaking | 858 Hz  | 3.53 | 1.5 dB  |
| Peaking | 6686 Hz | 7.25 | 3.5 dB  |
| Peaking | 8175 Hz | 2.53 | -6.6 dB |
| Peaking | 9579 Hz | 1.41 | 4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GR10/Grado%20GR10.png)