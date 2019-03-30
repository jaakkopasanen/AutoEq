# Ultrasone Edition 12
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.2; 37 -2.4; 41 -3.9; 45 -4.8; 49 -5.2; 54 -5.6; 60 -6.3; 66 -7.2; 72 -7.8; 79 -8.1; 87 -8.2; 96 -8.2; 106 -8.2; 116 -8.1; 128 -7.8; 141 -7.6; 155 -7.5; 170 -7.3; 187 -7.2; 206 -7.1; 227 -6.7; 249 -6.3; 274 -6.0; 302 -5.5; 332 -5.2; 365 -4.8; 402 -4.3; 442 -4.0; 486 -3.7; 535 -3.5; 588 -3.2; 647 -2.7; 712 -2.3; 783 -2.3; 861 -2.3; 947 -2.5; 1042 -2.8; 1146 -3.0; 1261 -3.3; 1387 -3.6; 1526 -3.6; 1678 -3.6; 1846 -3.6; 2031 -3.6; 2234 -4.0; 2457 -4.3; 2703 -2.8; 2973 -0.5; 3270 -1.4; 3597 -5.8; 3957 -9.6; 4353 -11.9; 4788 -12.4; 5267 -15.0; 5793 -18.2; 6373 -19.5; 7010 -18.3; 7711 -14.9; 8482 -11.0; 9330 -8.9; 10263 -8.2; 11289 -8.3; 12418 -9.4; 13660 -10.2; 15026 -10.1; 16529 -9.0; 18182 -6.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 12 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 12 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 1.85 | 7.3 dB   |
| Peaking | 943 Hz   | 0.65 | 4.3 dB   |
| Peaking | 3056 Hz  | 3.81 | 7.6 dB   |
| Peaking | 6224 Hz  | 1.7  | -13.8 dB |
| Peaking | 14890 Hz | 1.89 | -3.7 dB  |
| Peaking | 105 Hz   | 1.07 | -2.2 dB  |
| Peaking | 2010 Hz  | 5.09 | 1.1 dB   |
| Peaking | 4197 Hz  | 8.72 | -2.1 dB  |
| Peaking | 7326 Hz  | 7.27 | -1.9 dB  |
| Peaking | 9423 Hz  | 2.88 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.3 dB |
| Peaking | 8000 Hz  | 1.41 | -9.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20Edition%2012/Ultrasone%20Edition%2012.png)