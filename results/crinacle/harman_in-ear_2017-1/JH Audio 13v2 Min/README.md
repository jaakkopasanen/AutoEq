# JH Audio 13v2 Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.5; 25 -4.4; 28 -4.4; 31 -4.6; 34 -4.8; 37 -5.0; 41 -5.4; 45 -5.7; 49 -6.0; 54 -6.3; 60 -6.5; 66 -6.8; 72 -7.1; 79 -7.5; 87 -8.0; 96 -8.5; 106 -8.9; 116 -9.1; 128 -9.4; 141 -9.7; 155 -9.9; 170 -10.1; 187 -10.1; 206 -10.1; 227 -10.1; 249 -10.0; 274 -9.9; 302 -9.6; 332 -9.3; 365 -9.0; 402 -8.8; 442 -8.5; 486 -8.1; 535 -7.7; 588 -7.3; 647 -6.9; 712 -6.5; 783 -6.1; 861 -5.9; 947 -5.9; 1042 -6.1; 1146 -5.9; 1261 -5.8; 1387 -5.7; 1526 -5.5; 1678 -5.2; 1846 -5.0; 2031 -4.9; 2234 -4.6; 2457 -4.2; 2703 -2.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.3; 5793 -5.5; 6373 -6.3; 7010 -11.7; 7711 -14.7; 8482 -11.1; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.4; 15026 -23.3; 16529 -32.4; 18182 -36.5; 20000 -29.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio 13v2 Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio 13v2 Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.38 | 2.8 dB   |
| Peaking | 173 Hz   | 0.34 | -4.1 dB  |
| Peaking | 7675 Hz  | 3.2  | -17.1 dB |
| Peaking | 8717 Hz  | 0.37 | 21.3 dB  |
| Peaking | 17884 Hz | 0.43 | -39.8 dB |
| Peaking | 2202 Hz  | 1.07 | -5.4 dB  |
| Peaking | 3356 Hz  | 0.6  | 5.8 dB   |
| Peaking | 6614 Hz  | 0.79 | -3.4 dB  |
| Peaking | 12800 Hz | 3.09 | 6.9 dB   |
| Peaking | 15764 Hz | 2.32 | -6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB   |
| Peaking | 62 Hz    | 1.41 | -0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 16000 Hz | 1.41 | -28.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JH%20Audio%2013v2%20Min/JH%20Audio%2013v2%20Min.png)