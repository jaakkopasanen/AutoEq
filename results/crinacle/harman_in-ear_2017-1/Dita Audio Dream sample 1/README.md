# Dita Audio Dream sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.5; 25 -11.4; 28 -11.1; 31 -10.8; 34 -10.5; 37 -10.3; 41 -10.1; 45 -9.9; 49 -9.6; 54 -9.3; 60 -9.1; 66 -9.1; 72 -9.0; 79 -9.0; 87 -9.2; 96 -9.3; 106 -9.4; 116 -9.6; 128 -9.6; 141 -9.7; 155 -9.8; 170 -9.8; 187 -9.8; 206 -9.7; 227 -9.7; 249 -9.6; 274 -9.5; 302 -9.3; 332 -9.0; 365 -8.7; 402 -8.5; 442 -8.3; 486 -8.0; 535 -7.7; 588 -7.3; 647 -7.1; 712 -6.5; 783 -5.8; 861 -5.4; 947 -5.2; 1042 -5.3; 1146 -5.6; 1261 -5.8; 1387 -5.6; 1526 -5.0; 1678 -4.1; 1846 -3.2; 2031 -2.1; 2234 -1.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.9; 3597 -2.2; 3957 -4.0; 4353 -6.0; 4788 -7.2; 5267 -5.7; 5793 -6.4; 6373 -5.3; 7010 -5.6; 7711 -8.7; 8482 -10.6; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -7.8; 13660 -17.0; 15026 -24.3; 16529 -27.2; 18182 -28.3; 20000 -26.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Audio Dream sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Audio Dream sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.8  | -4.7 dB  |
| Peaking | 357 Hz   | 0.17 | -3.4 dB  |
| Peaking | 5766 Hz  | 1.03 | -7.2 dB  |
| Peaking | 7604 Hz  | 0.22 | 18.5 dB  |
| Peaking | 17315 Hz | 0.3  | -32.2 dB |
| Peaking | 2785 Hz  | 3.68 | 2.0 dB   |
| Peaking | 6771 Hz  | 4.46 | 3.6 dB   |
| Peaking | 8328 Hz  | 2.56 | -5.5 dB  |
| Peaking | 11962 Hz | 1.86 | 6.8 dB   |
| Peaking | 14519 Hz | 2.57 | -6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -26.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Dita%20Audio%20Dream%20sample%201/Dita%20Audio%20Dream%20sample%201.png)