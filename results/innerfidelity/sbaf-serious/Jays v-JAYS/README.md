# Jays v-JAYS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.6; 54 -2.9; 60 -4.2; 66 -5.2; 72 -5.8; 79 -6.3; 87 -6.4; 96 -6.4; 106 -6.2; 116 -5.9; 128 -5.7; 141 -5.2; 155 -5.0; 170 -4.6; 187 -4.3; 206 -3.9; 227 -3.4; 249 -2.8; 274 -2.4; 302 -2.8; 332 -5.2; 365 -4.8; 402 -4.1; 442 -3.6; 486 -3.5; 535 -3.3; 588 -2.8; 647 -2.8; 712 -2.9; 783 -2.8; 861 -3.2; 947 -3.1; 1042 -3.7; 1146 -4.2; 1261 -5.1; 1387 -6.4; 1526 -8.1; 1678 -9.8; 1846 -11.1; 2031 -11.7; 2234 -11.8; 2457 -11.4; 2703 -11.8; 2973 -12.3; 3270 -12.2; 3597 -14.0; 3957 -16.1; 4353 -14.2; 4788 -10.7; 5267 -8.0; 5793 -5.7; 6373 -1.1; 7010 -4.0; 7711 -6.6; 8482 -9.1; 9330 -9.5; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.8; 16529 -10.5; 18182 -12.0; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jays v-JAYS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays v-JAYS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 1.03 | 6.9 dB   |
| Peaking | 1433 Hz  | 0.22 | 5.5 dB   |
| Peaking | 2158 Hz  | 1.05 | -10.3 dB |
| Peaking | 3983 Hz  | 2.86 | -10.7 dB |
| Peaking | 17947 Hz | 1.28 | -6.1 dB  |
| Peaking | 89 Hz    | 2.54 | -1.5 dB  |
| Peaking | 287 Hz   | 2.01 | 3.4 dB   |
| Peaking | 342 Hz   | 2.69 | -3.8 dB  |
| Peaking | 6414 Hz  | 6.97 | 5.9 dB   |
| Peaking | 8866 Hz  | 4.28 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | -6.6 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jays%20v-JAYS/Jays%20v-JAYS.png)