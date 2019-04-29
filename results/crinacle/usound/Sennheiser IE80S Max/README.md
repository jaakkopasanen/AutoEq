# Sennheiser IE80S Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.6; 25 -10.7; 28 -10.8; 31 -10.9; 34 -10.9; 37 -10.9; 41 -10.9; 45 -10.9; 49 -10.9; 54 -10.9; 60 -11.0; 66 -11.0; 72 -11.0; 79 -11.1; 87 -11.2; 96 -11.3; 106 -11.4; 116 -11.3; 128 -11.3; 141 -11.2; 155 -11.1; 170 -10.9; 187 -10.6; 206 -10.3; 227 -10.0; 249 -9.6; 274 -9.2; 302 -8.8; 332 -8.3; 365 -7.9; 402 -7.5; 442 -7.0; 486 -6.6; 535 -6.1; 588 -5.6; 647 -5.1; 712 -4.6; 783 -4.0; 861 -3.5; 947 -3.2; 1042 -2.9; 1146 -3.3; 1261 -4.0; 1387 -4.2; 1526 -4.0; 1678 -3.4; 1846 -2.9; 2031 -2.5; 2234 -2.5; 2457 -2.9; 2703 -3.6; 2973 -4.3; 3270 -4.9; 3597 -5.3; 3957 -6.2; 4353 -8.3; 4788 -10.6; 5267 -7.7; 5793 -2.6; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -6.5; 20000 -14.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80S Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80S Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.51 | -3.7 dB |
| Peaking | 142 Hz   | 0.36 | -5.1 dB |
| Peaking | 1356 Hz  | 0.36 | 3.3 dB  |
| Peaking | 4818 Hz  | 3.46 | -6.8 dB |
| Peaking | 6199 Hz  | 4.68 | 6.6 dB  |
| Peaking | 1006 Hz  | 1.76 | 2.3 dB  |
| Peaking | 1410 Hz  | 0.93 | -2.7 dB |
| Peaking | 2049 Hz  | 1.9  | 2.4 dB  |
| Peaking | 17916 Hz | 1.4  | 2.5 dB  |
| Peaking | 19960 Hz | 0.97 | -8.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sennheiser%20IE80S%20Max/Sennheiser%20IE80S%20Max.png)