# Massdrop x Koss ESP95X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.7; 25 -0.7; 28 -0.9; 31 -1.0; 34 -1.0; 37 -1.0; 41 -0.8; 45 -0.6; 49 -0.5; 54 -0.6; 60 -2.0; 66 -2.9; 72 -4.0; 79 -5.8; 87 -5.9; 96 -6.0; 106 -6.2; 116 -6.3; 128 -6.6; 141 -7.0; 155 -7.5; 170 -7.8; 187 -8.0; 206 -8.1; 227 -8.1; 249 -8.1; 274 -7.9; 302 -7.7; 332 -7.4; 365 -7.3; 402 -7.5; 442 -7.6; 486 -7.8; 535 -7.9; 588 -7.9; 647 -7.8; 712 -7.8; 783 -8.7; 861 -9.7; 947 -10.1; 1042 -10.6; 1146 -10.3; 1261 -9.7; 1387 -8.3; 1526 -7.0; 1678 -6.5; 1846 -6.2; 2031 -4.9; 2234 -4.6; 2457 -5.2; 2703 -5.6; 2973 -6.6; 3270 -6.9; 3597 -6.2; 3957 -3.7; 4353 -3.9; 4788 -3.1; 5267 -4.1; 5793 -6.2; 6373 -4.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.1; 13660 -6.8; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Koss ESP95X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Koss ESP95X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.56 | 7.3 dB  |
| Peaking | 628 Hz   | 0.06 | -2.2 dB |
| Peaking | 2196 Hz  | 2.68 | 3.9 dB  |
| Peaking | 4553 Hz  | 2.34 | 5.0 dB  |
| Peaking | 6782 Hz  | 6.19 | 4.1 dB  |
| Peaking | 55 Hz    | 4.3  | 1.3 dB  |
| Peaking | 82 Hz    | 3.44 | -1.2 dB |
| Peaking | 769 Hz   | 0.56 | 1.3 dB  |
| Peaking | 1037 Hz  | 2.36 | -3.6 dB |
| Peaking | 11158 Hz | 4.18 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Koss%20ESP95X/Massdrop%20x%20Koss%20ESP95X.png)