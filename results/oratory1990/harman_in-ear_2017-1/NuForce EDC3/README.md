# NuForce EDC3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.1; 25 4.0; 28 3.9; 31 3.7; 34 3.6; 37 3.5; 41 3.3; 45 3.2; 49 3.0; 54 2.7; 60 2.5; 66 2.2; 72 1.9; 79 1.6; 87 1.2; 96 0.8; 106 0.4; 116 0.0; 128 -0.2; 141 -0.5; 155 -0.6; 170 -0.7; 187 -0.8; 206 -0.9; 227 -1.4; 249 -1.9; 274 -2.1; 302 -2.0; 332 -1.7; 365 -1.4; 402 -1.4; 442 -1.3; 486 -1.2; 535 -1.0; 588 -0.6; 647 -0.4; 712 -0.1; 783 0.3; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -1.4; 1526 -0.9; 1678 0.1; 1846 1.2; 2031 2.7; 2234 4.3; 2457 5.8; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -5.7; 16529 -10.8; 18182 -10.1; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce EDC3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce EDC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.48 | 4.3 dB   |
| Peaking | 65 Hz    | 0.86 | 1.9 dB   |
| Peaking | 384 Hz   | 0.1  | -1.7 dB  |
| Peaking | 3799 Hz  | 0.74 | 7.8 dB   |
| Peaking | 17585 Hz | 1.42 | -12.4 dB |
| Peaking | 1475 Hz  | 3.85 | -2.1 dB  |
| Peaking | 2469 Hz  | 4.26 | 2.2 dB   |
| Peaking | 6114 Hz  | 2.68 | 6.0 dB   |
| Peaking | 6673 Hz  | 1.25 | -4.2 dB  |
| Peaking | 13309 Hz | 3.69 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/NuForce%20EDC3/NuForce%20EDC3.png)