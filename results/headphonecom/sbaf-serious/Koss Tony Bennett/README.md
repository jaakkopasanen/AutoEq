# Koss Tony Bennett

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.9; 25 3.3; 28 2.6; 31 2.1; 34 1.6; 37 1.2; 41 0.6; 45 0.2; 49 -0.2; 54 -0.7; 60 -1.1; 66 -1.1; 72 -0.1; 79 2.1; 87 2.2; 96 -0.6; 106 -2.1; 116 -3.0; 128 -3.7; 141 -4.3; 155 -4.7; 170 -4.2; 187 -5.0; 206 -4.9; 227 -4.5; 249 -4.1; 274 -3.0; 302 -1.0; 332 0.6; 365 1.3; 402 0.7; 442 -0.2; 486 -0.4; 535 -0.4; 588 0.2; 647 -0.3; 712 0.1; 783 0.9; 861 1.6; 947 -0.2; 1042 0.5; 1146 1.3; 1261 2.1; 1387 2.4; 1526 2.3; 1678 2.4; 1846 2.7; 2031 3.0; 2234 2.8; 2457 3.1; 2703 3.6; 2973 3.1; 3270 3.1; 3597 4.4; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.1; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Tony Bennett GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Tony Bennett ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.66 | 4.5 dB  |
| Peaking | 84 Hz   | 6.81 | 4.1 dB  |
| Peaking | 170 Hz  | 1.19 | -5.4 dB |
| Peaking | 2032 Hz | 0.7  | 2.5 dB  |
| Peaking | 4940 Hz | 1.67 | 6.1 dB  |
| Peaking | 58 Hz   | 4.24 | -1.1 dB |
| Peaking | 251 Hz  | 4.06 | -1.7 dB |
| Peaking | 352 Hz  | 4.22 | 2.6 dB  |
| Peaking | 6405 Hz | 5.27 | 3.1 dB  |
| Peaking | 8153 Hz | 1.57 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20Tony%20Bennett/Koss%20Tony%20Bennett.png)