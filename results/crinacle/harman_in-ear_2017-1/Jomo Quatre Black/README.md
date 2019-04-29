# Jomo Quatre Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.7; 25 -10.6; 28 -10.5; 31 -10.5; 34 -10.4; 37 -10.3; 41 -10.2; 45 -10.1; 49 -10.0; 54 -10.0; 60 -9.9; 66 -10.0; 72 -10.1; 79 -10.2; 87 -10.4; 96 -10.6; 106 -10.8; 116 -10.9; 128 -11.1; 141 -11.2; 155 -11.3; 170 -11.4; 187 -11.4; 206 -11.4; 227 -11.2; 249 -11.1; 274 -10.9; 302 -10.7; 332 -10.3; 365 -9.9; 402 -9.7; 442 -9.4; 486 -8.9; 535 -8.5; 588 -8.0; 647 -7.5; 712 -6.9; 783 -6.3; 861 -5.8; 947 -5.6; 1042 -5.7; 1146 -6.1; 1261 -6.5; 1387 -6.5; 1526 -6.2; 1678 -5.8; 1846 -5.4; 2031 -4.7; 2234 -3.8; 2457 -2.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -3.6; 4788 -6.8; 5267 -5.9; 5793 -1.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.3; 15026 -13.9; 16529 -18.6; 18182 -21.6; 20000 -12.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Quatre Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Quatre Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.12 | -3.7 dB  |
| Peaking | 226 Hz   | 0.66 | -4.1 dB  |
| Peaking | 3108 Hz  | 1.65 | 6.8 dB   |
| Peaking | 6311 Hz  | 5.38 | 5.8 dB   |
| Peaking | 18092 Hz | 1.11 | -16.8 dB |
| Peaking | 903 Hz   | 4.15 | 1.5 dB   |
| Peaking | 3964 Hz  | 7.08 | 1.9 dB   |
| Peaking | 4880 Hz  | 7.28 | -3.3 dB  |
| Peaking | 13044 Hz | 1.85 | 4.4 dB   |
| Peaking | 15408 Hz | 1.65 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -13.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Quatre%20Black/Jomo%20Quatre%20Black.png)