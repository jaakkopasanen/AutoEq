# BGVP DMG Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.3; 25 -9.5; 28 -9.8; 31 -10.0; 34 -10.2; 37 -10.3; 41 -10.4; 45 -10.6; 49 -10.6; 54 -10.7; 60 -10.9; 66 -11.1; 72 -11.2; 79 -11.4; 87 -11.6; 96 -11.7; 106 -11.9; 116 -11.9; 128 -11.9; 141 -11.9; 155 -11.8; 170 -11.6; 187 -11.3; 206 -11.0; 227 -10.6; 249 -10.1; 274 -9.6; 302 -9.0; 332 -8.3; 365 -7.7; 402 -7.0; 442 -6.5; 486 -5.8; 535 -5.2; 588 -4.6; 647 -4.0; 712 -3.2; 783 -2.5; 861 -1.9; 947 -1.6; 1042 -1.7; 1146 -2.0; 1261 -2.3; 1387 -2.4; 1526 -2.4; 1678 -2.5; 1846 -2.5; 2031 -2.5; 2234 -2.2; 2457 -2.1; 2703 -2.7; 2973 -2.1; 3270 -0.5; 3597 -1.2; 3957 -1.9; 4353 -2.3; 4788 -3.4; 5267 -4.0; 5793 -4.4; 6373 -2.4; 7010 -2.9; 7711 -5.1; 8482 -6.6; 9330 -7.9; 10263 -7.0; 11289 -5.4; 12418 -5.4; 13660 -8.1; 15026 -16.2; 16529 -20.9; 18182 -19.1; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DMG Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DMG Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.36 | -4.0 dB  |
| Peaking | 163 Hz   | 0.53 | -5.3 dB  |
| Peaking | 876 Hz   | 1.18 | 3.2 dB   |
| Peaking | 3475 Hz  | 0.4  | 3.4 dB   |
| Peaking | 17317 Hz | 1.09 | -17.4 dB |
| Peaking | 5678 Hz  | 3.26 | -4.4 dB  |
| Peaking | 6649 Hz  | 1.9  | 4.8 dB   |
| Peaking | 7586 Hz  | 4.45 | -2.8 dB  |
| Peaking | 9116 Hz  | 3.89 | -3.4 dB  |
| Peaking | 12553 Hz | 3.89 | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -15.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/BGVP%20DMG%20Black/BGVP%20DMG%20Black.png)