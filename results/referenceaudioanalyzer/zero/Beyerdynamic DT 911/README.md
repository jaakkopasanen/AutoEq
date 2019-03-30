# Beyerdynamic DT 911
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.1; 87 -1.7; 96 -2.3; 106 -2.8; 116 -3.4; 128 -3.8; 141 -4.3; 155 -4.6; 170 -4.7; 187 -5.0; 206 -5.0; 227 -5.2; 249 -5.4; 274 -5.2; 302 -5.0; 332 -4.9; 365 -4.6; 402 -4.4; 442 -4.1; 486 -4.1; 535 -4.1; 588 -3.8; 647 -3.7; 712 -3.4; 783 -3.6; 861 -3.8; 947 -4.2; 1042 -4.7; 1146 -5.1; 1261 -5.4; 1387 -5.4; 1526 -5.3; 1678 -5.5; 1846 -5.8; 2031 -6.1; 2234 -6.3; 2457 -6.5; 2703 -6.9; 2973 -7.4; 3270 -7.7; 3597 -7.3; 3957 -5.4; 4353 -4.4; 4788 -9.2; 5267 -13.4; 5793 -14.3; 6373 -13.5; 7010 -14.3; 7711 -15.9; 8482 -16.3; 9330 -15.2; 10263 -13.7; 11289 -12.4; 12418 -11.7; 13660 -11.2; 15026 -10.5; 16529 -9.0; 18182 -7.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 911 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 911 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.41 | 6.6 dB  |
| Peaking | 759 Hz   | 0.65 | 2.8 dB  |
| Peaking | 4341 Hz  | 3.48 | 7.3 dB  |
| Peaking | 5246 Hz  | 3.46 | -4.2 dB |
| Peaking | 8544 Hz  | 0.67 | -9.0 dB |
| Peaking | 39 Hz    | 2.14 | -0.7 dB |
| Peaking | 75 Hz    | 3.56 | 0.9 dB  |
| Peaking | 8371 Hz  | 3.82 | -1.7 dB |
| Peaking | 10740 Hz | 1.04 | 1.4 dB  |
| Peaking | 14765 Hz | 1.52 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 5.2 dB   |
| Peaking | 125 Hz   | 1.41 | 1.7 dB   |
| Peaking | 250 Hz   | 1.41 | 0.2 dB   |
| Peaking | 500 Hz   | 1.41 | 2.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -11.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20911/Beyerdynamic%20DT%20911.png)