# Earsonics ES2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.7; 41 -2.5; 45 -3.2; 49 -3.7; 54 -4.3; 60 -5.1; 66 -5.8; 72 -6.6; 79 -7.4; 87 -8.0; 96 -8.8; 106 -9.6; 116 -10.2; 128 -10.7; 141 -11.3; 155 -11.8; 170 -12.1; 187 -12.2; 206 -12.4; 227 -12.4; 249 -12.6; 274 -12.7; 302 -12.4; 332 -12.2; 365 -11.8; 402 -11.7; 442 -11.3; 486 -11.0; 535 -10.6; 588 -10.1; 647 -9.8; 712 -9.3; 783 -8.8; 861 -8.4; 947 -8.3; 1042 -8.6; 1146 -9.2; 1261 -9.8; 1387 -10.0; 1526 -10.1; 1678 -10.0; 1846 -9.7; 2031 -8.3; 2234 -5.4; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -14.2; 15026 -21.0; 16529 -19.6; 18182 -9.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics ES2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics ES2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.43 | 6.8 dB   |
| Peaking | 226 Hz   | 0.35 | -6.7 dB  |
| Peaking | 1772 Hz  | 1.07 | -12.7 dB |
| Peaking | 2639 Hz  | 0.52 | 12.3 dB  |
| Peaking | 15647 Hz | 1.81 | -17.2 dB |
| Peaking | 3689 Hz  | 4.39 | -0.9 dB  |
| Peaking | 6330 Hz  | 2.57 | 3.5 dB   |
| Peaking | 7603 Hz  | 2.37 | -3.8 dB  |
| Peaking | 12435 Hz | 3.09 | 3.9 dB   |
| Peaking | 14162 Hz | 4.7  | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB   |
| Peaking | 62 Hz    | 1.41 | 0.7 dB   |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.6 dB  |
| Peaking | 500 Hz   | 1.41 | -3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -15.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Earsonics%20ES2/Earsonics%20ES2.png)