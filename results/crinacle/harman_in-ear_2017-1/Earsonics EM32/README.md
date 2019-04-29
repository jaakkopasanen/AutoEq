# Earsonics EM32
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.0; 23 -13.3; 25 -13.5; 28 -13.7; 31 -13.8; 34 -13.8; 37 -13.9; 41 -14.0; 45 -14.1; 49 -14.0; 54 -13.9; 60 -13.9; 66 -14.0; 72 -14.0; 79 -14.0; 87 -14.0; 96 -13.9; 106 -13.6; 116 -13.3; 128 -12.9; 141 -12.3; 155 -11.7; 170 -10.7; 187 -9.8; 206 -8.7; 227 -7.6; 249 -6.6; 274 -5.9; 302 -5.6; 332 -5.6; 365 -5.8; 402 -6.3; 442 -6.8; 486 -7.2; 535 -7.6; 588 -7.9; 647 -8.1; 712 -8.3; 783 -8.3; 861 -8.4; 947 -8.8; 1042 -9.4; 1146 -10.2; 1261 -10.7; 1387 -10.7; 1526 -10.0; 1678 -8.8; 1846 -6.9; 2031 -3.7; 2234 -1.2; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.9; 3597 -2.6; 3957 -1.9; 4353 -2.0; 4788 -3.7; 5267 -0.9; 5793 -0.5; 6373 -1.5; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.2; 15026 -26.8; 16529 -31.4; 18182 -22.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics EM32 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics EM32 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.44 | -7.4 dB  |
| Peaking | 111 Hz   | 1.21 | -4.4 dB  |
| Peaking | 5180 Hz  | 0.75 | 7.7 dB   |
| Peaking | 12409 Hz | 1.93 | 12.2 dB  |
| Peaking | 16099 Hz | 1.08 | -29.9 dB |
| Peaking | 310 Hz   | 2.43 | 2.5 dB   |
| Peaking | 1582 Hz  | 0.94 | -7.7 dB  |
| Peaking | 2317 Hz  | 1.54 | 8.6 dB   |
| Peaking | 4682 Hz  | 7.99 | -3.2 dB  |
| Peaking | 9935 Hz  | 5.79 | 0.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.2 dB  |
| Peaking | 62 Hz    | 1.41 | -5.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB  |
| Peaking | 250 Hz   | 1.41 | 1.4 dB   |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | -4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 16000 Hz | 1.41 | -24.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Earsonics%20EM32/Earsonics%20EM32.png)