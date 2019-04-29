# NocturnaL Audio Gorham
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.8; 25 -7.1; 28 -7.6; 31 -7.9; 34 -8.1; 37 -8.3; 41 -8.6; 45 -8.8; 49 -9.1; 54 -9.3; 60 -9.6; 66 -9.9; 72 -10.2; 79 -10.5; 87 -10.9; 96 -11.3; 106 -11.7; 116 -12.0; 128 -12.2; 141 -12.4; 155 -12.5; 170 -12.6; 187 -12.7; 206 -12.7; 227 -12.6; 249 -12.3; 274 -12.1; 302 -11.8; 332 -11.4; 365 -10.9; 402 -10.5; 442 -10.1; 486 -9.6; 535 -9.0; 588 -8.4; 647 -7.8; 712 -7.2; 783 -6.5; 861 -5.9; 947 -5.6; 1042 -5.6; 1146 -5.9; 1261 -6.1; 1387 -5.9; 1526 -5.4; 1678 -4.7; 1846 -4.2; 2031 -3.5; 2234 -2.9; 2457 -2.0; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.3; 5793 -3.5; 6373 -5.1; 7010 -7.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.4; 13660 -19.1; 15026 -28.5; 16529 -26.8; 18182 -13.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NocturnaL Audio Gorham GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NocturnaL Audio Gorham ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 132 Hz   | 0.48 | -5.0 dB  |
| Peaking | 295 Hz   | 0.86 | -2.7 dB  |
| Peaking | 2807 Hz  | 4.01 | 1.2 dB   |
| Peaking | 3932 Hz  | 0.68 | 6.3 dB   |
| Peaking | 15739 Hz | 1.98 | -26.1 dB |
| Peaking | 923 Hz   | 3.35 | 1.1 dB   |
| Peaking | 1372 Hz  | 3.1  | -0.8 dB  |
| Peaking | 6920 Hz  | 5.4  | -3.4 dB  |
| Peaking | 12024 Hz | 2.19 | 6.8 dB   |
| Peaking | 14087 Hz | 2.93 | -7.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -22.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/NocturnaL%20Audio%20Gorham/NocturnaL%20Audio%20Gorham.png)