# Koss UR 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.8; 54 4.8; 60 3.6; 66 3.0; 72 3.1; 79 2.9; 87 2.1; 96 1.3; 106 0.6; 116 0.1; 128 -0.2; 141 -0.8; 155 -1.2; 170 -1.2; 187 -1.7; 206 -2.0; 227 -2.1; 249 -2.3; 274 -3.4; 302 -4.2; 332 -5.4; 365 -6.7; 402 -8.0; 442 -9.0; 486 -9.5; 535 -10.1; 588 -9.4; 647 -6.4; 712 -3.5; 783 -1.0; 861 -2.6; 947 -1.5; 1042 1.1; 1146 3.5; 1261 5.2; 1387 6.0; 1526 6.0; 1678 6.0; 1846 3.9; 2031 -0.1; 2234 -1.1; 2457 1.5; 2703 1.5; 2973 5.2; 3270 6.0; 3597 3.7; 3957 -0.0; 4353 0.7; 4788 -1.2; 5267 0.1; 5793 -4.4; 6373 -3.1; 7010 -2.4; 7711 -3.5; 8482 -4.2; 9330 -3.2; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss UR 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.66 | 6.7 dB   |
| Peaking | 488 Hz   | 1.15 | -10.4 dB |
| Peaking | 1397 Hz  | 1.99 | 8.1 dB   |
| Peaking | 3249 Hz  | 5.01 | 7.1 dB   |
| Peaking | 7283 Hz  | 1.37 | -3.8 dB  |
| Peaking | 758 Hz   | 2.29 | -2.7 dB  |
| Peaking | 763 Hz   | 5.22 | 5.3 dB   |
| Peaking | 1737 Hz  | 7.99 | 2.6 dB   |
| Peaking | 2121 Hz  | 8.95 | -4.0 dB  |
| Peaking | 11217 Hz | 4.92 | 1.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20UR%2020/Koss%20UR%2020.png)