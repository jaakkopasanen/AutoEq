# Bluedio T4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -10.2; 25 -9.5; 28 -8.6; 31 -7.6; 34 -6.7; 37 -5.8; 41 -4.9; 45 -4.1; 49 -3.4; 54 -2.7; 60 -2.0; 66 -1.5; 72 -1.0; 79 -0.7; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.6; 783 -3.1; 861 -4.8; 947 -6.3; 1042 -7.0; 1146 -8.8; 1261 -8.5; 1387 -7.1; 1526 -7.0; 1678 -7.7; 1846 -8.7; 2031 -9.4; 2234 -9.8; 2457 -8.7; 2703 -7.3; 2973 -6.6; 3270 -5.9; 3597 -5.1; 3957 -5.6; 4353 -8.2; 4788 -7.8; 5267 -7.1; 5793 -7.7; 6373 -5.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.78 | -7.6 dB |
| Peaking | 94 Hz   | 0.22 | 6.5 dB  |
| Peaking | 670 Hz  | 0.85 | 5.1 dB  |
| Peaking | 1081 Hz | 1.67 | -5.3 dB |
| Peaking | 2140 Hz | 3.32 | -3.8 dB |
| Peaking | 80 Hz   | 3.25 | 0.4 dB  |
| Peaking | 142 Hz  | 2.46 | -0.3 dB |
| Peaking | 3797 Hz | 3.59 | 4.2 dB  |
| Peaking | 4260 Hz | 2.27 | -3.4 dB |
| Peaking | 6777 Hz | 7.99 | 3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 4.9 dB  |
| Peaking | 250 Hz   | 1.41 | 4.2 dB  |
| Peaking | 500 Hz   | 1.41 | 6.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20T4/Bluedio%20T4.png)