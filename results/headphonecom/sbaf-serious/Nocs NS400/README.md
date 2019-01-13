# Nocs NS400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 -12.1; 23 -12.0; 25 -12.0; 28 -11.9; 31 -11.8; 34 -11.7; 37 -11.7; 41 -11.6; 45 -11.5; 49 -11.4; 54 -11.4; 60 -11.3; 66 -11.2; 72 -11.2; 79 -11.1; 87 -10.9; 96 -10.7; 106 -10.5; 116 -10.2; 128 -9.9; 141 -9.6; 155 -9.3; 170 -8.9; 187 -8.4; 206 -7.9; 227 -7.2; 249 -6.6; 274 -6.0; 302 -5.3; 332 -4.6; 365 -3.8; 402 -3.2; 442 -2.6; 486 -2.0; 535 -1.3; 588 -0.7; 647 -0.2; 712 0.2; 783 0.4; 861 0.5; 947 0.3; 1042 -0.1; 1146 -0.4; 1261 -0.9; 1387 -1.5; 1526 -2.1; 1678 -2.6; 1846 -3.0; 2031 -3.8; 2234 -4.5; 2457 -4.7; 2703 -3.9; 2973 -2.0; 3270 0.9; 3597 3.1; 3957 3.1; 4353 1.3; 4788 0.1; 5267 -0.5; 5793 -2.9; 6373 -6.9; 7010 -5.3; 7711 -2.6; 8482 -0.7; 9330 -1.1; 10263 -2.5; 11289 -0.1; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.21 | -11.8 dB |
| Peaking | 170 Hz   | 0.73 | -4.3 dB  |
| Peaking | 2432 Hz  | 1.76 | -5.7 dB  |
| Peaking | 3716 Hz  | 2.65 | 5.4 dB   |
| Peaking | 6580 Hz  | 3.77 | -7.3 dB  |
| Peaking | 86 Hz    | 3.73 | -0.4 dB  |
| Peaking | 327 Hz   | 2.07 | -0.8 dB  |
| Peaking | 791 Hz   | 1.52 | 1.6 dB   |
| Peaking | 1564 Hz  | 3.28 | -1.0 dB  |
| Peaking | 10159 Hz | 9.05 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS400/Nocs%20NS400.png)