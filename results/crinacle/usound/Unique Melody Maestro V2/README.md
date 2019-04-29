# Unique Melody Maestro V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.1; 25 -4.3; 28 -4.7; 31 -5.0; 34 -5.3; 37 -5.6; 41 -5.8; 45 -6.1; 49 -6.3; 54 -6.5; 60 -6.8; 66 -7.2; 72 -7.5; 79 -7.8; 87 -8.1; 96 -8.5; 106 -8.8; 116 -9.0; 128 -9.1; 141 -9.3; 155 -9.4; 170 -9.3; 187 -9.3; 206 -9.1; 227 -9.0; 249 -8.8; 274 -8.6; 302 -8.4; 332 -8.2; 365 -8.0; 402 -7.8; 442 -7.6; 486 -7.4; 535 -7.2; 588 -7.1; 647 -6.9; 712 -6.6; 783 -6.4; 861 -6.2; 947 -6.1; 1042 -6.4; 1146 -7.1; 1261 -7.7; 1387 -8.0; 1526 -7.7; 1678 -6.9; 1846 -5.9; 2031 -5.1; 2234 -4.4; 2457 -3.5; 2703 -2.4; 2973 -1.0; 3270 -0.5; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -3.3; 5267 -5.9; 5793 -9.1; 6373 -10.3; 7010 -9.1; 7711 -9.4; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -9.6; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Maestro V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Maestro V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.33 | 3.3 dB  |
| Peaking | 157 Hz   | 0.5  | -3.0 dB |
| Peaking | 3829 Hz  | 1.38 | 7.6 dB  |
| Peaking | 6314 Hz  | 2.2  | -6.1 dB |
| Peaking | 18728 Hz | 1.93 | -3.7 dB |
| Peaking | 928 Hz   | 2.05 | 1.1 dB  |
| Peaking | 1423 Hz  | 1.96 | -2.5 dB |
| Peaking | 1940 Hz  | 1.6  | 0.3 dB  |
| Peaking | 3362 Hz  | 1.94 | 1.7 dB  |
| Peaking | 3546 Hz  | 5.04 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Unique%20Melody%20Maestro%20V2/Unique%20Melody%20Maestro%20V2.png)