# Massdrop x Koss ESP95X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.9; 87 -2.0; 96 -2.1; 106 -2.3; 116 -2.4; 128 -2.7; 141 -3.1; 155 -3.6; 170 -3.9; 187 -4.1; 206 -4.2; 227 -4.2; 249 -4.2; 274 -4.0; 302 -3.8; 332 -3.6; 365 -3.4; 402 -3.6; 442 -3.7; 486 -3.9; 535 -4.0; 588 -4.1; 647 -3.9; 712 -3.9; 783 -4.8; 861 -5.8; 947 -6.2; 1042 -6.7; 1146 -6.5; 1261 -5.8; 1387 -4.4; 1526 -3.1; 1678 -2.6; 1846 -2.3; 2031 -1.1; 2234 -0.7; 2457 -1.3; 2703 -1.8; 2973 -2.7; 3270 -3.1; 3597 -2.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.6; 5793 -2.4; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Koss ESP95X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Koss ESP95X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.3  | 6.3 dB  |
| Peaking | 121 Hz  | 2.08 | 0.3 dB  |
| Peaking | 433 Hz  | 1.07 | 2.5 dB  |
| Peaking | 2157 Hz | 1.84 | 5.1 dB  |
| Peaking | 4754 Hz | 1.55 | 6.1 dB  |
| Peaking | 712 Hz  | 4.18 | 1.5 dB  |
| Peaking | 1096 Hz | 1.81 | -1.7 dB |
| Peaking | 1518 Hz | 4.3  | 1.7 dB  |
| Peaking | 6540 Hz | 6.77 | 3.3 dB  |
| Peaking | 7775 Hz | 1.81 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | 2.5 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Koss%20ESP95X/Massdrop%20x%20Koss%20ESP95X.png)