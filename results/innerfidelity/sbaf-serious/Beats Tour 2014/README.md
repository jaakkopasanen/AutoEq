# Beats Tour 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.5; 28 -6.8; 31 -7.1; 34 -7.3; 37 -7.5; 41 -7.7; 45 -7.9; 49 -8.1; 54 -8.3; 60 -8.5; 66 -8.7; 72 -8.9; 79 -9.1; 87 -9.3; 96 -9.5; 106 -9.5; 116 -9.4; 128 -9.4; 141 -9.3; 155 -9.1; 170 -8.8; 187 -8.4; 206 -8.1; 227 -7.5; 249 -7.1; 274 -6.5; 302 -5.9; 332 -5.3; 365 -4.7; 402 -4.0; 442 -3.3; 486 -2.8; 535 -2.2; 588 -1.3; 647 -0.8; 712 -0.4; 783 0.1; 861 0.1; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.3; 1387 -0.7; 1526 -1.1; 1678 -1.2; 1846 -0.9; 2031 -0.3; 2234 0.3; 2457 1.6; 2703 2.6; 2973 4.3; 3270 5.7; 3597 6.0; 3957 5.4; 4353 2.9; 4788 1.5; 5267 1.7; 5793 2.4; 6373 4.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Tour 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Tour 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 69 Hz    | 0.39 | -7.3 dB |
| Peaking | 198 Hz   | 0.65 | -4.8 dB |
| Peaking | 3573 Hz  | 2.1  | 6.3 dB  |
| Peaking | 23028 Hz | 2.35 | 1.5 dB  |
| Peaking | 23 Hz    | 0.92 | -2.6 dB |
| Peaking | 802 Hz   | 2.39 | 1.3 dB  |
| Peaking | 1712 Hz  | 2.9  | -1.6 dB |
| Peaking | 6537 Hz  | 4.26 | 5.5 dB  |
| Peaking | 6603 Hz  | 1.57 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Tour%202014/Beats%20Tour%202014.png)