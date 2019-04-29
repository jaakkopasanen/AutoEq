# Dita Audio Dream
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -11.7; 25 -11.6; 28 -11.3; 31 -11.1; 34 -10.8; 37 -10.6; 41 -10.4; 45 -10.2; 49 -10.0; 54 -9.8; 60 -9.6; 66 -9.6; 72 -9.5; 79 -9.6; 87 -9.7; 96 -9.8; 106 -9.9; 116 -10.1; 128 -10.2; 141 -10.3; 155 -10.3; 170 -10.3; 187 -10.3; 206 -10.2; 227 -10.1; 249 -10.0; 274 -9.9; 302 -9.6; 332 -9.2; 365 -8.8; 402 -8.6; 442 -8.2; 486 -7.9; 535 -7.5; 588 -7.0; 647 -6.6; 712 -6.1; 783 -5.5; 861 -5.0; 947 -4.8; 1042 -4.9; 1146 -5.2; 1261 -5.5; 1387 -5.3; 1526 -4.7; 1678 -3.9; 1846 -3.1; 2031 -2.0; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.0; 3597 -2.3; 3957 -4.2; 4353 -6.4; 4788 -7.8; 5267 -6.3; 5793 -6.0; 6373 -4.1; 7010 -4.2; 7711 -6.5; 8482 -10.0; 9330 -10.9; 10263 -9.0; 11289 -7.1; 12418 -8.9; 13660 -15.8; 15026 -22.8; 16529 -25.4; 18182 -24.5; 20000 -21.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Audio Dream GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Audio Dream ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.22 | -5.6 dB  |
| Peaking | 192 Hz   | 0.66 | -3.7 dB  |
| Peaking | 2594 Hz  | 1.21 | 6.5 dB   |
| Peaking | 16015 Hz | 1.73 | -13.0 dB |
| Peaking | 18982 Hz | 0.76 | -16.3 dB |
| Peaking | 887 Hz   | 3.46 | 1.6 dB   |
| Peaking | 4720 Hz  | 5.54 | -3.1 dB  |
| Peaking | 6835 Hz  | 3.84 | 3.7 dB   |
| Peaking | 8965 Hz  | 3.62 | -3.7 dB  |
| Peaking | 11660 Hz | 4.37 | 4.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 16000 Hz | 1.41 | -23.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Dita%20Audio%20Dream/Dita%20Audio%20Dream.png)