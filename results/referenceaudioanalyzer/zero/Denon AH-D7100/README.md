# Denon AH-D7100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.5; 25 -5.8; 28 -6.1; 31 -6.3; 34 -6.3; 37 -6.3; 41 -6.4; 45 -6.6; 49 -6.8; 54 -7.2; 60 -7.4; 66 -7.6; 72 -7.6; 79 -7.6; 87 -7.6; 96 -7.6; 106 -7.4; 116 -7.0; 128 -6.7; 141 -6.6; 155 -6.6; 170 -6.1; 187 -5.5; 206 -4.8; 227 -3.8; 249 -2.4; 274 -1.1; 302 -0.5; 332 -0.5; 365 -1.3; 402 -2.5; 442 -3.5; 486 -4.4; 535 -5.5; 588 -6.5; 647 -7.1; 712 -7.4; 783 -7.6; 861 -7.7; 947 -7.9; 1042 -8.1; 1146 -8.4; 1261 -9.1; 1387 -9.9; 1526 -10.6; 1678 -10.9; 1846 -10.6; 2031 -9.4; 2234 -7.5; 2457 -6.1; 2703 -6.1; 2973 -6.3; 3270 -5.8; 3597 -6.2; 3957 -7.4; 4353 -7.6; 4788 -6.1; 5267 -3.2; 5793 -5.6; 6373 -10.3; 7010 -10.9; 7711 -9.7; 8482 -8.1; 9330 -7.7; 10263 -9.3; 11289 -11.3; 12418 -11.2; 13660 -9.6; 15026 -9.5; 16529 -10.7; 18182 -9.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 317 Hz   | 1.99 | 6.7 dB  |
| Peaking | 1545 Hz  | 1.87 | -4.6 dB |
| Peaking | 11789 Hz | 1.1  | -4.1 dB |
| Peaking | 16842 Hz | 2.04 | -3.1 dB |
| Peaking | 18236 Hz | 2.21 | -2.0 dB |
| Peaking | 20 Hz    | 2.49 | 1.1 dB  |
| Peaking | 5453 Hz  | 5.56 | 5.8 dB  |
| Peaking | 6802 Hz  | 2.84 | -4.9 dB |
| Peaking | 9349 Hz  | 2.03 | 2.2 dB  |
| Peaking | 11282 Hz | 4.08 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | 5.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | -5.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Denon%20AH-D7100/Denon%20AH-D7100.png)