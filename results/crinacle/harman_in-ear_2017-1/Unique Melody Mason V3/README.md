# Unique Melody Mason V3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.2; 25 -7.5; 28 -7.8; 31 -8.0; 34 -8.2; 37 -8.4; 41 -8.5; 45 -8.6; 49 -8.7; 54 -8.8; 60 -8.9; 66 -9.0; 72 -9.1; 79 -9.2; 87 -9.4; 96 -9.5; 106 -9.6; 116 -9.5; 128 -9.5; 141 -9.5; 155 -9.4; 170 -9.3; 187 -9.1; 206 -8.8; 227 -8.6; 249 -8.4; 274 -8.1; 302 -7.8; 332 -7.5; 365 -7.3; 402 -7.1; 442 -7.0; 486 -6.8; 535 -6.7; 588 -6.6; 647 -6.6; 712 -6.5; 783 -6.5; 861 -6.5; 947 -6.8; 1042 -7.3; 1146 -8.0; 1261 -8.6; 1387 -8.8; 1526 -8.7; 1678 -8.1; 1846 -7.4; 2031 -6.5; 2234 -5.3; 2457 -3.8; 2703 -2.2; 2973 -0.8; 3270 -0.8; 3597 -0.6; 3957 -0.5; 4353 -0.6; 4788 -3.9; 5267 -8.8; 5793 -10.4; 6373 -6.6; 7010 -5.9; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.8; 15026 -22.6; 16529 -27.2; 18182 -26.0; 20000 -22.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Mason V3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Mason V3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 1.82 | -0.3 dB  |
| Peaking | 112 Hz   | 0.36 | -2.9 dB  |
| Peaking | 5751 Hz  | 4.82 | -8.8 dB  |
| Peaking | 9648 Hz  | 0.33 | 12.3 dB  |
| Peaking | 17158 Hz | 0.5  | -28.6 dB |
| Peaking | 1577 Hz  | 1.65 | -4.1 dB  |
| Peaking | 3442 Hz  | 1.6  | 3.9 dB   |
| Peaking | 8216 Hz  | 1.76 | -2.8 dB  |
| Peaking | 12820 Hz | 2.75 | 6.1 dB   |
| Peaking | 15031 Hz | 3.29 | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -22.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Unique%20Melody%20Mason%20V3/Unique%20Melody%20Mason%20V3.png)