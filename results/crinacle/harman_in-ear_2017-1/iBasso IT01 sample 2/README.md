# iBasso IT01 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.8; 23 -11.8; 25 -11.8; 28 -11.8; 31 -11.8; 34 -11.7; 37 -11.7; 41 -11.6; 45 -11.5; 49 -11.5; 54 -11.5; 60 -11.4; 66 -11.4; 72 -11.4; 79 -11.5; 87 -11.6; 96 -11.7; 106 -11.8; 116 -11.9; 128 -12.0; 141 -12.1; 155 -12.1; 170 -12.0; 187 -11.9; 206 -11.8; 227 -11.6; 249 -11.4; 274 -11.2; 302 -10.9; 332 -10.5; 365 -10.1; 402 -9.8; 442 -9.5; 486 -9.2; 535 -8.6; 588 -7.9; 647 -7.1; 712 -6.3; 783 -5.6; 861 -5.1; 947 -4.8; 1042 -4.8; 1146 -5.1; 1261 -5.5; 1387 -5.4; 1526 -5.0; 1678 -4.6; 1846 -4.1; 2031 -3.4; 2234 -2.7; 2457 -1.9; 2703 -1.3; 2973 -0.7; 3270 -0.5; 3597 -0.6; 3957 -1.6; 4353 -3.5; 4788 -5.4; 5267 -4.8; 5793 -2.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.6; 15026 -19.9; 16529 -26.8; 18182 -23.6; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT01 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT01 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 158 Hz   | 0.05 | -5.4 dB  |
| Peaking | 819 Hz   | 1.15 | 4.3 dB   |
| Peaking | 3123 Hz  | 0.48 | 8.0 dB   |
| Peaking | 12408 Hz | 1.56 | 8.4 dB   |
| Peaking | 16765 Hz | 0.88 | -23.6 dB |
| Peaking | 17 Hz    | 1.59 | -0.5 dB  |
| Peaking | 3431 Hz  | 3.06 | 1.3 dB   |
| Peaking | 4900 Hz  | 3.45 | -4.0 dB  |
| Peaking | 6371 Hz  | 3.68 | 4.4 dB   |
| Peaking | 7479 Hz  | 4.24 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 16000 Hz | 1.41 | -20.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/iBasso%20IT01%20sample%202/iBasso%20IT01%20sample%202.png)