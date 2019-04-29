# JH Audio Layla Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -13.0; 25 -13.2; 28 -13.5; 31 -13.6; 34 -13.7; 37 -13.8; 41 -13.9; 45 -14.0; 49 -14.1; 54 -14.2; 60 -14.2; 66 -14.3; 72 -14.4; 79 -14.6; 87 -14.7; 96 -14.8; 106 -14.8; 116 -14.9; 128 -14.8; 141 -14.7; 155 -14.5; 170 -14.3; 187 -14.0; 206 -13.8; 227 -13.3; 249 -12.9; 274 -12.6; 302 -12.1; 332 -11.6; 365 -11.1; 402 -10.7; 442 -10.4; 486 -10.0; 535 -9.6; 588 -9.3; 647 -9.0; 712 -8.6; 783 -8.1; 861 -7.7; 947 -7.6; 1042 -8.1; 1146 -8.9; 1261 -8.9; 1387 -8.0; 1526 -6.4; 1678 -4.4; 1846 -2.4; 2031 -0.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.5; 15026 -16.7; 16529 -23.2; 18182 -28.2; 20000 -27.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Layla Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Layla Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.21 | -6.4 dB  |
| Peaking | 450 Hz   | 0.15 | -3.8 dB  |
| Peaking | 3704 Hz  | 0.43 | 8.7 dB   |
| Peaking | 18858 Hz | 0.71 | -25.1 dB |
| Peaking | 1315 Hz  | 3.74 | -3.1 dB  |
| Peaking | 2062 Hz  | 3.85 | 2.6 dB   |
| Peaking | 8537 Hz  | 3.6  | -4.0 dB  |
| Peaking | 13060 Hz | 1.71 | 6.7 dB   |
| Peaking | 16188 Hz | 1.5  | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -5.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -19.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JH%20Audio%20Layla%20Max/JH%20Audio%20Layla%20Max.png)