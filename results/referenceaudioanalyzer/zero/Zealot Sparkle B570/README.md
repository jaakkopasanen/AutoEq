# Zealot Sparkle B570
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -5.3; 25 -6.4; 28 -8.0; 31 -9.5; 34 -10.9; 37 -12.1; 41 -13.5; 45 -14.6; 49 -15.5; 54 -16.2; 60 -16.6; 66 -16.7; 72 -16.5; 79 -16.3; 87 -16.1; 96 -15.8; 106 -15.4; 116 -15.2; 128 -14.9; 141 -14.7; 155 -14.5; 170 -14.4; 187 -14.3; 206 -14.1; 227 -13.8; 249 -13.3; 274 -12.8; 302 -12.7; 332 -12.7; 365 -12.8; 402 -12.6; 442 -12.3; 486 -12.0; 535 -11.9; 588 -12.1; 647 -11.8; 712 -11.5; 783 -11.1; 861 -10.6; 947 -10.4; 1042 -10.7; 1146 -11.4; 1261 -11.9; 1387 -11.3; 1526 -9.4; 1678 -6.5; 1846 -3.3; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.3; 3957 -2.9; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zealot Sparkle B570 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zealot Sparkle B570 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 64 Hz   | 0.89 | -7.0 dB |
| Peaking | 262 Hz  | 0.24 | -6.5 dB |
| Peaking | 1380 Hz | 1.84 | -7.3 dB |
| Peaking | 2219 Hz | 0.96 | 9.1 dB  |
| Peaking | 5439 Hz | 2.34 | 5.3 dB  |
| Peaking | 19 Hz   | 1.47 | 4.8 dB  |
| Peaking | 40 Hz   | 2.26 | -1.6 dB |
| Peaking | 294 Hz  | 5.15 | 0.7 dB  |
| Peaking | 6518 Hz | 6.33 | 2.5 dB  |
| Peaking | 7821 Hz | 2.02 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -10.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | -3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Zealot%20Sparkle%20B570/Zealot%20Sparkle%20B570.png)