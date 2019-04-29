# Jomo Trinity Brass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.2; 25 -10.4; 28 -10.6; 31 -10.7; 34 -10.8; 37 -10.8; 41 -10.9; 45 -11.0; 49 -11.0; 54 -11.1; 60 -11.2; 66 -11.2; 72 -11.3; 79 -11.4; 87 -11.5; 96 -11.6; 106 -11.7; 116 -11.6; 128 -11.5; 141 -11.4; 155 -11.2; 170 -10.9; 187 -10.6; 206 -10.2; 227 -9.7; 249 -9.2; 274 -8.7; 302 -8.1; 332 -7.4; 365 -6.8; 402 -6.2; 442 -5.7; 486 -5.2; 535 -4.6; 588 -4.1; 647 -3.7; 712 -3.2; 783 -2.8; 861 -2.6; 947 -2.7; 1042 -3.2; 1146 -4.0; 1261 -4.6; 1387 -4.9; 1526 -4.8; 1678 -4.5; 1846 -3.8; 2031 -2.8; 2234 -2.1; 2457 -1.5; 2703 -0.9; 2973 -0.8; 3270 -1.3; 3597 -2.4; 3957 -3.7; 4353 -4.0; 4788 -2.8; 5267 -1.1; 5793 -0.5; 6373 -0.9; 7010 -2.6; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -11.6; 15026 -20.9; 16529 -27.1; 18182 -27.9; 20000 -19.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Trinity Brass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Trinity Brass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.34 | -5.4 dB  |
| Peaking | 132 Hz   | 0.89 | -3.8 dB  |
| Peaking | 245 Hz   | 1.58 | -2.1 dB  |
| Peaking | 10619 Hz | 0.2  | 24.5 dB  |
| Peaking | 17067 Hz | 0.26 | -41.9 dB |
| Peaking | 1504 Hz  | 3.93 | -2.0 dB  |
| Peaking | 2846 Hz  | 2.44 | 3.1 dB   |
| Peaking | 5980 Hz  | 2.78 | 5.0 dB   |
| Peaking | 9417 Hz  | 0.38 | -3.8 dB  |
| Peaking | 12342 Hz | 2.38 | 7.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 16000 Hz | 1.41 | -25.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Trinity%20Brass/Jomo%20Trinity%20Brass.png)