# Unique Melody Martian
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.5; 25 -1.6; 28 -1.7; 31 -1.8; 34 -2.0; 37 -2.2; 41 -2.4; 45 -2.7; 49 -2.9; 54 -3.2; 60 -3.6; 66 -4.0; 72 -4.4; 79 -4.8; 87 -5.3; 96 -5.8; 106 -6.3; 116 -6.7; 128 -7.1; 141 -7.4; 155 -7.7; 170 -8.0; 187 -8.1; 206 -8.2; 227 -8.3; 249 -8.4; 274 -8.4; 302 -8.4; 332 -8.3; 365 -8.2; 402 -8.2; 442 -8.1; 486 -8.1; 535 -8.1; 588 -8.0; 647 -8.0; 712 -8.0; 783 -7.9; 861 -8.0; 947 -8.3; 1042 -8.8; 1146 -9.6; 1261 -10.2; 1387 -10.4; 1526 -10.2; 1678 -9.6; 1846 -8.8; 2031 -7.5; 2234 -6.0; 2457 -4.5; 2703 -2.6; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -1.7; 4353 -3.0; 4788 -1.7; 5267 -1.4; 5793 -2.4; 6373 -3.2; 7010 -6.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -10.1; 11289 -8.3; 12418 -6.7; 13660 -15.8; 15026 -30.4; 16529 -30.5; 18182 -16.0; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Martian GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Martian ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.69 | 5.2 dB   |
| Peaking | 1897 Hz  | 0.35 | -22.9 dB |
| Peaking | 2886 Hz  | 0.32 | 25.0 dB  |
| Peaking | 12452 Hz | 4.18 | 9.5 dB   |
| Peaking | 15689 Hz | 1.4  | -32.2 dB |
| Peaking | 197 Hz   | 1.43 | -1.1 dB  |
| Peaking | 793 Hz   | 1.84 | 1.3 dB   |
| Peaking | 5176 Hz  | 0.13 | -0.3 dB  |
| Peaking | 5522 Hz  | 4.74 | 1.8 dB   |
| Peaking | 22050 Hz | 2.33 | -0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB   |
| Peaking | 62 Hz    | 1.41 | 2.2 dB   |
| Peaking | 125 Hz   | 1.41 | -0.8 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 16000 Hz | 1.41 | -25.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Unique%20Melody%20Martian/Unique%20Melody%20Martian.png)