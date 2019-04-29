# 64 Audio N8 M15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.6; 25 -10.7; 28 -10.8; 31 -10.9; 34 -10.9; 37 -10.8; 41 -10.8; 45 -10.8; 49 -10.7; 54 -10.7; 60 -10.6; 66 -10.5; 72 -10.6; 79 -10.6; 87 -10.7; 96 -10.6; 106 -10.5; 116 -10.6; 128 -10.4; 141 -10.3; 155 -10.1; 170 -9.9; 187 -9.7; 206 -9.4; 227 -9.2; 249 -8.9; 274 -8.6; 302 -8.3; 332 -7.9; 365 -7.6; 402 -7.4; 442 -7.2; 486 -7.0; 535 -6.8; 588 -6.6; 647 -6.4; 712 -6.1; 783 -5.7; 861 -5.5; 947 -5.4; 1042 -5.7; 1146 -6.2; 1261 -6.7; 1387 -6.8; 1526 -6.5; 1678 -5.9; 1846 -5.3; 2031 -4.5; 2234 -3.5; 2457 -2.4; 2703 -1.3; 2973 -0.6; 3270 -0.5; 3597 -1.2; 3957 -2.4; 4353 -3.3; 4788 -4.8; 5267 -4.2; 5793 -1.2; 6373 -1.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -6.4; 10263 -6.4; 11289 -5.9; 12418 -5.9; 13660 -10.4; 15026 -18.7; 16529 -27.8; 18182 -32.8; 20000 -20.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 49 Hz    | 0.15 | -4.9 dB  |
| Peaking | 1526 Hz  | 1.42 | -4.5 dB  |
| Peaking | 5808 Hz  | 0.26 | 9.5 dB   |
| Peaking | 12641 Hz | 1.56 | 10.4 dB  |
| Peaking | 17735 Hz | 0.41 | -31.0 dB |
| Peaking | 2112 Hz  | 4.87 | -0.8 dB  |
| Peaking | 3098 Hz  | 3.28 | 1.5 dB   |
| Peaking | 5002 Hz  | 2.9  | -4.8 dB  |
| Peaking | 6005 Hz  | 2.74 | 4.7 dB   |
| Peaking | 7717 Hz  | 3.36 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 16000 Hz | 1.41 | -24.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20M15/64%20Audio%20N8%20M15.png)