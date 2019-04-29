# Final Audio F7200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.2; 31 -1.9; 34 -2.5; 37 -3.0; 41 -3.6; 45 -4.1; 49 -4.5; 54 -5.0; 60 -5.6; 66 -6.1; 72 -6.6; 79 -7.2; 87 -7.7; 96 -8.4; 106 -8.9; 116 -9.4; 128 -9.8; 141 -10.2; 155 -10.6; 170 -10.9; 187 -11.0; 206 -11.1; 227 -11.2; 249 -11.2; 274 -11.2; 302 -11.1; 332 -10.9; 365 -10.6; 402 -10.4; 442 -10.2; 486 -9.9; 535 -9.5; 588 -9.0; 647 -8.6; 712 -8.0; 783 -7.4; 861 -6.8; 947 -6.5; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -6.9; 1526 -6.2; 1678 -5.3; 1846 -4.5; 2031 -3.6; 2234 -3.0; 2457 -3.1; 2703 -4.5; 2973 -7.1; 3270 -7.4; 3597 -3.7; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.7; 8482 -8.7; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -14.7; 16529 -19.8; 18182 -21.8; 20000 -24.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio F7200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio F7200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.53 | 6.3 dB   |
| Peaking | 226 Hz   | 0.49 | -5.1 dB  |
| Peaking | 2154 Hz  | 3.62 | 3.4 dB   |
| Peaking | 5204 Hz  | 1.57 | 7.4 dB   |
| Peaking | 19016 Hz | 0.72 | -18.4 dB |
| Peaking | 3145 Hz  | 7.39 | -4.5 dB  |
| Peaking | 8248 Hz  | 4.51 | -4.0 dB  |
| Peaking | 9945 Hz  | 0.18 | 0.9 dB   |
| Peaking | 13599 Hz | 1.73 | 6.2 dB   |
| Peaking | 15833 Hz | 1.64 | -7.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB   |
| Peaking | 62 Hz    | 1.41 | 0.2 dB   |
| Peaking | 125 Hz   | 1.41 | -2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -14.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20F7200/Final%20Audio%20F7200.png)