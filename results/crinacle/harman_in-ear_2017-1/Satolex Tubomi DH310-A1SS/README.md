# Satolex Tubomi DH310-A1SS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -7.0; 25 -7.4; 28 -8.0; 31 -8.5; 34 -8.8; 37 -9.1; 41 -9.5; 45 -9.8; 49 -10.1; 54 -10.4; 60 -10.7; 66 -11.0; 72 -11.3; 79 -11.6; 87 -11.8; 96 -12.1; 106 -12.3; 116 -12.4; 128 -12.4; 141 -12.4; 155 -12.3; 170 -12.1; 187 -11.9; 206 -11.5; 227 -11.1; 249 -10.7; 274 -10.2; 302 -9.5; 332 -8.9; 365 -8.1; 402 -7.5; 442 -6.9; 486 -6.2; 535 -5.6; 588 -4.9; 647 -4.2; 712 -3.5; 783 -2.6; 861 -2.0; 947 -1.6; 1042 -1.5; 1146 -1.7; 1261 -1.7; 1387 -1.7; 1526 -1.4; 1678 -1.0; 1846 -0.8; 2031 -0.7; 2234 -0.5; 2457 -1.3; 2703 -2.4; 2973 -3.0; 3270 -2.8; 3597 -2.1; 3957 -1.3; 4353 -1.2; 4788 -2.1; 5267 -4.2; 5793 -8.0; 6373 -8.3; 7010 -4.1; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -8.5; 15026 -19.4; 16529 -21.5; 18182 -16.8; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Satolex Tubomi DH310-A1SS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Satolex Tubomi DH310-A1SS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 68 Hz    | 0.43 | -3.1 dB  |
| Peaking | 197 Hz   | 0.41 | -5.7 dB  |
| Peaking | 1226 Hz  | 0.51 | 3.0 dB   |
| Peaking | 3366 Hz  | 0.1  | 2.3 dB   |
| Peaking | 16860 Hz | 1.02 | -18.2 dB |
| Peaking | 3156 Hz  | 3.17 | -2.6 dB  |
| Peaking | 4186 Hz  | 1.14 | 2.7 dB   |
| Peaking | 5982 Hz  | 4.66 | -6.9 dB  |
| Peaking | 12597 Hz | 4.15 | 4.9 dB   |
| Peaking | 19939 Hz | 1.54 | -6.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.3 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 16000 Hz | 1.41 | -16.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Satolex%20Tubomi%20DH310-A1SS/Satolex%20Tubomi%20DH310-A1SS.png)