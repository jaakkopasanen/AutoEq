# Denon AH-D1001
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.1; 72 -1.6; 79 -2.2; 87 -2.9; 96 -3.6; 106 -4.1; 116 -4.2; 128 -4.4; 141 -4.4; 155 -4.1; 170 -3.5; 187 -3.0; 206 -2.6; 227 -2.5; 249 -2.6; 274 -2.6; 302 -2.5; 332 -2.6; 365 -3.1; 402 -3.8; 442 -4.4; 486 -4.8; 535 -5.7; 588 -6.8; 647 -7.9; 712 -8.7; 783 -9.1; 861 -9.4; 947 -9.2; 1042 -8.6; 1146 -8.1; 1261 -8.1; 1387 -8.0; 1526 -7.7; 1678 -7.4; 1846 -6.9; 2031 -6.0; 2234 -5.5; 2457 -5.7; 2703 -6.7; 2973 -7.0; 3270 -6.5; 3597 -6.7; 3957 -6.7; 4353 -5.9; 4788 -5.4; 5267 -7.0; 5793 -9.5; 6373 -10.2; 7010 -9.7; 7711 -10.8; 8482 -13.4; 9330 -16.1; 10263 -17.1; 11289 -16.5; 12418 -15.8; 13660 -15.5; 15026 -14.4; 16529 -11.5; 18182 -8.6; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D1001 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.5  | 6.5 dB   |
| Peaking | 307 Hz   | 0.89 | 4.2 dB   |
| Peaking | 843 Hz   | 1.2  | -3.8 dB  |
| Peaking | 5638 Hz  | 0.61 | 4.7 dB   |
| Peaking | 10812 Hz | 0.56 | -12.4 dB |
| Peaking | 123 Hz   | 3.97 | -0.7 dB  |
| Peaking | 2253 Hz  | 3.97 | 1.9 dB   |
| Peaking | 4253 Hz  | 0.65 | -2.2 dB  |
| Peaking | 5550 Hz  | 1.41 | 4.8 dB   |
| Peaking | 5887 Hz  | 4.39 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB   |
| Peaking | 62 Hz    | 1.41 | 4.6 dB   |
| Peaking | 125 Hz   | 1.41 | 0.3 dB   |
| Peaking | 250 Hz   | 1.41 | 4.4 dB   |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -8.0 dB  |
| Peaking | 16000 Hz | 1.41 | -10.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Denon%20AH-D1001/Denon%20AH-D1001.png)