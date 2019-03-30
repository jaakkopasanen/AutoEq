# Denon AH-D5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -8.5; 25 -9.2; 28 -10.0; 31 -10.6; 34 -10.9; 37 -11.1; 41 -11.2; 45 -11.2; 49 -11.1; 54 -10.9; 60 -10.8; 66 -10.8; 72 -10.6; 79 -10.4; 87 -10.2; 96 -9.9; 106 -9.7; 116 -9.4; 128 -9.1; 141 -8.9; 155 -8.6; 170 -8.3; 187 -8.0; 206 -7.7; 227 -7.3; 249 -7.0; 274 -6.7; 302 -6.3; 332 -6.0; 365 -5.5; 402 -5.1; 442 -4.8; 486 -4.6; 535 -4.7; 588 -5.2; 647 -5.8; 712 -6.3; 783 -6.1; 861 -5.4; 947 -5.2; 1042 -5.6; 1146 -5.6; 1261 -5.3; 1387 -4.8; 1526 -4.1; 1678 -3.3; 1846 -2.6; 2031 -1.8; 2234 -0.8; 2457 -0.5; 2703 -1.6; 2973 -3.5; 3270 -5.5; 3597 -7.1; 3957 -8.4; 4353 -9.4; 4788 -11.0; 5267 -12.6; 5793 -13.3; 6373 -12.4; 7010 -10.1; 7711 -6.5; 8482 -6.2; 9330 -6.2; 10263 -6.3; 11289 -7.4; 12418 -10.0; 13660 -9.0; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 54 Hz    | 0.41 | -4.8 dB |
| Peaking | 452 Hz   | 1.76 | 2.0 dB  |
| Peaking | 2317 Hz  | 1.76 | 6.3 dB  |
| Peaking | 5491 Hz  | 2.02 | -7.8 dB |
| Peaking | 12779 Hz | 4.74 | -4.3 dB |
| Peaking | 78 Hz    | 2.16 | 0.2 dB  |
| Peaking | 166 Hz   | 2.69 | -0.2 dB |
| Peaking | 3877 Hz  | 4.79 | -1.3 dB |
| Peaking | 6544 Hz  | 4.07 | -4.2 dB |
| Peaking | 7499 Hz  | 1.78 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Denon%20AH-D5000/Denon%20AH-D5000.png)