# Unique Melody 3X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.8dB
GraphicEQ: 21 -8.6; 23 -8.6; 25 -8.5; 28 -8.4; 31 -8.3; 34 -8.2; 37 -8.1; 41 -7.9; 45 -7.7; 49 -7.6; 54 -7.4; 60 -7.3; 66 -7.2; 72 -7.1; 79 -7.0; 87 -7.0; 96 -6.9; 106 -6.6; 116 -6.4; 128 -6.3; 141 -6.0; 155 -5.8; 170 -5.5; 187 -5.1; 206 -4.8; 227 -4.4; 249 -4.1; 274 -3.7; 302 -3.3; 332 -3.0; 365 -2.6; 402 -2.2; 442 -1.7; 486 -1.5; 535 -1.1; 588 -0.5; 647 -0.2; 712 -0.0; 783 0.3; 861 0.4; 947 0.2; 1042 -0.0; 1146 -0.2; 1261 -0.3; 1387 -0.7; 1526 -0.9; 1678 -1.1; 1846 -0.9; 2031 -0.5; 2234 -0.3; 2457 0.3; 2703 0.9; 2973 2.5; 3270 3.6; 3597 2.1; 3957 -1.8; 4353 -6.1; 4788 -8.7; 5267 -9.4; 5793 -8.4; 6373 -5.7; 7010 -3.2; 7711 -0.4; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody 3X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody 3X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 0.2  | -8.3 dB  |
| Peaking | 171 Hz  | 0.64 | -3.3 dB  |
| Peaking | 1696 Hz | 4.4  | -1.0 dB  |
| Peaking | 3339 Hz | 3.35 | 6.1 dB   |
| Peaking | 5136 Hz | 2.29 | -10.9 dB |
| Peaking | 361 Hz  | 2.34 | -0.5 dB  |
| Peaking | 783 Hz  | 2.27 | 1.0 dB   |
| Peaking | 6267 Hz | 4.83 | -1.6 dB  |
| Peaking | 6765 Hz | 4.74 | -1.1 dB  |
| Peaking | 7931 Hz | 2.16 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Unique%20Melody%203X/Unique%20Melody%203X.png)