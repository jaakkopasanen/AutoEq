# Sunrise Xcited
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.5; 31 -1.6; 34 -1.6; 37 -1.6; 41 -1.6; 45 -1.6; 49 -1.6; 54 -1.7; 60 -1.6; 66 -1.4; 72 -1.5; 79 -1.8; 87 -2.1; 96 -2.2; 106 -2.0; 116 -1.8; 128 -1.6; 141 -1.6; 155 -1.6; 170 -1.6; 187 -1.6; 206 -1.6; 227 -1.8; 249 -2.2; 274 -2.7; 302 -3.1; 332 -3.0; 365 -2.9; 402 -2.8; 442 -2.6; 486 -2.6; 535 -2.6; 588 -2.6; 647 -2.4; 712 -2.3; 783 -2.3; 861 -2.1; 947 -1.9; 1042 -2.0; 1146 -2.0; 1261 -2.0; 1387 -2.0; 1526 -2.2; 1678 -2.5; 1846 -2.8; 2031 -3.2; 2234 -3.6; 2457 -4.3; 2703 -5.3; 2973 -6.7; 3270 -8.3; 3597 -10.4; 3957 -12.9; 4353 -16.5; 4788 -20.4; 5267 -22.6; 5793 -23.5; 6373 -23.4; 7010 -21.7; 7711 -17.4; 8482 -13.8; 9330 -13.4; 10263 -15.4; 11289 -17.3; 12418 -16.2; 13660 -10.3; 15026 -6.2; 16529 -6.2; 18182 -8.9; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sunrise Xcited GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sunrise Xcited ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.1  | 4.5 dB   |
| Peaking | 768 Hz   | 0.18 | 2.5 dB   |
| Peaking | 2708 Hz  | 0.47 | 9.0 dB   |
| Peaking | 5584 Hz  | 0.77 | -24.2 dB |
| Peaking | 20533 Hz | 1.83 | -9.3 dB  |
| Peaking | 197 Hz   | 4.03 | 0.6 dB   |
| Peaking | 6968 Hz  | 5.46 | -2.9 dB  |
| Peaking | 8848 Hz  | 2.19 | 5.1 dB   |
| Peaking | 11939 Hz | 1.65 | -7.8 dB  |
| Peaking | 14642 Hz | 1.72 | 6.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB   |
| Peaking | 62 Hz    | 1.41 | 3.2 dB   |
| Peaking | 125 Hz   | 1.41 | 3.5 dB   |
| Peaking | 250 Hz   | 1.41 | 2.9 dB   |
| Peaking | 500 Hz   | 1.41 | 2.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -15.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sunrise%20Xcited/Sunrise%20Xcited.png)