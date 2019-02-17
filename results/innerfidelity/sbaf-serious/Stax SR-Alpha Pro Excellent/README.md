# Stax SR-Alpha Pro Excellent
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -2.4; 60 -4.0; 66 -5.5; 72 -7.7; 79 -9.6; 87 -9.8; 96 -9.7; 106 -9.4; 116 -8.6; 128 -8.0; 141 -7.5; 155 -7.2; 170 -6.9; 187 -6.6; 206 -6.5; 227 -6.2; 249 -6.1; 274 -5.9; 302 -5.9; 332 -5.8; 365 -5.7; 402 -5.7; 442 -5.4; 486 -5.5; 535 -5.5; 588 -5.4; 647 -5.4; 712 -5.7; 783 -5.6; 861 -5.9; 947 -6.2; 1042 -6.6; 1146 -7.0; 1261 -7.6; 1387 -8.4; 1526 -9.1; 1678 -9.7; 1846 -9.5; 2031 -8.3; 2234 -7.8; 2457 -7.3; 2703 -6.3; 2973 -5.2; 3270 -4.5; 3597 -3.9; 3957 -3.0; 4353 -3.5; 4788 -2.6; 5267 -1.6; 5793 -2.7; 6373 -5.3; 7010 -6.1; 7711 -7.6; 8482 -10.5; 9330 -11.3; 10263 -8.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-Alpha Pro Excellent GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Alpha Pro Excellent ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 61 Hz    | 0.3  | 19.3 dB  |
| Peaking | 86 Hz    | 0.55 | -21.3 dB |
| Peaking | 1737 Hz  | 2.03 | -3.9 dB  |
| Peaking | 4924 Hz  | 1.25 | 4.7 dB   |
| Peaking | 8935 Hz  | 2.93 | -6.2 dB  |
| Peaking | 665 Hz   | 1.92 | 0.7 dB   |
| Peaking | 5469 Hz  | 6.22 | 2.8 dB   |
| Peaking | 5786 Hz  | 2.58 | -1.6 dB  |
| Peaking | 11382 Hz | 5.94 | 0.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Alpha%20Pro%20Excellent/Stax%20SR-Alpha%20Pro%20Excellent.png)