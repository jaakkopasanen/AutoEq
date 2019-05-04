# Massdrop x Koss ESP95X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.7; 25 -0.8; 28 -0.9; 31 -1.0; 34 -1.0; 37 -1.0; 41 -0.9; 45 -0.6; 49 -0.5; 54 -0.6; 60 -1.8; 66 -3.0; 72 -4.2; 79 -5.7; 87 -6.0; 96 -6.0; 106 -6.2; 116 -6.3; 128 -6.6; 141 -7.0; 155 -7.5; 170 -7.8; 187 -8.0; 206 -8.1; 227 -8.1; 249 -8.1; 274 -7.9; 302 -7.7; 332 -7.5; 365 -7.3; 402 -7.5; 442 -7.6; 486 -7.8; 535 -7.9; 588 -7.9; 647 -7.8; 712 -7.8; 783 -8.7; 861 -9.7; 947 -10.1; 1042 -10.6; 1146 -10.4; 1261 -9.7; 1387 -8.3; 1526 -7.0; 1678 -6.5; 1846 -6.1; 2031 -5.0; 2234 -4.6; 2457 -5.2; 2703 -5.7; 2973 -6.6; 3270 -7.0; 3597 -6.1; 3957 -3.8; 4353 -3.8; 4788 -3.1; 5267 -4.2; 5793 -6.2; 6373 -4.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.1; 13660 -6.8; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Koss ESP95X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Koss ESP95X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.57 | 7.4 dB  |
| Peaking | 630 Hz   | 0.06 | -2.2 dB |
| Peaking | 2193 Hz  | 2.67 | 3.9 dB  |
| Peaking | 4548 Hz  | 2.37 | 5.0 dB  |
| Peaking | 6748 Hz  | 5.89 | 4.0 dB  |
| Peaking | 56 Hz    | 3.9  | 1.6 dB  |
| Peaking | 83 Hz    | 3.25 | -1.2 dB |
| Peaking | 775 Hz   | 0.55 | 1.3 dB  |
| Peaking | 1039 Hz  | 2.4  | -3.6 dB |
| Peaking | 10980 Hz | 4.18 | -1.4 dB |

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