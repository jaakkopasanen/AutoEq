# Final Audio E5000 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.6; 25 -11.9; 28 -12.4; 31 -12.8; 34 -13.1; 37 -13.3; 41 -13.5; 45 -13.6; 49 -13.6; 54 -13.7; 60 -13.8; 66 -13.8; 72 -13.9; 79 -14.0; 87 -14.0; 96 -14.0; 106 -14.1; 116 -13.9; 128 -13.8; 141 -13.7; 155 -13.4; 170 -13.2; 187 -12.8; 206 -12.6; 227 -12.2; 249 -11.9; 274 -11.5; 302 -11.1; 332 -10.5; 365 -10.0; 402 -9.6; 442 -9.2; 486 -8.8; 535 -8.4; 588 -8.0; 647 -7.5; 712 -6.9; 783 -6.8; 861 -6.7; 947 -6.6; 1042 -6.8; 1146 -7.1; 1261 -7.5; 1387 -7.4; 1526 -7.0; 1678 -6.5; 1846 -5.8; 2031 -4.9; 2234 -4.0; 2457 -3.4; 2703 -3.2; 2973 -3.3; 3270 -3.2; 3597 -2.9; 3957 -1.9; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.9; 15026 -24.1; 16529 -26.1; 18182 -19.4; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E5000 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E5000 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.5  | -4.8 dB  |
| Peaking | 141 Hz   | 0.42 | -6.2 dB  |
| Peaking | 2484 Hz  | 4.38 | 1.5 dB   |
| Peaking | 5295 Hz  | 0.85 | 6.6 dB   |
| Peaking | 16473 Hz | 1.47 | -22.5 dB |
| Peaking | 797 Hz   | 2.37 | 0.8 dB   |
| Peaking | 1368 Hz  | 3.03 | -1.4 dB  |
| Peaking | 7850 Hz  | 4.74 | -2.8 dB  |
| Peaking | 12837 Hz | 2.33 | 7.0 dB   |
| Peaking | 14832 Hz | 3.21 | -7.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -5.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 16000 Hz | 1.41 | -21.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20E5000%20sample%202/Final%20Audio%20E5000%20sample%202.png)