# AKG K712
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.7; 34 -2.9; 37 -3.7; 41 -4.2; 45 -4.4; 49 -4.6; 54 -5.0; 60 -5.3; 66 -5.5; 72 -5.5; 79 -5.5; 87 -5.5; 96 -5.5; 106 -5.5; 116 -5.6; 128 -6.0; 141 -6.2; 155 -6.4; 170 -6.5; 187 -6.5; 206 -6.8; 227 -6.8; 249 -6.8; 274 -7.0; 302 -7.1; 332 -6.9; 365 -6.8; 402 -6.8; 442 -6.8; 486 -6.7; 535 -6.5; 588 -6.5; 647 -6.5; 712 -6.5; 783 -6.2; 861 -6.0; 947 -5.6; 1042 -5.1; 1146 -4.4; 1261 -3.8; 1387 -3.7; 1526 -4.5; 1678 -5.6; 1846 -6.8; 2031 -7.8; 2234 -8.4; 2457 -8.2; 2703 -7.3; 2973 -5.3; 3270 -2.4; 3597 -1.0; 3957 -2.9; 4353 -5.6; 4788 -7.5; 5267 -7.7; 5793 -7.1; 6373 -8.9; 7010 -11.6; 7711 -11.9; 8482 -10.1; 9330 -8.6; 10263 -9.1; 11289 -10.6; 12418 -10.5; 13660 -7.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.84 | 6.2 dB  |
| Peaking | 1295 Hz  | 3.63 | 3.2 dB  |
| Peaking | 3593 Hz  | 5.29 | 6.5 dB  |
| Peaking | 7472 Hz  | 2.72 | -5.6 dB |
| Peaking | 11821 Hz | 2.97 | -4.4 dB |
| Peaking | 106 Hz   | 2.57 | 0.7 dB  |
| Peaking | 293 Hz   | 0.99 | -0.6 dB |
| Peaking | 2206 Hz  | 0.98 | 1.6 dB  |
| Peaking | 2278 Hz  | 2.47 | -4.1 dB |
| Peaking | 14662 Hz | 3.98 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K712/AKG%20K712.png)