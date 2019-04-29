# Dita Audio Answer
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.4; 25 -6.7; 28 -7.2; 31 -7.5; 34 -7.7; 37 -7.9; 41 -8.1; 45 -8.4; 49 -8.6; 54 -8.7; 60 -8.9; 66 -9.1; 72 -9.3; 79 -9.6; 87 -9.8; 96 -10.2; 106 -10.4; 116 -10.7; 128 -10.8; 141 -11.0; 155 -11.2; 170 -11.2; 187 -11.2; 206 -11.2; 227 -11.3; 249 -11.3; 274 -11.3; 302 -11.1; 332 -10.8; 365 -10.5; 402 -10.3; 442 -10.0; 486 -9.7; 535 -9.3; 588 -8.8; 647 -8.3; 712 -7.7; 783 -7.1; 861 -6.5; 947 -6.1; 1042 -6.0; 1146 -5.9; 1261 -5.8; 1387 -5.5; 1526 -4.4; 1678 -3.1; 1846 -2.0; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.0; 3957 -2.4; 4353 -4.1; 4788 -6.3; 5267 -7.1; 5793 -5.0; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -7.0; 12418 -10.0; 13660 -13.4; 15026 -17.5; 16529 -22.1; 18182 -25.9; 20000 -26.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Audio Answer GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Audio Answer ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 126 Hz   | 0.45 | -3.3 dB  |
| Peaking | 331 Hz   | 0.63 | -2.9 dB  |
| Peaking | 2633 Hz  | 1    | 7.1 dB   |
| Peaking | 10631 Hz | 0.63 | 9.6 dB   |
| Peaking | 18729 Hz | 0.27 | -21.9 dB |
| Peaking | 18 Hz    | 2.01 | 1.1 dB   |
| Peaking | 3657 Hz  | 5.16 | 1.4 dB   |
| Peaking | 5165 Hz  | 4.06 | -3.2 dB  |
| Peaking | 6523 Hz  | 4.48 | 4.5 dB   |
| Peaking | 7879 Hz  | 3    | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 16000 Hz | 1.41 | -20.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Dita%20Audio%20Answer/Dita%20Audio%20Answer.png)