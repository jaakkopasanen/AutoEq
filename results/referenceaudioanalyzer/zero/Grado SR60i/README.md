# Grado SR60i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.8; 49 -2.7; 54 -3.6; 60 -4.5; 66 -5.3; 72 -5.9; 79 -6.3; 87 -6.5; 96 -6.7; 106 -6.7; 116 -6.5; 128 -6.3; 141 -6.1; 155 -5.9; 170 -5.6; 187 -5.3; 206 -5.1; 227 -4.8; 249 -4.5; 274 -4.2; 302 -4.0; 332 -3.8; 365 -3.6; 402 -3.4; 442 -3.3; 486 -3.1; 535 -3.1; 588 -3.1; 647 -3.3; 712 -3.2; 783 -3.1; 861 -3.1; 947 -3.1; 1042 -3.2; 1146 -3.5; 1261 -3.8; 1387 -4.1; 1526 -4.8; 1678 -6.7; 1846 -9.9; 2031 -11.9; 2234 -12.1; 2457 -11.4; 2703 -10.3; 2973 -8.8; 3270 -7.1; 3597 -8.0; 3957 -10.3; 4353 -10.7; 4788 -10.0; 5267 -10.9; 5793 -12.7; 6373 -14.4; 7010 -13.9; 7711 -9.7; 8482 -6.5; 9330 -6.5; 10263 -6.6; 11289 -7.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 1.14 | 7.0 dB   |
| Peaking | 1586 Hz | 0.23 | 4.9 dB   |
| Peaking | 2199 Hz | 1.82 | -10.3 dB |
| Peaking | 4383 Hz | 1.96 | -5.1 dB  |
| Peaking | 6533 Hz | 2.84 | -9.5 dB  |
| Peaking | 45 Hz   | 3.42 | 1.4 dB   |
| Peaking | 93 Hz   | 1.75 | -1.3 dB  |
| Peaking | 1931 Hz | 4.16 | -0.2 dB  |
| Peaking | 8548 Hz | 4.55 | 2.2 dB   |
| Peaking | 8994 Hz | 1.27 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20SR60i/Grado%20SR60i.png)