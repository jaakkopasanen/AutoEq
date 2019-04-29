# Final Audio F4100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.3; 37 -2.0; 41 -2.7; 45 -3.3; 49 -3.8; 54 -4.3; 60 -4.9; 66 -5.5; 72 -6.1; 79 -6.7; 87 -7.2; 96 -7.9; 106 -8.5; 116 -9.0; 128 -9.4; 141 -10.0; 155 -10.3; 170 -10.6; 187 -10.7; 206 -10.8; 227 -10.9; 249 -11.0; 274 -10.9; 302 -10.8; 332 -10.7; 365 -10.4; 402 -10.3; 442 -10.0; 486 -9.7; 535 -9.3; 588 -8.9; 647 -8.4; 712 -7.8; 783 -7.3; 861 -6.8; 947 -6.5; 1042 -6.6; 1146 -6.9; 1261 -7.1; 1387 -6.9; 1526 -6.2; 1678 -5.3; 1846 -4.5; 2031 -3.6; 2234 -3.0; 2457 -3.2; 2703 -4.6; 2973 -7.1; 3270 -7.3; 3597 -3.7; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.1; 8482 -9.3; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -15.2; 16529 -20.4; 18182 -22.3; 20000 -21.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio F4100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio F4100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.59 | 6.4 dB   |
| Peaking | 226 Hz   | 0.49 | -4.9 dB  |
| Peaking | 2153 Hz  | 3.6  | 3.4 dB   |
| Peaking | 5173 Hz  | 1.63 | 7.4 dB   |
| Peaking | 18591 Hz | 0.8  | -18.0 dB |
| Peaking | 3138 Hz  | 7.26 | -4.3 dB  |
| Peaking | 8347 Hz  | 4.46 | -4.6 dB  |
| Peaking | 9068 Hz  | 0.22 | 0.9 dB   |
| Peaking | 13556 Hz | 1.7  | 5.8 dB   |
| Peaking | 15871 Hz | 1.8  | -7.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 0.7 dB   |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -14.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20F4100/Final%20Audio%20F4100.png)