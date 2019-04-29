# 64 Audio N8 (dd disabled)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.6; 87 -1.4; 96 -2.5; 106 -3.5; 116 -4.5; 128 -5.3; 141 -6.1; 155 -6.8; 170 -7.5; 187 -8.1; 206 -8.6; 227 -9.0; 249 -9.3; 274 -9.5; 302 -9.7; 332 -9.7; 365 -9.6; 402 -9.6; 442 -9.5; 486 -9.4; 535 -9.1; 588 -8.9; 647 -8.6; 712 -8.3; 783 -7.9; 861 -7.6; 947 -7.6; 1042 -7.9; 1146 -8.7; 1261 -9.4; 1387 -9.9; 1526 -9.9; 1678 -9.7; 1846 -9.3; 2031 -8.5; 2234 -7.3; 2457 -5.9; 2703 -4.5; 2973 -3.3; 3270 -2.5; 3597 -2.4; 3957 -3.4; 4353 -4.4; 4788 -5.1; 5267 -3.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -14.1; 15026 -28.1; 16529 -36.1; 18182 -35.0; 20000 -20.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 (dd disabled) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 (dd disabled) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.46 | 8.0 dB   |
| Peaking | 488 Hz   | 0.16 | -3.8 dB  |
| Peaking | 6052 Hz  | 0.45 | 16.8 dB  |
| Peaking | 12434 Hz | 1.66 | 16.7 dB  |
| Peaking | 16621 Hz | 0.37 | -37.8 dB |
| Peaking | 21 Hz    | 2.74 | 1.8 dB   |
| Peaking | 913 Hz   | 0.83 | 8.1 dB   |
| Peaking | 1492 Hz  | 0.41 | -9.0 dB  |
| Peaking | 3264 Hz  | 0.78 | 7.6 dB   |
| Peaking | 4630 Hz  | 3.63 | -4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB   |
| Peaking | 62 Hz    | 1.41 | 5.9 dB   |
| Peaking | 125 Hz   | 1.41 | 1.1 dB   |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 9.4 dB   |
| Peaking | 16000 Hz | 1.41 | -33.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20(dd%20disabled)/64%20Audio%20N8%20(dd%20disabled).png)