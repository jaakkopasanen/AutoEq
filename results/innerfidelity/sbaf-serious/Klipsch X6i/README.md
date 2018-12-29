# Klipsch X6i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.6; 28 1.4; 31 1.3; 34 1.1; 37 0.9; 41 0.8; 45 0.6; 49 0.3; 54 0.1; 60 -0.2; 66 -0.5; 72 -0.8; 79 -1.2; 87 -1.6; 96 -2.1; 106 -2.4; 116 -2.5; 128 -2.9; 141 -3.1; 155 -3.3; 170 -3.3; 187 -3.4; 206 -3.4; 227 -3.2; 249 -3.2; 274 -3.0; 302 -2.8; 332 -2.5; 365 -2.2; 402 -1.9; 442 -1.5; 486 -1.3; 535 -1.1; 588 -0.5; 647 -0.2; 712 0.1; 783 0.4; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.6; 1387 -1.1; 1526 -1.6; 1678 -1.8; 1846 -1.7; 2031 -1.4; 2234 -1.3; 2457 -0.7; 2703 -0.0; 2973 1.6; 3270 3.8; 3597 5.2; 3957 4.9; 4353 2.8; 4788 1.4; 5267 1.2; 5793 1.8; 6373 3.7; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch X6i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X6i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.57 | 2.0 dB  |
| Peaking | 182 Hz  | 0.63 | -3.6 dB |
| Peaking | 1962 Hz | 1.77 | -2.1 dB |
| Peaking | 3673 Hz | 3    | 5.9 dB  |
| Peaking | 6576 Hz | 6.24 | 4.0 dB  |
| Peaking | 369 Hz  | 2.18 | -0.4 dB |
| Peaking | 803 Hz  | 2.17 | 1.1 dB  |
| Peaking | 1500 Hz | 5.17 | -0.6 dB |
| Peaking | 8149 Hz | 4.23 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X6i/Klipsch%20X6i.png)