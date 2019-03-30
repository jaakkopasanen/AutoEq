# Fostex T40RP mkII mod
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -7.9; 25 -7.8; 28 -7.8; 31 -8.0; 34 -8.2; 37 -8.6; 41 -9.3; 45 -10.1; 49 -10.9; 54 -12.0; 60 -13.1; 66 -14.0; 72 -14.5; 79 -14.8; 87 -15.0; 96 -15.1; 106 -15.1; 116 -15.3; 128 -15.5; 141 -15.4; 155 -15.1; 170 -15.1; 187 -14.9; 206 -14.7; 227 -14.3; 249 -14.0; 274 -13.5; 302 -12.5; 332 -11.2; 365 -10.3; 402 -9.5; 442 -8.3; 486 -6.6; 535 -5.0; 588 -3.9; 647 -3.5; 712 -3.8; 783 -4.7; 861 -5.6; 947 -5.9; 1042 -5.3; 1146 -4.5; 1261 -3.7; 1387 -3.2; 1526 -2.6; 1678 -1.7; 1846 -0.7; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.6; 5267 -8.2; 5793 -11.8; 6373 -12.1; 7010 -8.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T40RP mkII mod GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T40RP mkII mod ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 76 Hz    | 1    | -4.5 dB  |
| Peaking | 187 Hz   | 0.51 | -7.9 dB  |
| Peaking | 593 Hz   | 2.14 | 4.9 dB   |
| Peaking | 3087 Hz  | 0.58 | 7.4 dB   |
| Peaking | 6052 Hz  | 3    | -10.6 dB |
| Peaking | 960 Hz   | 6.14 | -1.1 dB  |
| Peaking | 1905 Hz  | 2.52 | 1.4 dB   |
| Peaking | 2722 Hz  | 1.47 | -1.1 dB  |
| Peaking | 4380 Hz  | 7.25 | 2.5 dB   |
| Peaking | 11018 Hz | 1.59 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -6.1 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | -7.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fostex%20T40RP%20mkII%20mod/Fostex%20T40RP%20mkII%20mod.png)