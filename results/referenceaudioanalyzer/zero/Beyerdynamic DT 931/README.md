# Beyerdynamic DT 931
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.0; 60 -1.3; 66 -1.6; 72 -1.8; 79 -2.0; 87 -2.3; 96 -2.7; 106 -3.1; 116 -3.4; 128 -3.6; 141 -3.9; 155 -4.0; 170 -4.0; 187 -4.0; 206 -4.0; 227 -4.3; 249 -4.3; 274 -4.3; 302 -4.3; 332 -4.3; 365 -4.3; 402 -4.3; 442 -4.3; 486 -4.6; 535 -4.6; 588 -4.6; 647 -4.3; 712 -4.3; 783 -4.2; 861 -4.2; 947 -4.3; 1042 -4.3; 1146 -4.3; 1261 -4.3; 1387 -4.3; 1526 -4.6; 1678 -5.1; 1846 -5.7; 2031 -6.2; 2234 -6.6; 2457 -7.1; 2703 -7.7; 2973 -7.9; 3270 -7.2; 3597 -6.3; 3957 -6.6; 4353 -7.9; 4788 -10.3; 5267 -13.7; 5793 -14.3; 6373 -12.1; 7010 -12.3; 7711 -15.5; 8482 -18.0; 9330 -18.1; 10263 -16.7; 11289 -15.0; 12418 -13.8; 13660 -13.0; 15026 -12.2; 16529 -11.5; 18182 -10.1; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 931 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 931 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.36 | 5.4 dB  |
| Peaking | 186 Hz   | 0.15 | 1.4 dB  |
| Peaking | 1781 Hz  | 0.33 | 1.9 dB  |
| Peaking | 9008 Hz  | 1.85 | -6.1 dB |
| Peaking | 10987 Hz | 0.29 | -6.3 dB |
| Peaking | 1406 Hz  | 3.07 | 0.6 dB  |
| Peaking | 2940 Hz  | 1.58 | -2.3 dB |
| Peaking | 3870 Hz  | 1.93 | 4.1 dB  |
| Peaking | 5487 Hz  | 3.47 | -4.5 dB |
| Peaking | 6712 Hz  | 6.05 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB   |
| Peaking | 62 Hz    | 1.41 | 4.0 dB   |
| Peaking | 125 Hz   | 1.41 | 1.8 dB   |
| Peaking | 250 Hz   | 1.41 | 1.6 dB   |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -12.1 dB |
| Peaking | 16000 Hz | 1.41 | -7.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20931/Beyerdynamic%20DT%20931.png)