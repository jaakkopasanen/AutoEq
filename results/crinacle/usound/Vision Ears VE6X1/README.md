# Vision Ears VE6X1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -4.9; 25 -5.1; 28 -5.3; 31 -5.5; 34 -5.7; 37 -5.9; 41 -6.1; 45 -6.3; 49 -6.5; 54 -6.7; 60 -6.9; 66 -7.2; 72 -7.6; 79 -8.0; 87 -8.4; 96 -8.9; 106 -9.3; 116 -9.6; 128 -10.0; 141 -10.2; 155 -10.5; 170 -10.6; 187 -10.7; 206 -10.8; 227 -10.8; 249 -10.7; 274 -10.6; 302 -10.4; 332 -10.3; 365 -10.0; 402 -9.8; 442 -9.6; 486 -9.3; 535 -8.9; 588 -8.6; 647 -8.2; 712 -7.7; 783 -7.1; 861 -6.6; 947 -6.2; 1042 -6.1; 1146 -6.2; 1261 -6.3; 1387 -6.1; 1526 -5.5; 1678 -4.6; 1846 -3.8; 2031 -3.3; 2234 -3.4; 2457 -4.2; 2703 -4.6; 2973 -3.8; 3270 -3.0; 3597 -3.4; 3957 -4.5; 4353 -5.1; 4788 -3.5; 5267 -1.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears VE6X1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears VE6X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.28 | 1.9 dB  |
| Peaking | 213 Hz  | 0.47 | -4.6 dB |
| Peaking | 2016 Hz | 1.84 | 3.1 dB  |
| Peaking | 3344 Hz | 3.7  | 2.6 dB  |
| Peaking | 5829 Hz | 3.24 | 6.5 dB  |
| Peaking | 950 Hz  | 4.6  | 0.9 dB  |
| Peaking | 8176 Hz | 4.82 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Vision%20Ears%20VE6X1/Vision%20Ears%20VE6X1.png)