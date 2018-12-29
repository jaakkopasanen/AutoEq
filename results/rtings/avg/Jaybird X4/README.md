# Jaybird X4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 21 -1.4; 23 -1.3; 25 -1.3; 28 -1.2; 31 -1.1; 34 -1.0; 37 -1.0; 41 -1.0; 45 -1.0; 49 -0.9; 54 -0.9; 60 -1.1; 66 -1.3; 72 -1.4; 79 -1.5; 87 -1.8; 96 -1.9; 106 -2.2; 116 -3.0; 128 -4.1; 141 -5.0; 155 -5.2; 170 -5.1; 187 -4.9; 206 -4.7; 227 -4.3; 249 -3.9; 274 -3.4; 302 -2.9; 332 -2.4; 365 -1.9; 402 -1.5; 442 -0.9; 486 -0.4; 535 0.1; 588 0.7; 647 1.1; 712 1.5; 783 1.7; 861 1.6; 947 0.7; 1042 -0.6; 1146 -1.7; 1261 -2.2; 1387 -2.6; 1526 -2.9; 1678 -3.2; 1846 -3.6; 2031 -4.3; 2234 -4.7; 2457 -5.1; 2703 -5.0; 2973 -3.7; 3270 -2.1; 3597 -0.9; 3957 -0.2; 4353 -0.2; 4788 -0.0; 5267 -0.7; 5793 -3.1; 6373 -9.6; 7010 -8.4; 7711 -1.6; 8482 0.0; 9330 0.0; 10263 -2.2; 11289 -7.0; 12418 -8.1; 13660 -7.3; 15026 -7.9; 16529 -5.4; 18182 -0.4; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 178 Hz   | 0.84 | -5.2 dB  |
| Peaking | 740 Hz   | 2.23 | 2.8 dB   |
| Peaking | 2165 Hz  | 1.39 | -5.0 dB  |
| Peaking | 6619 Hz  | 7.36 | -10.9 dB |
| Peaking | 13943 Hz | 1.48 | -8.9 dB  |
| Peaking | 23 Hz    | 1.16 | -1.3 dB  |
| Peaking | 2763 Hz  | 5.85 | -1.7 dB  |
| Peaking | 4172 Hz  | 2.85 | 1.6 dB   |
| Peaking | 9302 Hz  | 3.68 | 3.2 dB   |
| Peaking | 11505 Hz | 5.5  | -3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20X4/Jaybird%20X4.png)