# Popclick String
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.8; 23 -14.8; 25 -14.8; 28 -14.7; 31 -14.7; 34 -14.6; 37 -14.5; 41 -14.4; 45 -14.2; 49 -14.2; 54 -14.0; 60 -13.9; 66 -13.9; 72 -13.7; 79 -13.7; 87 -13.6; 96 -13.5; 106 -13.2; 116 -12.9; 128 -12.6; 141 -12.3; 155 -12.0; 170 -11.5; 187 -10.9; 206 -10.4; 227 -9.7; 249 -9.2; 274 -8.5; 302 -7.9; 332 -7.1; 365 -6.5; 402 -5.9; 442 -5.1; 486 -4.8; 535 -4.3; 588 -3.8; 647 -3.6; 712 -3.7; 783 -3.3; 861 -3.2; 947 -3.7; 1042 -4.3; 1146 -4.7; 1261 -5.3; 1387 -6.3; 1526 -7.6; 1678 -8.6; 1846 -9.1; 2031 -9.8; 2234 -10.4; 2457 -10.1; 2703 -8.3; 2973 -5.0; 3270 -2.0; 3597 -0.5; 3957 -1.2; 4353 -4.1; 4788 -6.6; 5267 -10.1; 5793 -12.7; 6373 -6.2; 7010 -2.3; 7711 -3.8; 8482 -4.1; 9330 -4.1; 10263 -4.4; 11289 -4.2; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Popclick String GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Popclick String ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.25 | -10.5 dB |
| Peaking | 150 Hz  | 0.82 | -4.2 dB  |
| Peaking | 2233 Hz | 1.78 | -7.2 dB  |
| Peaking | 3564 Hz | 3.23 | 6.1 dB   |
| Peaking | 5577 Hz | 5.97 | -9.8 dB  |
| Peaking | 288 Hz  | 2.09 | -1.0 dB  |
| Peaking | 749 Hz  | 1.07 | 1.7 dB   |
| Peaking | 1564 Hz | 3.94 | -1.7 dB  |
| Peaking | 6049 Hz | 6.01 | -1.8 dB  |
| Peaking | 6908 Hz | 5.59 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.1 dB |
| Peaking | 62 Hz    | 1.41 | -7.0 dB  |
| Peaking | 125 Hz   | 1.41 | -7.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Popclick%20String/Popclick%20String.png)