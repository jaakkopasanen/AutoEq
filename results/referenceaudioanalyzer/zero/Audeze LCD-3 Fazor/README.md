# Audeze LCD-3 Fazor
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.3; 25 -6.4; 28 -7.0; 31 -7.9; 34 -8.6; 37 -9.0; 41 -9.0; 45 -9.0; 49 -9.2; 54 -9.3; 60 -9.3; 66 -9.3; 72 -9.3; 79 -9.2; 87 -9.2; 96 -9.2; 106 -9.1; 116 -9.1; 128 -9.1; 141 -9.3; 155 -9.3; 170 -9.3; 187 -9.3; 206 -9.3; 227 -9.3; 249 -9.3; 274 -9.1; 302 -9.2; 332 -9.3; 365 -9.0; 402 -8.3; 442 -7.5; 486 -7.3; 535 -7.9; 588 -8.5; 647 -8.9; 712 -8.7; 783 -8.3; 861 -7.6; 947 -6.9; 1042 -6.7; 1146 -7.0; 1261 -6.9; 1387 -6.7; 1526 -6.4; 1678 -5.4; 1846 -3.7; 2031 -2.2; 2234 -1.4; 2457 -0.6; 2703 -0.5; 2973 -1.7; 3270 -4.6; 3597 -5.9; 3957 -6.4; 4353 -7.0; 4788 -6.8; 5267 -5.4; 5793 -5.9; 6373 -8.0; 7010 -7.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -7.0; 12418 -9.6; 13660 -9.9; 15026 -9.1; 16529 -8.0; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 Fazor GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 Fazor ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 122 Hz   | 0.25 | -2.9 dB |
| Peaking | 1409 Hz  | 0.55 | -1.4 dB |
| Peaking | 2590 Hz  | 1.39 | 8.5 dB  |
| Peaking | 3631 Hz  | 1.92 | -3.2 dB |
| Peaking | 13875 Hz | 1.81 | -3.7 dB |
| Peaking | 24 Hz    | 2.69 | 1.3 dB  |
| Peaking | 478 Hz   | 3.49 | 2.1 dB  |
| Peaking | 801 Hz   | 0.77 | -1.8 dB |
| Peaking | 971 Hz   | 2.36 | 2.4 dB  |
| Peaking | 1979 Hz  | 6.08 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audeze%20LCD-3%20Fazor/Audeze%20LCD-3%20Fazor.png)