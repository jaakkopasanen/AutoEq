# Bluedio T4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -12.8; 25 -12.1; 28 -11.1; 31 -10.2; 34 -9.3; 37 -8.5; 41 -7.5; 45 -6.7; 49 -6.0; 54 -5.3; 60 -4.6; 66 -4.1; 72 -3.7; 79 -3.3; 87 -3.0; 96 -2.8; 106 -2.6; 116 -2.5; 128 -2.3; 141 -2.1; 155 -1.8; 170 -1.3; 187 -0.5; 206 -0.6; 227 -0.7; 249 -1.1; 274 -1.5; 302 -1.7; 332 -1.7; 365 -1.9; 402 -2.1; 442 -2.4; 486 -2.8; 535 -3.0; 588 -3.3; 647 -1.5; 712 -2.2; 783 -6.1; 861 -7.8; 947 -9.2; 1042 -10.0; 1146 -11.7; 1261 -11.4; 1387 -10.1; 1526 -10.1; 1678 -10.7; 1846 -11.8; 2031 -12.7; 2234 -13.4; 2457 -12.4; 2703 -10.6; 2973 -9.5; 3270 -8.5; 3597 -7.6; 3957 -8.2; 4353 -10.6; 4788 -11.0; 5267 -10.4; 5793 -10.3; 6373 -7.1; 7010 -4.5; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.73 | -8.3 dB  |
| Peaking | 550 Hz   | 0.09 | 5.1 dB   |
| Peaking | 1119 Hz  | 1.65 | -8.3 dB  |
| Peaking | 2204 Hz  | 1.37 | -10.3 dB |
| Peaking | 4974 Hz  | 2.21 | -6.8 dB  |
| Peaking | 201 Hz   | 4.95 | 1.1 dB   |
| Peaking | 541 Hz   | 1.75 | -1.1 dB  |
| Peaking | 683 Hz   | 6.86 | 4.1 dB   |
| Peaking | 809 Hz   | 5.46 | -1.4 dB  |
| Peaking | 11200 Hz | 2.45 | -0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 3.1 dB  |
| Peaking | 250 Hz   | 1.41 | 4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 4.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.2 dB |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20T4/Bluedio%20T4.png)