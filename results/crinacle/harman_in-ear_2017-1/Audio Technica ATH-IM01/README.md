# Audio Technica ATH-IM01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.9; 25 -7.2; 28 -7.6; 31 -7.8; 34 -8.1; 37 -8.3; 41 -8.5; 45 -8.8; 49 -9.0; 54 -9.3; 60 -9.6; 66 -9.9; 72 -10.2; 79 -10.6; 87 -11.0; 96 -11.4; 106 -11.8; 116 -12.2; 128 -12.5; 141 -12.7; 155 -12.9; 170 -13.0; 187 -13.1; 206 -13.1; 227 -13.0; 249 -12.9; 274 -12.7; 302 -12.4; 332 -12.0; 365 -11.6; 402 -11.2; 442 -10.8; 486 -10.3; 535 -9.7; 588 -9.1; 647 -8.4; 712 -7.6; 783 -6.9; 861 -6.2; 947 -5.7; 1042 -5.6; 1146 -5.7; 1261 -5.7; 1387 -5.2; 1526 -4.3; 1678 -3.3; 1846 -2.2; 2031 -1.2; 2234 -0.5; 2457 -0.5; 2703 -0.6; 2973 -1.6; 3270 -2.0; 3597 -0.9; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.8; 6373 -3.9; 7010 -6.0; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.5; 16529 -15.4; 18182 -10.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-IM01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-IM01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 120 Hz   | 0.5  | -4.3 dB  |
| Peaking | 288 Hz   | 0.68 | -4.2 dB  |
| Peaking | 2375 Hz  | 1.09 | 5.7 dB   |
| Peaking | 4871 Hz  | 1.98 | 5.4 dB   |
| Peaking | 16840 Hz | 2.22 | -10.1 dB |
| Peaking | 908 Hz   | 5.18 | 1.1 dB   |
| Peaking | 5850 Hz  | 6.9  | 2.5 dB   |
| Peaking | 6349 Hz  | 3.58 | 0.6 dB   |
| Peaking | 6817 Hz  | 2.28 | -2.1 dB  |
| Peaking | 13836 Hz | 4.53 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -6.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Audio%20Technica%20ATH-IM01/Audio%20Technica%20ATH-IM01.png)