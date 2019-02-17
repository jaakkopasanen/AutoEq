# JAYS u-JAYS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.2; 25 -3.6; 28 -3.9; 31 -4.2; 34 -4.4; 37 -4.6; 41 -4.8; 45 -4.9; 49 -4.9; 54 -5.0; 60 -5.3; 66 -5.6; 72 -5.7; 79 -5.9; 87 -6.0; 96 -6.1; 106 -5.9; 116 -5.9; 128 -5.9; 141 -6.4; 155 -6.3; 170 -5.8; 187 -6.0; 206 -5.9; 227 -5.5; 249 -5.1; 274 -4.2; 302 -3.3; 332 -2.7; 365 -2.8; 402 -3.1; 442 -3.5; 486 -4.0; 535 -4.3; 588 -4.3; 647 -4.8; 712 -5.3; 783 -5.5; 861 -5.9; 947 -6.3; 1042 -6.5; 1146 -6.4; 1261 -6.4; 1387 -6.5; 1526 -6.7; 1678 -6.6; 1846 -6.0; 2031 -5.1; 2234 -4.3; 2457 -3.1; 2703 -2.4; 2973 -2.2; 3270 -2.8; 3597 -2.1; 3957 -0.5; 4353 -1.1; 4788 -0.8; 5267 -1.7; 5793 -3.6; 6373 -4.3; 7010 -5.5; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JAYS u-JAYS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS u-JAYS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.89 | 3.6 dB  |
| Peaking | 50 Hz   | 1.78 | 0.8 dB  |
| Peaking | 377 Hz  | 1.4  | 3.8 dB  |
| Peaking | 2721 Hz | 3.1  | 3.0 dB  |
| Peaking | 4427 Hz | 1.83 | 5.9 dB  |
| Peaking | 659 Hz  | 1.95 | 1.2 dB  |
| Peaking | 881 Hz  | 0.69 | -0.9 dB |
| Peaking | 1644 Hz | 3.1  | -1.4 dB |
| Peaking | 1805 Hz | 1.11 | 0.9 dB  |
| Peaking | 8587 Hz | 2.93 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JAYS%20u-JAYS/JAYS%20u-JAYS.png)