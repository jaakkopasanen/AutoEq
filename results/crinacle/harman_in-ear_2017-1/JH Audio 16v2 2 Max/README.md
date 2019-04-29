# JH Audio 16v2 2 Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.6; 25 -12.7; 28 -12.9; 31 -13.1; 34 -13.2; 37 -13.3; 41 -13.5; 45 -13.7; 49 -13.8; 54 -14.0; 60 -14.3; 66 -14.6; 72 -14.9; 79 -15.2; 87 -15.4; 96 -15.8; 106 -16.2; 116 -16.4; 128 -16.5; 141 -16.7; 155 -16.7; 170 -16.7; 187 -16.6; 206 -16.5; 227 -16.2; 249 -15.9; 274 -15.6; 302 -15.1; 332 -14.6; 365 -14.0; 402 -13.5; 442 -12.9; 486 -12.3; 535 -11.6; 588 -10.9; 647 -10.1; 712 -9.2; 783 -8.2; 861 -7.3; 947 -6.6; 1042 -6.3; 1146 -6.4; 1261 -6.1; 1387 -5.0; 1526 -3.5; 1678 -1.9; 1846 -0.6; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -13.2; 16529 -19.2; 18182 -23.3; 20000 -25.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio 16v2 2 Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio 16v2 2 Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.5  | -3.7 dB  |
| Peaking | 106 Hz   | 0.23 | -4.0 dB  |
| Peaking | 194 Hz   | 0.37 | -6.5 dB  |
| Peaking | 2367 Hz  | 0.88 | 6.7 dB   |
| Peaking | 5237 Hz  | 2.03 | 4.9 dB   |
| Peaking | 912 Hz   | 4.29 | 1.0 dB   |
| Peaking | 1267 Hz  | 5.52 | -1.2 dB  |
| Peaking | 8320 Hz  | 0.51 | 4.0 dB   |
| Peaking | 13409 Hz | 1.46 | 9.6 dB   |
| Peaking | 19019 Hz | 0.24 | -19.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -5.5 dB  |
| Peaking | 125 Hz   | 1.41 | -8.2 dB  |
| Peaking | 250 Hz   | 1.41 | -7.9 dB  |
| Peaking | 500 Hz   | 1.41 | -4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -13.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JH%20Audio%2016v2%202%20Max/JH%20Audio%2016v2%202%20Max.png)