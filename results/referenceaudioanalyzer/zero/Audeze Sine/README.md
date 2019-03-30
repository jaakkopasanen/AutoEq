# Audeze Sine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.7; 25 -3.7; 28 -3.9; 31 -4.0; 34 -3.9; 37 -3.8; 41 -3.6; 45 -3.5; 49 -3.4; 54 -3.3; 60 -2.7; 66 -2.4; 72 -2.7; 79 -3.3; 87 -3.5; 96 -3.8; 106 -3.8; 116 -4.0; 128 -4.1; 141 -3.8; 155 -3.5; 170 -3.2; 187 -3.1; 206 -3.2; 227 -3.4; 249 -3.0; 274 -2.7; 302 -2.4; 332 -2.0; 365 -1.5; 402 -1.2; 442 -1.1; 486 -0.9; 535 -0.6; 588 -0.5; 647 -0.7; 712 -1.1; 783 -1.4; 861 -2.1; 947 -3.3; 1042 -4.2; 1146 -4.4; 1261 -4.6; 1387 -5.1; 1526 -5.7; 1678 -5.7; 1846 -5.1; 2031 -4.5; 2234 -4.3; 2457 -4.1; 2703 -4.2; 2973 -5.1; 3270 -6.2; 3597 -6.8; 3957 -7.3; 4353 -8.5; 4788 -9.7; 5267 -10.0; 5793 -9.8; 6373 -9.2; 7010 -7.5; 7711 -4.5; 8482 -4.1; 9330 -4.1; 10263 -7.3; 11289 -12.4; 12418 -14.8; 13660 -14.1; 15026 -11.2; 16529 -8.6; 18182 -6.7; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 64 Hz    | 2.75 | 1.6 dB   |
| Peaking | 587 Hz   | 0.76 | 3.9 dB   |
| Peaking | 1313 Hz  | 1.36 | -2.4 dB  |
| Peaking | 5108 Hz  | 2.11 | -6.0 dB  |
| Peaking | 13356 Hz | 1.59 | -11.4 dB |
| Peaking | 6513 Hz  | 3.63 | -3.1 dB  |
| Peaking | 9185 Hz  | 1.44 | 4.3 dB   |
| Peaking | 11499 Hz | 3.72 | -4.7 dB  |
| Peaking | 16406 Hz | 3.45 | -1.4 dB  |
| Peaking | 17845 Hz | 2.07 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB   |
| Peaking | 125 Hz   | 1.41 | -0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB   |
| Peaking | 500 Hz   | 1.41 | 4.1 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | -4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -10.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audeze%20Sine/Audeze%20Sine.png)