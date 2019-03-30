# Fischer Audio FA-003
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -2.1; 28 -3.0; 31 -3.8; 34 -4.4; 37 -4.8; 41 -5.4; 45 -5.8; 49 -6.1; 54 -6.5; 60 -7.0; 66 -7.4; 72 -7.7; 79 -8.0; 87 -8.2; 96 -8.3; 106 -8.5; 116 -8.6; 128 -8.8; 141 -8.9; 155 -8.6; 170 -8.1; 187 -7.4; 206 -6.5; 227 -5.5; 249 -4.3; 274 -2.6; 302 -1.4; 332 -1.9; 365 -3.3; 402 -4.6; 442 -5.7; 486 -6.4; 535 -6.8; 588 -6.9; 647 -6.9; 712 -6.9; 783 -6.7; 861 -6.2; 947 -6.0; 1042 -6.3; 1146 -6.3; 1261 -6.3; 1387 -6.3; 1526 -6.3; 1678 -6.3; 1846 -6.0; 2031 -5.4; 2234 -5.0; 2457 -4.9; 2703 -5.6; 2973 -6.9; 3270 -8.4; 3597 -10.1; 3957 -11.1; 4353 -11.0; 4788 -10.2; 5267 -7.9; 5793 -3.6; 6373 -0.6; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.3; 12418 -7.3; 13660 -6.6; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio FA-003 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio FA-003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.85 | 6.9 dB  |
| Peaking | 173 Hz   | 0.36 | -3.7 dB |
| Peaking | 302 Hz   | 1.77 | 7.7 dB  |
| Peaking | 4278 Hz  | 2.54 | -6.1 dB |
| Peaking | 6322 Hz  | 5.03 | 7.0 dB  |
| Peaking | 620 Hz   | 2.4  | -0.5 dB |
| Peaking | 916 Hz   | 5    | 0.5 dB  |
| Peaking | 2415 Hz  | 3.04 | 1.9 dB  |
| Peaking | 3449 Hz  | 5.66 | -1.3 dB |
| Peaking | 12635 Hz | 4.43 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 3.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.6 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20FA-003/Fischer%20Audio%20FA-003.png)