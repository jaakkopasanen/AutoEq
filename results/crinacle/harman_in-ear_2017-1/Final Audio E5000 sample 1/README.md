# Final Audio E5000 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -10.2; 25 -10.6; 28 -11.1; 31 -11.5; 34 -11.8; 37 -12.1; 41 -12.3; 45 -12.5; 49 -12.7; 54 -12.8; 60 -12.9; 66 -13.0; 72 -13.1; 79 -13.2; 87 -13.3; 96 -13.4; 106 -13.4; 116 -13.4; 128 -13.4; 141 -13.3; 155 -13.1; 170 -12.9; 187 -12.6; 206 -12.2; 227 -11.9; 249 -11.5; 274 -11.1; 302 -10.7; 332 -10.2; 365 -9.7; 402 -9.3; 442 -8.9; 486 -8.5; 535 -8.1; 588 -7.7; 647 -7.3; 712 -6.8; 783 -6.4; 861 -6.0; 947 -6.0; 1042 -6.2; 1146 -6.8; 1261 -7.3; 1387 -7.3; 1526 -6.9; 1678 -6.4; 1846 -5.8; 2031 -5.1; 2234 -4.3; 2457 -3.6; 2703 -3.2; 2973 -3.1; 3270 -2.6; 3597 -1.8; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.4; 15026 -19.6; 16529 -20.7; 18182 -15.3; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E5000 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E5000 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.43 | -4.9 dB  |
| Peaking | 168 Hz   | 0.54 | -5.0 dB  |
| Peaking | 4772 Hz  | 0.93 | 6.7 dB   |
| Peaking | 16408 Hz | 1.46 | -16.3 dB |
| Peaking | 882 Hz   | 2.61 | 1.1 dB   |
| Peaking | 1371 Hz  | 3.21 | -1.5 dB  |
| Peaking | 7961 Hz  | 5.16 | -2.3 dB  |
| Peaking | 12930 Hz | 2.53 | 4.7 dB   |
| Peaking | 14706 Hz | 3.87 | -5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -5.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 16000 Hz | 1.41 | -15.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20E5000%20sample%201/Final%20Audio%20E5000%20sample%201.png)