# Sony Fake MDR-7506
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.6; 34 -2.6; 37 -3.5; 41 -4.5; 45 -5.4; 49 -6.1; 54 -6.8; 60 -7.2; 66 -7.2; 72 -7.0; 79 -7.0; 87 -7.1; 96 -6.9; 106 -6.8; 116 -6.8; 128 -6.5; 141 -6.1; 155 -5.7; 170 -5.3; 187 -4.8; 206 -4.3; 227 -3.8; 249 -3.3; 274 -3.1; 302 -3.1; 332 -3.7; 365 -4.7; 402 -5.6; 442 -6.4; 486 -7.0; 535 -7.5; 588 -7.9; 647 -8.1; 712 -8.3; 783 -8.5; 861 -8.4; 947 -8.0; 1042 -7.7; 1146 -7.5; 1261 -7.8; 1387 -8.2; 1526 -8.4; 1678 -8.7; 1846 -9.2; 2031 -9.6; 2234 -9.8; 2457 -9.8; 2703 -9.8; 2973 -9.0; 3270 -7.3; 3597 -6.5; 3957 -6.5; 4353 -4.2; 4788 -0.5; 5267 -0.7; 5793 -3.8; 6373 -4.9; 7010 -5.5; 7711 -7.2; 8482 -8.4; 9330 -8.3; 10263 -8.1; 11289 -8.8; 12418 -7.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony Fake MDR-7506 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony Fake MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.84 | 6.8 dB  |
| Peaking | 275 Hz   | 1.85 | 4.1 dB  |
| Peaking | 2466 Hz  | 0.34 | -3.1 dB |
| Peaking | 5030 Hz  | 2.48 | 8.7 dB  |
| Peaking | 10501 Hz | 1.94 | -1.7 dB |
| Peaking | 36 Hz    | 2.51 | 1.6 dB  |
| Peaking | 63 Hz    | 0.95 | -1.3 dB |
| Peaking | 685 Hz   | 0.95 | -3.5 dB |
| Peaking | 903 Hz   | 0.45 | 3.0 dB  |
| Peaking | 2267 Hz  | 1.61 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20Fake%20MDR-7506/Sony%20Fake%20MDR-7506.png)