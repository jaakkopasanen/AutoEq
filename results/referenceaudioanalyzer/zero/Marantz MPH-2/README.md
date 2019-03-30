# Marantz MPH-2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.9; 25 -13.2; 28 -13.6; 31 -13.8; 34 -13.9; 37 -13.9; 41 -13.6; 45 -13.3; 49 -13.0; 54 -12.6; 60 -12.4; 66 -12.5; 72 -12.7; 79 -12.9; 87 -13.2; 96 -13.2; 106 -13.0; 116 -13.0; 128 -13.0; 141 -13.0; 155 -12.9; 170 -12.7; 187 -12.3; 206 -11.7; 227 -10.6; 249 -9.5; 274 -8.4; 302 -7.1; 332 -5.4; 365 -3.7; 402 -2.5; 442 -1.7; 486 -1.6; 535 -1.9; 588 -2.7; 647 -3.4; 712 -3.9; 783 -3.9; 861 -3.7; 947 -3.4; 1042 -3.2; 1146 -2.9; 1261 -2.9; 1387 -2.9; 1526 -2.7; 1678 -2.3; 1846 -1.9; 2031 -1.2; 2234 -0.5; 2457 -0.7; 2703 -2.0; 2973 -3.0; 3270 -2.9; 3597 -2.2; 3957 -1.7; 4353 -0.9; 4788 -2.5; 5267 -7.0; 5793 -12.4; 6373 -13.3; 7010 -9.4; 7711 -5.2; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -6.2; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marantz MPH-2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marantz MPH-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.27 | -8.1 dB  |
| Peaking | 174 Hz  | 1.07 | -6.6 dB  |
| Peaking | 977 Hz  | 0.14 | 3.6 dB   |
| Peaking | 4496 Hz | 3.34 | 4.1 dB   |
| Peaking | 6094 Hz | 3.23 | -11.4 dB |
| Peaking | 277 Hz  | 2.44 | -1.8 dB  |
| Peaking | 459 Hz  | 1.49 | 3.5 dB   |
| Peaking | 735 Hz  | 1.16 | -2.3 dB  |
| Peaking | 2320 Hz | 3.26 | 3.1 dB   |
| Peaking | 2430 Hz | 1.23 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 4.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Marantz%20MPH-2/Marantz%20MPH-2.png)