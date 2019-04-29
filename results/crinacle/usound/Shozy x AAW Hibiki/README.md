# Shozy x AAW Hibiki
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.3; 25 -3.8; 28 -4.4; 31 -4.8; 34 -5.2; 37 -5.6; 41 -6.0; 45 -6.3; 49 -6.5; 54 -6.8; 60 -7.0; 66 -7.3; 72 -7.6; 79 -7.9; 87 -8.2; 96 -8.5; 106 -8.8; 116 -9.0; 128 -9.1; 141 -9.3; 155 -9.5; 170 -9.5; 187 -9.5; 206 -9.4; 227 -9.3; 249 -9.2; 274 -9.1; 302 -8.9; 332 -8.7; 365 -8.4; 402 -8.1; 442 -7.8; 486 -7.4; 535 -6.9; 588 -6.4; 647 -5.7; 712 -5.0; 783 -4.4; 861 -3.8; 947 -3.2; 1042 -3.2; 1146 -3.7; 1261 -4.3; 1387 -4.7; 1526 -4.8; 1678 -4.6; 1846 -4.7; 2031 -5.2; 2234 -6.1; 2457 -7.4; 2703 -8.0; 2973 -7.4; 3270 -6.6; 3597 -6.7; 3957 -8.5; 4353 -11.7; 4788 -9.1; 5267 -3.4; 5793 -0.5; 6373 -0.9; 7010 -4.2; 7711 -7.1; 8482 -6.3; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -7.7; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy x AAW Hibiki GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy x AAW Hibiki ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 15 Hz   |  0.73 | 4.6 dB  |
| Peaking | 192 Hz  |  0.41 | -3.3 dB |
| Peaking | 975 Hz  |  1.21 | 3.8 dB  |
| Peaking | 4445 Hz |  4.43 | -6.9 dB |
| Peaking | 5871 Hz |  3.72 | 7.5 dB  |
| Peaking | 1909 Hz |  3.64 | 1.3 dB  |
| Peaking | 2722 Hz |  2.94 | -2.5 dB |
| Peaking | 3342 Hz |  2.6  | 1.1 dB  |
| Peaking | 7581 Hz | 10.11 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shozy%20x%20AAW%20Hibiki/Shozy%20x%20AAW%20Hibiki.png)