# AZLA 01R Mk2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.1; 25 -8.4; 28 -8.8; 31 -9.1; 34 -9.3; 37 -9.5; 41 -9.7; 45 -9.8; 49 -9.9; 54 -9.9; 60 -10.0; 66 -10.0; 72 -10.1; 79 -10.2; 87 -10.3; 96 -10.3; 106 -10.4; 116 -10.3; 128 -10.3; 141 -10.2; 155 -10.0; 170 -9.7; 187 -9.5; 206 -9.1; 227 -8.7; 249 -8.4; 274 -7.9; 302 -7.5; 332 -6.9; 365 -6.4; 402 -6.0; 442 -5.6; 486 -5.1; 535 -4.7; 588 -4.3; 647 -3.9; 712 -3.5; 783 -3.2; 861 -3.0; 947 -3.1; 1042 -3.6; 1146 -4.3; 1261 -4.9; 1387 -5.3; 1526 -5.5; 1678 -5.6; 1846 -5.9; 2031 -6.3; 2234 -6.8; 2457 -7.1; 2703 -6.4; 2973 -4.8; 3270 -3.7; 3597 -3.7; 3957 -5.7; 4353 -8.6; 4788 -9.2; 5267 -7.7; 5793 -3.1; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -6.1; 16529 -13.5; 18182 -18.2; 20000 -16.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AZLA 01R Mk2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AZLA 01R Mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 86 Hz    | 0.31 | -4.6 dB  |
| Peaking | 747 Hz   | 1.05 | 3.4 dB   |
| Peaking | 4871 Hz  | 4.97 | -4.8 dB  |
| Peaking | 6296 Hz  | 4.1  | 6.3 dB   |
| Peaking | 18785 Hz | 1.15 | -14.2 dB |
| Peaking | 982 Hz   | 5.85 | 0.7 dB   |
| Peaking | 2550 Hz  | 1.88 | -2.2 dB  |
| Peaking | 3351 Hz  | 2.69 | 3.8 dB   |
| Peaking | 4281 Hz  | 6.98 | -2.1 dB  |
| Peaking | 14182 Hz | 2.92 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -6.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/AZLA%2001R%20Mk2/AZLA%2001R%20Mk2.png)