# Marantz MPH-4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.0; 31 -1.8; 34 -2.6; 37 -3.2; 41 -4.0; 45 -4.5; 49 -4.8; 54 -5.3; 60 -5.7; 66 -6.3; 72 -6.8; 79 -7.3; 87 -7.3; 96 -6.7; 106 -6.1; 116 -5.8; 128 -5.8; 141 -5.8; 155 -5.7; 170 -5.3; 187 -5.0; 206 -4.7; 227 -4.5; 249 -4.3; 274 -4.5; 302 -4.7; 332 -5.0; 365 -5.2; 402 -5.5; 442 -5.7; 486 -5.8; 535 -6.0; 588 -6.1; 647 -6.3; 712 -6.5; 783 -6.5; 861 -6.3; 947 -5.7; 1042 -5.5; 1146 -5.8; 1261 -5.9; 1387 -5.8; 1526 -5.8; 1678 -5.6; 1846 -4.9; 2031 -4.1; 2234 -3.9; 2457 -4.4; 2703 -5.3; 2973 -5.9; 3270 -5.7; 3597 -6.1; 3957 -6.7; 4353 -7.4; 4788 -11.3; 5267 -13.8; 5793 -14.8; 6373 -14.5; 7010 -12.8; 7711 -10.0; 8482 -7.2; 9330 -6.5; 10263 -8.3; 11289 -13.4; 12418 -16.6; 13660 -14.1; 15026 -8.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marantz MPH-4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marantz MPH-4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 1.37 | 6.4 dB   |
| Peaking | 255 Hz   | 1.41 | 2.2 dB   |
| Peaking | 2477 Hz  | 0.96 | 2.4 dB   |
| Peaking | 5858 Hz  | 2.39 | -9.5 dB  |
| Peaking | 12634 Hz | 2.99 | -11.1 dB |
| Peaking | 70 Hz    | 0.67 | 0.8 dB   |
| Peaking | 80 Hz    | 2.47 | -2.2 dB  |
| Peaking | 1555 Hz  | 5.44 | -0.4 dB  |
| Peaking | 9318 Hz  | 3.15 | 5.9 dB   |
| Peaking | 9529 Hz  | 1.4  | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 2.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Marantz%20MPH-4/Marantz%20MPH-4.png)