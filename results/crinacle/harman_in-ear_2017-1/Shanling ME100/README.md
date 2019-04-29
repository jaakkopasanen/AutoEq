# Shanling ME100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -2.0; 31 -2.4; 34 -2.8; 37 -3.1; 41 -3.5; 45 -3.8; 49 -4.0; 54 -4.4; 60 -4.8; 66 -5.2; 72 -5.7; 79 -6.1; 87 -6.6; 96 -7.1; 106 -7.7; 116 -8.2; 128 -8.6; 141 -9.1; 155 -9.5; 170 -9.8; 187 -10.1; 206 -10.3; 227 -10.5; 249 -10.6; 274 -10.8; 302 -10.8; 332 -10.6; 365 -10.4; 402 -10.1; 442 -9.8; 486 -9.2; 535 -8.6; 588 -7.8; 647 -7.0; 712 -6.1; 783 -5.2; 861 -4.3; 947 -4.2; 1042 -4.8; 1146 -5.7; 1261 -6.6; 1387 -7.0; 1526 -6.9; 1678 -6.7; 1846 -6.4; 2031 -5.9; 2234 -5.3; 2457 -4.4; 2703 -3.3; 2973 -2.2; 3270 -1.5; 3597 -1.8; 3957 -3.2; 4353 -6.0; 4788 -8.7; 5267 -6.1; 5793 -1.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.2; 15026 -16.6; 16529 -23.9; 18182 -23.8; 20000 -14.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shanling ME100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shanling ME100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.43 | 6.4 dB   |
| Peaking | 242 Hz   | 0.77 | -4.7 dB  |
| Peaking | 3202 Hz  | 2.79 | 4.8 dB   |
| Peaking | 12549 Hz | 0.43 | 13.2 dB  |
| Peaking | 17023 Hz | 0.56 | -27.8 dB |
| Peaking | 895 Hz   | 3.71 | 3.2 dB   |
| Peaking | 4893 Hz  | 5.39 | -6.2 dB  |
| Peaking | 6115 Hz  | 2.42 | 7.5 dB   |
| Peaking | 7781 Hz  | 1.4  | -3.6 dB  |
| Peaking | 13278 Hz | 5.76 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB   |
| Peaking | 62 Hz    | 1.41 | 1.1 dB   |
| Peaking | 125 Hz   | 1.41 | -1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -17.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shanling%20ME100/Shanling%20ME100.png)