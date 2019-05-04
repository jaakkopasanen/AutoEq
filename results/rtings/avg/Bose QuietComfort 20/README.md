# Bose QuietComfort 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -4.7; 25 -6.1; 28 -7.7; 31 -8.7; 34 -9.2; 37 -9.5; 41 -9.5; 45 -9.5; 49 -9.4; 54 -9.2; 60 -9.2; 66 -9.2; 72 -9.3; 79 -9.5; 87 -9.8; 96 -10.1; 106 -10.3; 116 -10.3; 128 -10.1; 141 -9.7; 155 -9.4; 170 -9.1; 187 -9.0; 206 -8.9; 227 -9.0; 249 -8.9; 274 -8.9; 302 -8.8; 332 -8.7; 365 -8.5; 402 -8.1; 442 -7.5; 486 -6.6; 535 -5.5; 588 -4.2; 647 -3.0; 712 -1.8; 783 -0.6; 861 -0.5; 947 -0.5; 1042 -1.7; 1146 -2.7; 1261 -3.8; 1387 -4.8; 1526 -6.2; 1678 -7.8; 1846 -9.1; 2031 -9.3; 2234 -8.6; 2457 -7.2; 2703 -6.1; 2973 -5.8; 3270 -6.5; 3597 -8.5; 3957 -10.8; 4353 -11.0; 4788 -8.2; 5267 -4.8; 5793 -3.7; 6373 -7.3; 7010 -6.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 1.36 | 7.1 dB  |
| Peaking | 32 Hz   | 1.59 | -2.3 dB |
| Peaking | 292 Hz  | 0.1  | -3.6 dB |
| Peaking | 874 Hz  | 1.04 | 9.7 dB  |
| Peaking | 1905 Hz | 4.21 | -2.9 dB |
| Peaking | 111 Hz  | 3.24 | -0.7 dB |
| Peaking | 182 Hz  | 3.08 | 0.7 dB  |
| Peaking | 3021 Hz | 3.94 | 2.6 dB  |
| Peaking | 4195 Hz | 3.32 | -4.9 dB |
| Peaking | 5515 Hz | 5.38 | 4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)