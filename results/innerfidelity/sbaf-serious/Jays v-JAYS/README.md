# Jays v-JAYS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -2.0; 45 -3.4; 49 -4.6; 54 -6.0; 60 -7.3; 66 -8.2; 72 -8.8; 79 -9.3; 87 -9.5; 96 -9.5; 106 -9.2; 116 -8.9; 128 -8.7; 141 -8.3; 155 -8.1; 170 -7.6; 187 -7.3; 206 -7.0; 227 -6.5; 249 -5.9; 274 -5.5; 302 -5.8; 332 -8.3; 365 -7.9; 402 -7.2; 442 -6.6; 486 -6.5; 535 -6.3; 588 -5.9; 647 -5.8; 712 -6.0; 783 -5.9; 861 -6.3; 947 -6.1; 1042 -6.7; 1146 -7.2; 1261 -8.1; 1387 -9.4; 1526 -11.1; 1678 -12.8; 1846 -14.2; 2031 -14.7; 2234 -14.8; 2457 -14.4; 2703 -14.8; 2973 -15.4; 3270 -15.3; 3597 -17.1; 3957 -19.1; 4353 -17.2; 4788 -13.7; 5267 -11.1; 5793 -8.7; 6373 -3.6; 7010 -6.4; 7711 -9.6; 8482 -12.1; 9330 -12.6; 10263 -8.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.3; 16529 -13.5; 18182 -15.1; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jays v-JAYS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays v-JAYS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 1.92 | 7.4 dB   |
| Peaking | 2144 Hz  | 1.61 | -7.7 dB  |
| Peaking | 3951 Hz  | 2.35 | -11.4 dB |
| Peaking | 17032 Hz | 2.21 | -4.8 dB  |
| Peaking | 18709 Hz | 1.1  | -7.1 dB  |
| Peaking | 33 Hz    | 0.03 | 0.9 dB   |
| Peaking | 98 Hz    | 0.94 | -4.2 dB  |
| Peaking | 6511 Hz  | 5.2  | 7.2 dB   |
| Peaking | 9279 Hz  | 1.68 | -9.8 dB  |
| Peaking | 10805 Hz | 1.5  | 6.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.2 dB |
| Peaking | 4000 Hz  | 1.41 | -9.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jays%20v-JAYS/Jays%20v-JAYS.png)