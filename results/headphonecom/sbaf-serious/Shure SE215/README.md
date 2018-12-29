# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 -5.5; 23 -5.5; 25 -5.5; 28 -5.6; 31 -5.6; 34 -5.7; 37 -5.7; 41 -5.8; 45 -6.0; 49 -6.1; 54 -6.3; 60 -6.5; 66 -6.7; 72 -6.9; 79 -7.1; 87 -7.3; 96 -7.4; 106 -7.5; 116 -7.5; 128 -7.5; 141 -7.5; 155 -7.5; 170 -7.3; 187 -7.1; 206 -6.8; 227 -6.4; 249 -6.0; 274 -5.5; 302 -4.9; 332 -4.3; 365 -3.7; 402 -3.1; 442 -2.5; 486 -2.0; 535 -1.3; 588 -0.8; 647 -0.2; 712 0.2; 783 0.4; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.4; 1261 -1.0; 1387 -2.5; 1526 -3.5; 1678 -4.4; 1846 -5.1; 2031 -5.5; 2234 -5.6; 2457 -4.4; 2703 -1.9; 2973 1.0; 3270 3.5; 3597 4.4; 3957 2.2; 4353 -2.7; 4788 -7.4; 5267 -2.3; 5793 4.2; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.2; 10263 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.26 | -5.3 dB  |
| Peaking | 134 Hz   | 0.76 | -4.5 dB  |
| Peaking | 263 Hz   | 1.33 | -2.9 dB  |
| Peaking | 1978 Hz  | 2.72 | -6.3 dB  |
| Peaking | 24000 Hz | 2.49 | -3.4 dB  |
| Peaking | 801 Hz   | 3.22 | 1.4 dB   |
| Peaking | 2473 Hz  | 4.39 | -2.9 dB  |
| Peaking | 3579 Hz  | 2.75 | 6.7 dB   |
| Peaking | 4817 Hz  | 4.08 | -10.6 dB |
| Peaking | 6091 Hz  | 4.09 | 7.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE215/Shure%20SE215.png)