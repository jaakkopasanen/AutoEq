# ADVANCED M4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.1; 49 -1.7; 54 -2.2; 60 -2.7; 66 -3.2; 72 -3.6; 79 -4.0; 87 -4.4; 96 -4.8; 106 -5.1; 116 -5.3; 128 -5.3; 141 -5.6; 155 -5.6; 170 -5.5; 187 -5.2; 206 -4.9; 227 -4.6; 249 -4.8; 274 -5.4; 302 -5.6; 332 -5.6; 365 -5.4; 402 -5.2; 442 -4.9; 486 -4.6; 535 -4.3; 588 -4.1; 647 -3.9; 712 -3.7; 783 -3.4; 861 -3.3; 947 -3.3; 1042 -3.3; 1146 -3.3; 1261 -3.3; 1387 -3.3; 1526 -3.6; 1678 -4.1; 1846 -5.2; 2031 -6.6; 2234 -8.2; 2457 -10.4; 2703 -13.4; 2973 -15.9; 3270 -16.3; 3597 -14.6; 3957 -12.0; 4353 -10.7; 4788 -10.1; 5267 -9.3; 5793 -9.2; 6373 -10.5; 7010 -11.2; 7711 -9.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ADVANCED M4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ADVANCED M4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.55 | 6.4 dB   |
| Peaking | 1295 Hz | 0.4  | 3.7 dB   |
| Peaking | 1647 Hz | 1.49 | 1.4 dB   |
| Peaking | 3133 Hz | 1.61 | -12.5 dB |
| Peaking | 6874 Hz | 4.18 | -4.3 dB  |
| Peaking | 143 Hz  | 1.5  | -0.3 dB  |
| Peaking | 230 Hz  | 2.51 | 1.3 dB   |
| Peaking | 312 Hz  | 2.17 | -0.7 dB  |
| Peaking | 7644 Hz | 7.59 | -1.5 dB  |
| Peaking | 8512 Hz | 3.39 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | -8.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/ADVANCED%20M4/ADVANCED%20M4.png)