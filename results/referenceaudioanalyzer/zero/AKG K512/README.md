# AKG K512
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.4; 34 -2.6; 37 -3.8; 41 -5.1; 45 -6.1; 49 -7.0; 54 -7.9; 60 -8.7; 66 -9.1; 72 -9.1; 79 -9.1; 87 -9.1; 96 -9.4; 106 -9.7; 116 -10.0; 128 -10.4; 141 -10.8; 155 -11.1; 170 -11.3; 187 -11.4; 206 -11.6; 227 -11.7; 249 -11.4; 274 -11.4; 302 -11.4; 332 -11.4; 365 -11.2; 402 -11.1; 442 -11.0; 486 -10.4; 535 -10.1; 588 -10.7; 647 -11.1; 712 -10.2; 783 -8.9; 861 -9.5; 947 -10.4; 1042 -10.1; 1146 -9.3; 1261 -8.5; 1387 -7.5; 1526 -6.2; 1678 -4.6; 1846 -3.4; 2031 -2.6; 2234 -1.6; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.0; 3957 -0.8; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -9.3; 10263 -10.5; 11289 -10.6; 12418 -9.8; 13660 -8.2; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K512 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K512 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 1.32 | 7.2 dB   |
| Peaking | 302 Hz   | 0.23 | -5.4 dB  |
| Peaking | 1150 Hz  | 1.44 | -4.1 dB  |
| Peaking | 4391 Hz  | 0.27 | 8.4 dB   |
| Peaking | 10393 Hz | 1.01 | -10.1 dB |
| Peaking | 33 Hz    | 3.37 | 0.7 dB   |
| Peaking | 2456 Hz  | 3.83 | 0.7 dB   |
| Peaking | 3732 Hz  | 4.01 | -1.2 dB  |
| Peaking | 6379 Hz  | 3.12 | 2.0 dB   |
| Peaking | 7292 Hz  | 5.62 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -4.0 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K512/AKG%20K512.png)