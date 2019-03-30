# Denon AH-D1100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.2; 23 -14.5; 25 -14.8; 28 -15.1; 31 -15.3; 34 -15.5; 37 -15.6; 41 -15.7; 45 -15.9; 49 -15.9; 54 -15.9; 60 -15.7; 66 -15.6; 72 -15.4; 79 -15.2; 87 -14.9; 96 -14.7; 106 -14.4; 116 -14.2; 128 -14.0; 141 -14.2; 155 -14.6; 170 -14.9; 187 -14.9; 206 -14.9; 227 -14.6; 249 -13.9; 274 -13.0; 302 -11.7; 332 -10.0; 365 -7.9; 402 -5.7; 442 -3.7; 486 -2.3; 535 -2.2; 588 -2.9; 647 -3.9; 712 -4.8; 783 -5.4; 861 -5.5; 947 -5.2; 1042 -4.6; 1146 -4.0; 1261 -3.4; 1387 -2.9; 1526 -2.4; 1678 -2.0; 1846 -1.5; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -2.4; 3597 -4.4; 3957 -5.1; 4353 -7.0; 4788 -10.0; 5267 -12.8; 5793 -12.9; 6373 -8.3; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -8.0; 12418 -8.1; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D1100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.43 | -6.4 dB  |
| Peaking | 100 Hz   | 0.41 | -6.6 dB  |
| Peaking | 231 Hz   | 1.33 | -7.3 dB  |
| Peaking | 1044 Hz  | 0.15 | 4.7 dB   |
| Peaking | 5411 Hz  | 3.34 | -10.5 dB |
| Peaking | 324 Hz   | 3.79 | -1.7 dB  |
| Peaking | 500 Hz   | 2.11 | 3.8 dB   |
| Peaking | 848 Hz   | 1.41 | -3.5 dB  |
| Peaking | 2471 Hz  | 2.14 | 2.8 dB   |
| Peaking | 11910 Hz | 3.09 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.9 dB |
| Peaking | 62 Hz    | 1.41 | -6.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -8.1 dB |
| Peaking | 500 Hz   | 1.41 | 5.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Denon%20AH-D1100/Denon%20AH-D1100.png)