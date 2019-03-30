# Monoprice 8320
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.7; 28 -0.8; 31 -0.8; 34 -0.9; 37 -0.9; 41 -1.0; 45 -1.1; 49 -1.2; 54 -1.2; 60 -1.2; 66 -1.2; 72 -1.2; 79 -1.2; 87 -1.2; 96 -1.2; 106 -1.2; 116 -1.2; 128 -1.2; 141 -1.2; 155 -1.4; 170 -1.5; 187 -1.5; 206 -1.5; 227 -1.5; 249 -1.5; 274 -1.8; 302 -2.0; 332 -2.2; 365 -2.5; 402 -2.7; 442 -2.9; 486 -3.1; 535 -3.4; 588 -3.5; 647 -3.7; 712 -3.9; 783 -4.3; 861 -4.6; 947 -5.1; 1042 -5.6; 1146 -6.1; 1261 -6.8; 1387 -7.7; 1526 -8.9; 1678 -10.5; 1846 -12.6; 2031 -14.9; 2234 -16.3; 2457 -15.8; 2703 -13.6; 2973 -11.0; 3270 -9.0; 3597 -7.6; 3957 -7.1; 4353 -7.6; 4788 -7.3; 5267 -6.2; 5793 -5.1; 6373 -2.6; 7010 -1.9; 7711 -4.2; 8482 -4.4; 9330 -4.4; 10263 -4.4; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice 8320 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice 8320 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 16 Hz   | 0.41 | 3.5 dB   |
| Peaking | 151 Hz  | 0.31 | 3.0 dB   |
| Peaking | 2261 Hz | 1.65 | -12.4 dB |
| Peaking | 4799 Hz | 3.91 | -1.5 dB  |
| Peaking | 6680 Hz | 5.52 | 4.2 dB   |
| Peaking | 3481 Hz | 1.71 | -0.8 dB  |
| Peaking | 3586 Hz | 3.62 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB   |
| Peaking | 62 Hz    | 1.41 | 2.3 dB   |
| Peaking | 125 Hz   | 1.41 | 2.6 dB   |
| Peaking | 250 Hz   | 1.41 | 2.4 dB   |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.1 dB |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Monoprice%208320/Monoprice%208320.png)