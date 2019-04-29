# Astell & Kern Rosie Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -12.8; 25 -12.9; 28 -13.0; 31 -13.1; 34 -13.2; 37 -13.3; 41 -13.4; 45 -13.4; 49 -13.5; 54 -13.5; 60 -13.7; 66 -13.9; 72 -14.0; 79 -14.2; 87 -14.4; 96 -14.6; 106 -14.7; 116 -14.7; 128 -14.7; 141 -14.7; 155 -14.6; 170 -14.4; 187 -14.2; 206 -13.8; 227 -13.4; 249 -13.0; 274 -12.5; 302 -12.0; 332 -11.4; 365 -10.8; 402 -10.2; 442 -9.6; 486 -8.9; 535 -8.2; 588 -7.5; 647 -6.7; 712 -5.8; 783 -5.0; 861 -4.2; 947 -3.6; 1042 -3.4; 1146 -3.8; 1261 -4.9; 1387 -5.5; 1526 -5.2; 1678 -4.6; 1846 -4.0; 2031 -3.6; 2234 -3.2; 2457 -2.8; 2703 -2.3; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.3; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -8.3; 8482 -10.0; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -15.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astell & Kern Rosie Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astell & Kern Rosie Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.34 | -5.0 dB |
| Peaking | 160 Hz  | 0.42 | -7.1 dB |
| Peaking | 923 Hz  | 1.54 | 3.7 dB  |
| Peaking | 3865 Hz | 1.03 | 6.8 dB  |
| Peaking | 20 Hz   | 1.05 | -0.7 dB |
| Peaking | 3974 Hz | 5.27 | -1.1 dB |
| Peaking | 6454 Hz | 2.59 | 4.4 dB  |
| Peaking | 8249 Hz | 2.69 | -6.6 dB |
| Peaking | 9559 Hz | 5.43 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Astell%20&%20Kern%20Rosie%20Max/Astell%20&%20Kern%20Rosie%20Max.png)