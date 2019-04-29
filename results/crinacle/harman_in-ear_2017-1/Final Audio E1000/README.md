# Final Audio E1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.0; 34 -1.5; 37 -2.0; 41 -2.5; 45 -3.0; 49 -3.4; 54 -3.9; 60 -4.5; 66 -5.1; 72 -5.6; 79 -6.2; 87 -6.7; 96 -7.3; 106 -7.9; 116 -8.4; 128 -8.9; 141 -9.4; 155 -9.7; 170 -10.1; 187 -10.3; 206 -10.4; 227 -10.6; 249 -10.6; 274 -10.7; 302 -10.6; 332 -10.4; 365 -10.2; 402 -10.0; 442 -9.9; 486 -9.6; 535 -9.2; 588 -8.8; 647 -8.2; 712 -7.6; 783 -7.0; 861 -6.4; 947 -6.1; 1042 -6.1; 1146 -6.4; 1261 -6.9; 1387 -7.1; 1526 -6.8; 1678 -6.3; 1846 -5.6; 2031 -4.9; 2234 -4.2; 2457 -3.6; 2703 -3.3; 2973 -2.7; 3270 -2.2; 3597 -1.8; 3957 -1.7; 4353 -2.0; 4788 -3.0; 5267 -4.8; 5793 -6.3; 6373 -4.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.6; 15026 -22.2; 16529 -25.9; 18182 -20.9; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.49 | 6.3 dB   |
| Peaking | 239 Hz   | 0.5  | -4.6 dB  |
| Peaking | 3961 Hz  | 0.83 | 5.8 dB   |
| Peaking | 12443 Hz | 0.99 | 13.3 dB  |
| Peaking | 16070 Hz | 0.73 | -26.1 dB |
| Peaking | 949 Hz   | 3.18 | 1.3 dB   |
| Peaking | 1440 Hz  | 3.34 | -1.3 dB  |
| Peaking | 5742 Hz  | 5.86 | -2.4 dB  |
| Peaking | 6721 Hz  | 7.43 | 3.5 dB   |
| Peaking | 17704 Hz | 4.38 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 1.1 dB   |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -20.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20E1000/Final%20Audio%20E1000.png)