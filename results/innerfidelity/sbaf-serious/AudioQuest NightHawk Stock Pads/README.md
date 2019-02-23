# AudioQuest NightHawk Stock Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -8.9; 25 -8.9; 28 -8.9; 31 -8.8; 34 -8.8; 37 -8.7; 41 -8.7; 45 -8.7; 49 -8.7; 54 -8.6; 60 -8.6; 66 -8.7; 72 -8.8; 79 -9.1; 87 -9.7; 96 -10.6; 106 -11.4; 116 -11.0; 128 -11.7; 141 -12.2; 155 -12.1; 170 -11.7; 187 -12.3; 206 -12.3; 227 -12.2; 249 -12.1; 274 -11.9; 302 -11.6; 332 -11.3; 365 -10.9; 402 -10.3; 442 -9.6; 486 -9.0; 535 -8.2; 588 -7.1; 647 -6.1; 712 -5.2; 783 -4.4; 861 -3.6; 947 -2.6; 1042 -2.5; 1146 -3.1; 1261 -3.4; 1387 -5.1; 1526 -6.3; 1678 -6.7; 1846 -6.3; 2031 -5.3; 2234 -4.4; 2457 -2.4; 2703 -0.5; 2973 -0.5; 3270 -1.9; 3597 -2.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.6; 6373 -3.0; 7010 -4.3; 7711 -6.2; 8482 -7.1; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AudioQuest NightHawk Stock Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioQuest NightHawk Stock Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  1.01 | -2.2 dB |
| Peaking | 205 Hz  |  0.47 | -6.0 dB |
| Peaking | 940 Hz  |  1.71 | 5.2 dB  |
| Peaking | 2805 Hz |  3.57 | 5.2 dB  |
| Peaking | 4688 Hz |  1.83 | 6.3 dB  |
| Peaking | 1239 Hz |  5.47 | 1.4 dB  |
| Peaking | 1631 Hz |  3.23 | -1.6 dB |
| Peaking | 2512 Hz | 10.63 | 0.9 dB  |
| Peaking | 6590 Hz |  5.24 | 1.4 dB  |
| Peaking | 8650 Hz |  2.86 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioQuest%20NightHawk%20Stock%20Pads/AudioQuest%20NightHawk%20Stock%20Pads.png)