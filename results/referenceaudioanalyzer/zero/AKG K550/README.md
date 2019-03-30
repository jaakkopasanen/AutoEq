# AKG K550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -0.6; 45 -0.6; 49 -0.6; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -0.8; 87 -0.9; 96 -0.9; 106 -0.6; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -1.3; 206 -2.8; 227 -4.5; 249 -5.8; 274 -6.7; 302 -7.3; 332 -7.9; 365 -8.3; 402 -8.4; 442 -8.2; 486 -7.8; 535 -7.3; 588 -7.1; 647 -7.1; 712 -7.4; 783 -7.7; 861 -7.7; 947 -7.6; 1042 -7.4; 1146 -7.4; 1261 -7.1; 1387 -6.5; 1526 -5.7; 1678 -5.0; 1846 -4.5; 2031 -4.9; 2234 -6.3; 2457 -7.8; 2703 -8.9; 2973 -9.5; 3270 -9.6; 3597 -9.0; 3957 -8.7; 4353 -9.2; 4788 -10.4; 5267 -10.1; 5793 -6.9; 6373 -3.1; 7010 -5.9; 7711 -10.3; 8482 -12.8; 9330 -12.9; 10263 -12.6; 11289 -12.6; 12418 -12.5; 13660 -11.0; 15026 -7.4; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 0.36 | 6.8 dB  |
| Peaking | 3101 Hz | 4.03 | -2.7 dB |
| Peaking | 5064 Hz | 3.35 | -3.4 dB |
| Peaking | 6445 Hz | 4.09 | 8.1 dB  |
| Peaking | 9879 Hz | 0.91 | -7.3 dB |
| Peaking | 22 Hz   | 2.91 | 1.7 dB  |
| Peaking | 172 Hz  | 1.98 | 3.9 dB  |
| Peaking | 330 Hz  | 0.99 | -3.2 dB |
| Peaking | 963 Hz  | 1.96 | -1.0 dB |
| Peaking | 1834 Hz | 3.64 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | 6.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K550/AKG%20K550.png)