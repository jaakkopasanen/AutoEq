# Denon AH-D2000 Snorry Mod
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.5; 23 -14.7; 25 -14.8; 28 -14.9; 31 -15.0; 34 -15.0; 37 -15.0; 41 -14.9; 45 -14.7; 49 -14.6; 54 -14.4; 60 -14.2; 66 -14.2; 72 -14.0; 79 -13.9; 87 -13.7; 96 -13.6; 106 -13.4; 116 -13.1; 128 -12.9; 141 -12.7; 155 -12.5; 170 -12.2; 187 -11.9; 206 -11.5; 227 -11.1; 249 -10.6; 274 -10.0; 302 -9.4; 332 -8.6; 365 -7.4; 402 -5.9; 442 -4.1; 486 -2.6; 535 -2.4; 588 -2.6; 647 -2.5; 712 -2.7; 783 -3.4; 861 -4.5; 947 -5.3; 1042 -5.6; 1146 -5.4; 1261 -4.7; 1387 -3.7; 1526 -2.8; 1678 -2.1; 1846 -1.9; 2031 -1.9; 2234 -1.3; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.3; 3597 -4.3; 3957 -7.1; 4353 -9.8; 4788 -13.0; 5267 -14.6; 5793 -13.2; 6373 -9.6; 7010 -7.7; 7711 -7.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D2000 Snorry Mod GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 Snorry Mod ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 27 Hz   | 0.09 | -8.0 dB  |
| Peaking | 543 Hz  | 1.47 | 6.3 dB   |
| Peaking | 2744 Hz | 0.91 | 7.4 dB   |
| Peaking | 5092 Hz | 2.24 | -11.3 dB |
| Peaking | 766 Hz  | 4.04 | 1.6 dB   |
| Peaking | 1258 Hz | 0.98 | -1.7 dB  |
| Peaking | 1513 Hz | 2.59 | 2.2 dB   |
| Peaking | 5841 Hz | 8.25 | -1.7 dB  |
| Peaking | 7174 Hz | 1.58 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | 5.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Denon%20AH-D2000%20Snorry%20Mod/Denon%20AH-D2000%20Snorry%20Mod.png)