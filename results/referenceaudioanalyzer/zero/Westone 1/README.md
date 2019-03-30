# Westone 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.5; 25 -6.8; 28 -7.3; 31 -7.6; 34 -7.8; 37 -8.0; 41 -8.3; 45 -8.4; 49 -8.5; 54 -8.6; 60 -8.8; 66 -8.8; 72 -8.9; 79 -9.1; 87 -9.1; 96 -9.1; 106 -9.1; 116 -9.1; 128 -9.1; 141 -9.1; 155 -9.1; 170 -9.4; 187 -9.6; 206 -9.8; 227 -9.8; 249 -9.5; 274 -9.4; 302 -9.4; 332 -9.3; 365 -9.1; 402 -9.1; 442 -9.2; 486 -9.4; 535 -9.4; 588 -9.2; 647 -9.1; 712 -8.9; 783 -8.8; 861 -8.8; 947 -8.7; 1042 -8.8; 1146 -8.8; 1261 -8.8; 1387 -8.8; 1526 -8.8; 1678 -8.8; 1846 -8.7; 2031 -8.4; 2234 -8.0; 2457 -7.3; 2703 -6.6; 2973 -7.1; 3270 -8.1; 3597 -7.8; 3957 -6.5; 4353 -4.5; 4788 -1.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 74 Hz   | 0.6  | -2.2 dB |
| Peaking | 219 Hz  | 1.11 | -1.7 dB |
| Peaking | 510 Hz  | 1.52 | -0.7 dB |
| Peaking | 1685 Hz | 0.17 | -2.2 dB |
| Peaking | 5571 Hz | 2.07 | 8.5 dB  |
| Peaking | 2697 Hz | 5.45 | 1.6 dB  |
| Peaking | 3487 Hz | 5.43 | -1.5 dB |
| Peaking | 6603 Hz | 9.89 | 1.6 dB  |
| Peaking | 7657 Hz | 5.1  | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Westone%201/Westone%201.png)