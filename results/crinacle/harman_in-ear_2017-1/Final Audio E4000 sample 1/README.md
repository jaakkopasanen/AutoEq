# Final Audio E4000 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.9; 25 -6.4; 28 -7.1; 31 -7.7; 34 -8.1; 37 -8.5; 41 -9.0; 45 -9.4; 49 -9.7; 54 -10.0; 60 -10.4; 66 -10.8; 72 -11.1; 79 -11.4; 87 -11.7; 96 -12.0; 106 -12.2; 116 -12.3; 128 -12.4; 141 -12.4; 155 -12.4; 170 -12.2; 187 -12.0; 206 -11.7; 227 -11.3; 249 -11.0; 274 -10.5; 302 -10.0; 332 -9.5; 365 -8.9; 402 -8.4; 442 -7.9; 486 -7.4; 535 -6.8; 588 -6.3; 647 -5.7; 712 -5.0; 783 -4.4; 861 -4.3; 947 -4.3; 1042 -4.0; 1146 -4.3; 1261 -5.0; 1387 -5.2; 1526 -5.1; 1678 -4.8; 1846 -4.5; 2031 -4.1; 2234 -3.6; 2457 -3.3; 2703 -3.0; 2973 -2.6; 3270 -2.0; 3597 -1.4; 3957 -0.9; 4353 -0.7; 4788 -0.5; 5267 -0.9; 5793 -1.5; 6373 -2.0; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -11.0; 15026 -21.6; 16529 -23.3; 18182 -20.4; 20000 -20.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E4000 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E4000 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.99 | -1.5 dB  |
| Peaking | 150 Hz   | 0.48 | -6.2 dB  |
| Peaking | 797 Hz   | 2.14 | 1.9 dB   |
| Peaking | 10642 Hz | 0.26 | 15.0 dB  |
| Peaking | 16543 Hz | 0.43 | -29.1 dB |
| Peaking | 1771 Hz  | 1.92 | -1.0 dB  |
| Peaking | 4890 Hz  | 1.47 | 1.9 dB   |
| Peaking | 8101 Hz  | 2.63 | -3.4 dB  |
| Peaking | 12774 Hz | 5.42 | 5.3 dB   |
| Peaking | 19946 Hz | 2.28 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -20.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20E4000%20sample%201/Final%20Audio%20E4000%20sample%201.png)