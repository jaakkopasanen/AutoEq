# HiFiMan HE-300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.0; 45 -2.0; 49 -2.9; 54 -3.8; 60 -4.6; 66 -5.3; 72 -5.8; 79 -6.2; 87 -6.5; 96 -6.8; 106 -6.8; 116 -7.0; 128 -7.1; 141 -7.4; 155 -7.4; 170 -7.4; 187 -7.3; 206 -7.2; 227 -7.6; 249 -8.0; 274 -8.1; 302 -7.8; 332 -7.7; 365 -7.5; 402 -7.2; 442 -7.1; 486 -7.1; 535 -7.1; 588 -7.1; 647 -6.7; 712 -5.8; 783 -5.2; 861 -5.4; 947 -5.1; 1042 -4.7; 1146 -4.5; 1261 -4.5; 1387 -4.5; 1526 -4.3; 1678 -4.0; 1846 -4.5; 2031 -5.8; 2234 -6.9; 2457 -7.8; 2703 -8.5; 2973 -8.9; 3270 -8.9; 3597 -8.7; 3957 -8.9; 4353 -10.4; 4788 -11.8; 5267 -11.7; 5793 -9.5; 6373 -6.6; 7010 -5.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan HE-300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan HE-300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.69 | 7.4 dB  |
| Peaking | 193 Hz  | 0.16 | -1.8 dB |
| Peaking | 2275 Hz | 0.44 | 5.8 dB  |
| Peaking | 2864 Hz | 1.2  | -7.2 dB |
| Peaking | 4968 Hz | 2.86 | -7.1 dB |
| Peaking | 202 Hz  | 3.55 | 0.7 dB  |
| Peaking | 264 Hz  | 4.24 | -0.6 dB |
| Peaking | 593 Hz  | 7.24 | -0.6 dB |
| Peaking | 6940 Hz | 5.66 | 2.3 dB  |
| Peaking | 7903 Hz | 1.05 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/HiFiMan%20HE-300/HiFiMan%20HE-300.png)