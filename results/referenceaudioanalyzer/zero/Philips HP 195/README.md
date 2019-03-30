# Philips HP 195
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.0; 54 -2.0; 60 -3.1; 66 -4.0; 72 -4.9; 79 -5.9; 87 -6.9; 96 -8.0; 106 -9.1; 116 -9.9; 128 -10.3; 141 -10.6; 155 -10.5; 170 -10.2; 187 -9.6; 206 -9.0; 227 -8.3; 249 -7.6; 274 -7.0; 302 -6.3; 332 -5.7; 365 -5.1; 402 -4.5; 442 -3.8; 486 -3.3; 535 -2.8; 588 -2.2; 647 -1.5; 712 -0.8; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -2.1; 1146 -5.3; 1261 -8.2; 1387 -10.0; 1526 -10.7; 1678 -10.3; 1846 -8.7; 2031 -6.4; 2234 -4.4; 2457 -3.2; 2703 -2.8; 2973 -3.1; 3270 -3.7; 3597 -5.0; 3957 -5.4; 4353 -3.7; 4788 -3.3; 5267 -8.9; 5793 -12.8; 6373 -13.4; 7010 -11.2; 7711 -9.0; 8482 -9.2; 9330 -10.8; 10263 -11.7; 11289 -11.5; 12418 -10.5; 13660 -7.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips HP 195 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips HP 195 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 1.38 | 7.4 dB   |
| Peaking | 1571 Hz  | 1.95 | -14.7 dB |
| Peaking | 1629 Hz  | 0.46 | 9.7 dB   |
| Peaking | 7604 Hz  | 0.72 | -6.4 dB  |
| Peaking | 22050 Hz | 2.09 | -3.9 dB  |
| Peaking | 154 Hz   | 1.33 | -5.1 dB  |
| Peaking | 763 Hz   | 2.36 | 2.4 dB   |
| Peaking | 4700 Hz  | 4.27 | 7.5 dB   |
| Peaking | 6432 Hz  | 1.26 | -7.1 dB  |
| Peaking | 7719 Hz  | 2.83 | 8.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.2 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 4.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20HP%20195/Philips%20HP%20195.png)