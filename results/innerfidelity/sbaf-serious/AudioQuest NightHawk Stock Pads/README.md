# AudioQuest NightHawk Stock Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.6; 25 -9.6; 28 -9.5; 31 -9.5; 34 -9.4; 37 -9.4; 41 -9.4; 45 -9.3; 49 -9.3; 54 -9.3; 60 -9.3; 66 -9.4; 72 -9.5; 79 -9.8; 87 -10.4; 96 -11.3; 106 -12.0; 116 -11.7; 128 -12.3; 141 -12.9; 155 -12.8; 170 -12.4; 187 -13.0; 206 -12.9; 227 -12.8; 249 -12.8; 274 -12.5; 302 -12.3; 332 -12.0; 365 -11.6; 402 -11.0; 442 -10.2; 486 -9.7; 535 -8.9; 588 -7.7; 647 -6.8; 712 -5.9; 783 -5.0; 861 -4.2; 947 -3.3; 1042 -3.1; 1146 -3.7; 1261 -4.1; 1387 -5.7; 1526 -7.0; 1678 -7.4; 1846 -6.9; 2031 -6.0; 2234 -5.0; 2457 -3.0; 2703 -0.8; 2973 -0.5; 3270 -2.6; 3597 -3.0; 3957 -0.7; 4353 -1.0; 4788 -0.5; 5267 -0.7; 5793 -3.3; 6373 -3.7; 7010 -4.8; 7711 -6.4; 8482 -7.8; 9330 -8.0; 10263 -4.9; 11289 -2.9; 12418 -2.9; 13660 -2.9; 15026 -3.1; 16529 -4.0; 18182 -6.7; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AudioQuest NightHawk Stock Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioQuest NightHawk Stock Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.07 | -5.7 dB |
| Peaking | 370 Hz  | 0.38 | -8.2 dB |
| Peaking | 1367 Hz | 0.39 | 7.9 dB  |
| Peaking | 1738 Hz | 1.43 | -9.9 dB |
| Peaking | 8595 Hz | 2.34 | -6.2 dB |
| Peaking | 25 Hz   | 0.21 | -0.7 dB |
| Peaking | 67 Hz   | 1.87 | 1.4 dB  |
| Peaking | 2903 Hz | 4.48 | 3.7 dB  |
| Peaking | 3393 Hz | 2.08 | -4.0 dB |
| Peaking | 4251 Hz | 2.56 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.5 dB |
| Peaking | 250 Hz   | 1.41 | -8.5 dB |
| Peaking | 500 Hz   | 1.41 | -5.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioQuest%20NightHawk%20Stock%20Pads/AudioQuest%20NightHawk%20Stock%20Pads.png)