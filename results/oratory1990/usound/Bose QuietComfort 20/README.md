# Bose QuietComfort 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -4.3; 25 -5.2; 28 -6.1; 31 -6.7; 34 -6.9; 37 -6.9; 41 -6.8; 45 -6.7; 49 -6.6; 54 -6.4; 60 -6.4; 66 -6.6; 72 -6.8; 79 -7.1; 87 -7.6; 96 -8.0; 106 -8.2; 116 -8.3; 128 -8.1; 141 -7.8; 155 -7.5; 170 -7.3; 187 -7.3; 206 -7.3; 227 -7.3; 249 -7.3; 274 -7.3; 302 -7.2; 332 -7.2; 365 -7.3; 402 -7.4; 442 -7.5; 486 -7.3; 535 -6.4; 588 -5.1; 647 -4.1; 712 -3.5; 783 -2.7; 861 -1.9; 947 -2.1; 1042 -3.0; 1146 -4.2; 1261 -5.2; 1387 -6.1; 1526 -8.6; 1678 -10.7; 1846 -10.8; 2031 -9.5; 2234 -8.4; 2457 -8.1; 2703 -7.7; 2973 -7.4; 3270 -7.4; 3597 -7.9; 3957 -9.0; 4353 -8.6; 4788 -5.8; 5267 -2.1; 5793 -0.5; 6373 -1.1; 7010 -7.4; 7711 -10.5; 8482 -6.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 911 Hz  | 2.11 | 5.2 dB  |
| Peaking | 1794 Hz | 2.8  | -5.2 dB |
| Peaking | 4266 Hz | 2.34 | -4.9 dB |
| Peaking | 5929 Hz | 2.05 | 8.9 dB  |
| Peaking | 7545 Hz | 4.45 | -7.8 dB |
| Peaking | 65 Hz   | 2.11 | 0.5 dB  |
| Peaking | 110 Hz  | 1.5  | -1.8 dB |
| Peaking | 268 Hz  | 1.26 | -0.6 dB |
| Peaking | 477 Hz  | 2.1  | -1.5 dB |
| Peaking | 638 Hz  | 3.13 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)