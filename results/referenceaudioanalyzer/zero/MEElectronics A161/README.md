# MEElectronics A161
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -4.1; 25 -4.8; 28 -5.6; 31 -6.2; 34 -6.7; 37 -7.0; 41 -7.4; 45 -7.7; 49 -8.0; 54 -8.2; 60 -8.5; 66 -8.7; 72 -8.8; 79 -8.9; 87 -8.9; 96 -8.9; 106 -8.9; 116 -8.9; 128 -8.9; 141 -8.9; 155 -8.7; 170 -8.6; 187 -8.5; 206 -8.3; 227 -7.9; 249 -7.9; 274 -8.4; 302 -8.7; 332 -8.5; 365 -8.2; 402 -7.8; 442 -7.4; 486 -7.0; 535 -6.7; 588 -6.3; 647 -5.9; 712 -5.6; 783 -5.2; 861 -4.9; 947 -4.5; 1042 -4.3; 1146 -4.0; 1261 -3.9; 1387 -3.7; 1526 -3.9; 1678 -4.2; 1846 -4.8; 2031 -5.8; 2234 -7.2; 2457 -8.9; 2703 -9.3; 2973 -7.7; 3270 -5.1; 3597 -2.4; 3957 -0.7; 4353 -0.5; 4788 -2.1; 5267 -5.5; 5793 -7.7; 6373 -6.7; 7010 -3.9; 7711 -5.8; 8482 -6.1; 9330 -6.7; 10263 -6.3; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEElectronics A161 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEElectronics A161 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.87 | 3.3 dB  |
| Peaking | 96 Hz   | 0.57 | -3.0 dB |
| Peaking | 319 Hz  | 2.61 | -1.9 dB |
| Peaking | 2677 Hz | 5.25 | -4.6 dB |
| Peaking | 4108 Hz | 3.18 | 6.4 dB  |
| Peaking | 1282 Hz | 1.46 | 2.7 dB  |
| Peaking | 4823 Hz | 3.46 | 4.0 dB  |
| Peaking | 5845 Hz | 1.51 | -4.9 dB |
| Peaking | 6879 Hz | 6.35 | 4.4 dB  |
| Peaking | 7695 Hz | 2.36 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MEElectronics%20A161/MEElectronics%20A161.png)