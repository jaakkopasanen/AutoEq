# AKG K540
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.3; 37 -1.8; 41 -2.5; 45 -3.0; 49 -3.4; 54 -3.8; 60 -4.1; 66 -4.4; 72 -4.8; 79 -5.3; 87 -5.7; 96 -6.0; 106 -6.1; 116 -6.3; 128 -6.4; 141 -6.4; 155 -6.5; 170 -6.7; 187 -7.1; 206 -7.4; 227 -7.1; 249 -6.9; 274 -6.4; 302 -6.1; 332 -6.1; 365 -5.8; 402 -5.5; 442 -5.2; 486 -4.8; 535 -4.2; 588 -3.6; 647 -2.7; 712 -1.5; 783 -0.5; 861 -0.5; 947 -0.9; 1042 -3.3; 1146 -5.0; 1261 -5.9; 1387 -6.5; 1526 -6.8; 1678 -6.6; 1846 -6.4; 2031 -6.8; 2234 -8.0; 2457 -9.5; 2703 -10.5; 2973 -10.9; 3270 -11.0; 3597 -10.7; 3957 -10.1; 4353 -9.5; 4788 -9.8; 5267 -10.7; 5793 -10.4; 6373 -7.9; 7010 -5.5; 7711 -6.2; 8482 -6.5; 9330 -8.8; 10263 -12.2; 11289 -14.6; 12418 -15.3; 13660 -13.0; 15026 -7.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K540 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.84 | 6.4 dB  |
| Peaking | 861 Hz   | 1.5  | 7.1 dB  |
| Peaking | 1190 Hz  | 2.54 | -2.2 dB |
| Peaking | 3399 Hz  | 1.22 | -4.8 dB |
| Peaking | 12164 Hz | 2.25 | -9.8 dB |
| Peaking | 207 Hz   | 2.3  | -1.2 dB |
| Peaking | 5675 Hz  | 3.35 | -4.7 dB |
| Peaking | 6996 Hz  | 1.43 | 3.6 dB  |
| Peaking | 10396 Hz | 4.26 | -2.7 dB |
| Peaking | 15123 Hz | 2.52 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K540/AKG%20K540.png)