# Beyerdynamic T70 250 Ohm sn01111
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.3; 28 4.0; 31 3.7; 34 3.5; 37 3.4; 41 3.1; 45 2.9; 49 2.7; 54 2.5; 60 2.3; 66 2.1; 72 1.9; 79 1.6; 87 1.4; 96 1.2; 106 1.0; 116 0.6; 128 -0.2; 141 -0.9; 155 -1.0; 170 -0.0; 187 -0.8; 206 -0.6; 227 -0.2; 249 0.0; 274 0.1; 302 0.1; 332 -0.2; 365 -0.4; 402 -0.6; 442 0.1; 486 0.2; 535 0.5; 588 0.6; 647 0.4; 712 0.2; 783 0.3; 861 0.1; 947 0.0; 1042 0.1; 1146 -0.0; 1261 -0.1; 1387 -0.4; 1526 -0.5; 1678 -0.3; 1846 0.6; 2031 1.7; 2234 3.4; 2457 4.4; 2703 3.9; 2973 4.1; 3270 4.0; 3597 4.3; 3957 6.0; 4353 4.8; 4788 5.4; 5267 6.0; 5793 6.0; 6373 5.5; 7010 0.5; 7711 -4.7; 8482 -8.0; 9330 -7.9; 10263 -4.5; 11289 -0.1; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70 250 Ohm sn01111 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm sn01111 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.56 | 4.4 dB   |
| Peaking | 2490 Hz  | 3.68 | 3.6 dB   |
| Peaking | 3927 Hz  | 2.05 | 4.5 dB   |
| Peaking | 5977 Hz  | 2.29 | 7.2 dB   |
| Peaking | 8631 Hz  | 2.69 | -10.9 dB |
| Peaking | 150 Hz   | 3.74 | -1.4 dB  |
| Peaking | 393 Hz   | 3.8  | -0.7 dB  |
| Peaking | 554 Hz   | 2.66 | 0.6 dB   |
| Peaking | 1543 Hz  | 3.87 | -1.1 dB  |
| Peaking | 11733 Hz | 6.3  | 1.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm%20sn01111/Beyerdynamic%20T70%20250%20Ohm%20sn01111.png)