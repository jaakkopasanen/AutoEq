# 64 Audio N8 M15 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.3; 25 -12.3; 28 -12.2; 31 -12.1; 34 -11.9; 37 -11.8; 41 -11.7; 45 -11.5; 49 -11.4; 54 -11.1; 60 -10.9; 66 -10.8; 72 -10.8; 79 -10.7; 87 -10.6; 96 -10.5; 106 -10.4; 116 -10.3; 128 -10.1; 141 -10.0; 155 -9.8; 170 -9.6; 187 -9.3; 206 -9.0; 227 -8.7; 249 -8.4; 274 -8.1; 302 -7.8; 332 -7.4; 365 -7.1; 402 -6.9; 442 -6.8; 486 -6.5; 535 -6.4; 588 -6.2; 647 -6.0; 712 -5.8; 783 -5.5; 861 -5.3; 947 -5.2; 1042 -5.4; 1146 -5.9; 1261 -6.4; 1387 -6.5; 1526 -6.3; 1678 -5.8; 1846 -5.3; 2031 -4.7; 2234 -3.8; 2457 -2.6; 2703 -1.4; 2973 -0.6; 3270 -0.5; 3597 -1.3; 3957 -2.5; 4353 -3.4; 4788 -4.8; 5267 -4.9; 5793 -1.5; 6373 -1.1; 7010 -3.4; 7711 -5.5; 8482 -5.8; 9330 -7.4; 10263 -6.8; 11289 -5.8; 12418 -5.8; 13660 -11.3; 15026 -22.7; 16529 -31.8; 18182 -33.2; 20000 -20.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.4  | -6.1 dB  |
| Peaking | 129 Hz   | 0.46 | -3.4 dB  |
| Peaking | 6296 Hz  | 0.45 | 11.3 dB  |
| Peaking | 12607 Hz | 1.79 | 14.0 dB  |
| Peaking | 17224 Hz | 0.4  | -32.5 dB |
| Peaking | 1562 Hz  | 2.17 | -2.0 dB  |
| Peaking | 3082 Hz  | 2.44 | 3.1 dB   |
| Peaking | 5089 Hz  | 3.03 | -4.3 dB  |
| Peaking | 6038 Hz  | 4.54 | 3.9 dB   |
| Peaking | 18555 Hz | 5.26 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 16000 Hz | 1.41 | -29.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20M15%20sample%201/64%20Audio%20N8%20M15%20sample%201.png)