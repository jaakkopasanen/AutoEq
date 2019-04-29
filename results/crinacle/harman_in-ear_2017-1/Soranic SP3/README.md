# Soranic SP3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.4; 25 -5.6; 28 -5.8; 31 -6.0; 34 -6.1; 37 -6.2; 41 -6.3; 45 -6.5; 49 -6.6; 54 -6.7; 60 -6.9; 66 -7.2; 72 -7.4; 79 -7.7; 87 -8.0; 96 -8.3; 106 -8.6; 116 -8.8; 128 -9.1; 141 -9.3; 155 -9.4; 170 -9.5; 187 -9.6; 206 -9.6; 227 -9.6; 249 -9.6; 274 -9.5; 302 -9.3; 332 -9.0; 365 -8.7; 402 -8.4; 442 -8.1; 486 -7.8; 535 -7.4; 588 -7.1; 647 -6.7; 712 -6.3; 783 -5.9; 861 -5.7; 947 -5.7; 1042 -6.2; 1146 -7.0; 1261 -7.7; 1387 -8.2; 1526 -8.4; 1678 -8.3; 1846 -7.7; 2031 -6.4; 2234 -5.0; 2457 -3.1; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -3.2; 5267 -5.7; 5793 -7.0; 6373 -8.2; 7010 -8.8; 7711 -8.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.3; 13660 -22.2; 15026 -34.2; 16529 -30.1; 18182 -14.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soranic SP3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soranic SP3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 215 Hz   | 0.59 | -3.4 dB  |
| Peaking | 1683 Hz  | 1.49 | -7.1 dB  |
| Peaking | 6159 Hz  | 0.33 | 13.7 dB  |
| Peaking | 6326 Hz  | 1.57 | -11.9 dB |
| Peaking | 15431 Hz | 1.71 | -36.5 dB |
| Peaking | 18 Hz    | 0.97 | 1.6 dB   |
| Peaking | 7567 Hz  | 7.24 | -2.1 dB  |
| Peaking | 12375 Hz | 2.77 | 10.7 dB  |
| Peaking | 14069 Hz | 2.23 | -10.0 dB |
| Peaking | 22050 Hz | 2.57 | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | -0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -26.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Soranic%20SP3/Soranic%20SP3.png)