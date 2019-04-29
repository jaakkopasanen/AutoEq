# JH Audio 13v2 Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -12.4; 25 -12.5; 28 -12.6; 31 -12.7; 34 -12.7; 37 -12.8; 41 -13.0; 45 -13.1; 49 -13.1; 54 -13.2; 60 -13.4; 66 -13.5; 72 -13.7; 79 -13.8; 87 -14.0; 96 -14.2; 106 -14.4; 116 -14.3; 128 -14.3; 141 -14.3; 155 -14.2; 170 -14.0; 187 -13.8; 206 -13.4; 227 -13.0; 249 -12.6; 274 -12.2; 302 -11.6; 332 -11.0; 365 -10.3; 402 -9.7; 442 -9.2; 486 -8.5; 535 -7.9; 588 -7.3; 647 -6.7; 712 -6.0; 783 -5.4; 861 -5.0; 947 -4.9; 1042 -5.2; 1146 -5.5; 1261 -5.7; 1387 -5.6; 1526 -5.2; 1678 -4.8; 1846 -4.6; 2031 -4.5; 2234 -4.5; 2457 -4.2; 2703 -2.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.5; 6373 -1.9; 7010 -6.3; 7711 -10.7; 8482 -8.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.8; 15026 -19.0; 16529 -27.6; 18182 -32.9; 20000 -28.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio 13v2 Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio 13v2 Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.26 | -5.6 dB  |
| Peaking | 139 Hz   | 0.66 | -4.7 dB  |
| Peaking | 280 Hz   | 1.05 | -2.5 dB  |
| Peaking | 9600 Hz  | 0.24 | 13.2 dB  |
| Peaking | 18161 Hz | 0.43 | -35.2 dB |
| Peaking | 2017 Hz  | 0.94 | -4.9 dB  |
| Peaking | 3317 Hz  | 0.37 | 4.0 dB   |
| Peaking | 7877 Hz  | 3.63 | -9.3 dB  |
| Peaking | 13233 Hz | 2.69 | 6.4 dB   |
| Peaking | 16013 Hz | 2.11 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB  |
| Peaking | 62 Hz    | 1.41 | -5.0 dB  |
| Peaking | 125 Hz   | 1.41 | -6.6 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -23.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JH%20Audio%2013v2%20Max/JH%20Audio%2013v2%20Max.png)