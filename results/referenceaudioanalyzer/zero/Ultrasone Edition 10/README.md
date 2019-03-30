# Ultrasone Edition 10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.2; 37 -1.9; 41 -2.6; 45 -3.2; 49 -3.5; 54 -3.8; 60 -4.2; 66 -4.6; 72 -4.9; 79 -5.0; 87 -5.1; 96 -5.1; 106 -5.0; 116 -5.0; 128 -4.8; 141 -4.7; 155 -4.4; 170 -4.3; 187 -4.1; 206 -3.9; 227 -3.7; 249 -3.5; 274 -3.4; 302 -3.1; 332 -3.0; 365 -2.8; 402 -2.7; 442 -2.7; 486 -2.7; 535 -2.7; 588 -2.7; 647 -2.8; 712 -3.0; 783 -3.2; 861 -3.5; 947 -3.9; 1042 -4.6; 1146 -5.4; 1261 -6.3; 1387 -6.7; 1526 -6.2; 1678 -4.6; 1846 -1.6; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.7; 2973 -3.0; 3270 -7.1; 3597 -12.1; 3957 -16.2; 4353 -18.3; 4788 -18.8; 5267 -19.2; 5793 -21.5; 6373 -23.0; 7010 -21.5; 7711 -16.3; 8482 -11.1; 9330 -9.9; 10263 -12.0; 11289 -14.5; 12418 -15.3; 13660 -13.6; 15026 -10.7; 16529 -8.2; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.76 | 6.2 dB   |
| Peaking | 428 Hz   | 0.54 | 4.0 dB   |
| Peaking | 2499 Hz  | 1.89 | 11.3 dB  |
| Peaking | 5555 Hz  | 1    | -16.6 dB |
| Peaking | 12951 Hz | 2.48 | -6.7 dB  |
| Peaking | 1389 Hz  | 5.25 | -2.4 dB  |
| Peaking | 4141 Hz  | 3.13 | -7.4 dB  |
| Peaking | 4803 Hz  | 1.25 | 5.7 dB   |
| Peaking | 6799 Hz  | 3.22 | -6.3 dB  |
| Peaking | 8839 Hz  | 4.81 | 4.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 0.4 dB   |
| Peaking | 125 Hz   | 1.41 | 0.8 dB   |
| Peaking | 250 Hz   | 1.41 | 2.2 dB   |
| Peaking | 500 Hz   | 1.41 | 4.2 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 9.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -9.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -11.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20Edition%2010/Ultrasone%20Edition%2010.png)