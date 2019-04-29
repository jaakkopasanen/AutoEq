# Noble Audio K10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.0; 25 -5.3; 28 -5.7; 31 -6.0; 34 -6.3; 37 -6.5; 41 -6.8; 45 -7.0; 49 -7.3; 54 -7.5; 60 -7.8; 66 -8.1; 72 -8.5; 79 -8.8; 87 -9.2; 96 -9.6; 106 -9.9; 116 -10.1; 128 -10.3; 141 -10.5; 155 -10.6; 170 -10.6; 187 -10.5; 206 -10.4; 227 -10.2; 249 -10.0; 274 -9.7; 302 -9.4; 332 -9.0; 365 -8.5; 402 -8.2; 442 -7.8; 486 -7.4; 535 -7.1; 588 -6.6; 647 -6.3; 712 -5.9; 783 -5.5; 861 -5.4; 947 -5.6; 1042 -6.2; 1146 -7.0; 1261 -7.8; 1387 -8.2; 1526 -8.0; 1678 -7.4; 1846 -6.7; 2031 -5.7; 2234 -4.8; 2457 -4.0; 2703 -3.2; 2973 -2.4; 3270 -1.4; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.4; 5793 -2.5; 6373 -6.3; 7010 -6.5; 7711 -8.3; 8482 -9.0; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.1; 15026 -20.6; 16529 -24.4; 18182 -24.3; 20000 -17.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio K10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio K10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.93 | 2.5 dB   |
| Peaking | 161 Hz   | 0.56 | -4.3 dB  |
| Peaking | 7984 Hz  | 2.02 | -10.9 dB |
| Peaking | 8915 Hz  | 0.46 | 14.9 dB  |
| Peaking | 17089 Hz | 0.54 | -24.5 dB |
| Peaking | 1559 Hz  | 2.46 | -3.3 dB  |
| Peaking | 3819 Hz  | 2.09 | 2.2 dB   |
| Peaking | 6404 Hz  | 8.63 | -2.8 dB  |
| Peaking | 12815 Hz | 5.54 | 4.5 dB   |
| Peaking | 14780 Hz | 3.64 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB   |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 16000 Hz | 1.41 | -19.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Noble%20Audio%20K10/Noble%20Audio%20K10.png)