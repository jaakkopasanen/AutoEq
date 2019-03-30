# Philips SHB 9100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.6; 25 -4.3; 28 -5.2; 31 -5.8; 34 -6.3; 37 -6.7; 41 -7.0; 45 -7.2; 49 -7.3; 54 -7.3; 60 -7.2; 66 -7.0; 72 -6.8; 79 -6.6; 87 -6.2; 96 -5.8; 106 -5.4; 116 -5.1; 128 -4.7; 141 -4.3; 155 -3.9; 170 -3.5; 187 -3.1; 206 -2.7; 227 -2.2; 249 -1.8; 274 -1.5; 302 -1.3; 332 -1.2; 365 -1.2; 402 -1.1; 442 -0.7; 486 -0.5; 535 -0.5; 588 -0.7; 647 -0.9; 712 -1.1; 783 -1.4; 861 -1.5; 947 -1.8; 1042 -1.8; 1146 -1.8; 1261 -1.8; 1387 -1.8; 1526 -1.7; 1678 -1.4; 1846 -1.3; 2031 -1.9; 2234 -3.0; 2457 -4.8; 2703 -6.8; 2973 -7.5; 3270 -6.6; 3597 -4.1; 3957 -3.2; 4353 -6.1; 4788 -7.8; 5267 -7.5; 5793 -6.9; 6373 -6.8; 7010 -6.2; 7711 -5.7; 8482 -4.8; 9330 -3.4; 10263 -3.3; 11289 -3.3; 12418 -3.3; 13660 -3.3; 15026 -3.3; 16529 -3.3; 18182 -3.3; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHB 9100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHB 9100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.65 | -4.3 dB |
| Peaking | 462 Hz  | 0.56 | 2.8 dB  |
| Peaking | 1831 Hz | 2.08 | 1.9 dB  |
| Peaking | 2862 Hz | 3.97 | -4.6 dB |
| Peaking | 5649 Hz | 1.69 | -4.4 dB |
| Peaking | 71 Hz   | 3.6  | 0.2 dB  |
| Peaking | 3931 Hz | 5.37 | 4.4 dB  |
| Peaking | 4417 Hz | 1.61 | -4.7 dB |
| Peaking | 5844 Hz | 0.95 | 3.6 dB  |
| Peaking | 7459 Hz | 2.4  | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.5 dB |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20SHB%209100/Philips%20SHB%209100.png)