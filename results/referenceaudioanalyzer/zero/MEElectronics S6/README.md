# MEElectronics S6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -13.0; 25 -13.4; 28 -13.9; 31 -14.2; 34 -14.4; 37 -14.5; 41 -14.5; 45 -14.5; 49 -14.5; 54 -14.3; 60 -14.1; 66 -13.8; 72 -13.5; 79 -13.1; 87 -12.7; 96 -12.2; 106 -11.7; 116 -11.2; 128 -10.6; 141 -10.0; 155 -9.4; 170 -8.9; 187 -8.3; 206 -7.6; 227 -7.1; 249 -6.5; 274 -5.9; 302 -5.3; 332 -4.7; 365 -4.2; 402 -3.9; 442 -3.7; 486 -3.3; 535 -2.8; 588 -2.4; 647 -2.0; 712 -1.5; 783 -1.1; 861 -0.8; 947 -0.8; 1042 -0.7; 1146 -0.5; 1261 -0.7; 1387 -0.9; 1526 -1.2; 1678 -1.8; 1846 -2.7; 2031 -4.0; 2234 -5.7; 2457 -8.1; 2703 -10.5; 2973 -11.8; 3270 -11.6; 3597 -10.3; 3957 -9.2; 4353 -10.1; 4788 -13.5; 5267 -14.8; 5793 -12.5; 6373 -6.5; 7010 -3.8; 7711 -5.7; 8482 -6.0; 9330 -7.0; 10263 -6.1; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEElectronics S6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEElectronics S6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 45 Hz   |  0.34 | -8.6 dB  |
| Peaking | 1595 Hz |  0.3  | 7.0 dB   |
| Peaking | 2987 Hz |  1.54 | -11.3 dB |
| Peaking | 5190 Hz |  3.6  | -10.7 dB |
| Peaking | 324 Hz  |  4.49 | 0.4 dB   |
| Peaking | 5823 Hz | 10.57 | -2.4 dB  |
| Peaking | 6798 Hz |  6.19 | 3.3 dB   |
| Peaking | 9457 Hz |  3.35 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.2 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -8.0 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MEElectronics%20S6/MEElectronics%20S6.png)