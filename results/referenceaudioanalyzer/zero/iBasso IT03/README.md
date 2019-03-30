# iBasso IT03
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.0; 25 -10.0; 28 -10.1; 31 -10.1; 34 -10.1; 37 -10.0; 41 -9.9; 45 -9.8; 49 -9.7; 54 -9.7; 60 -9.5; 66 -9.4; 72 -9.2; 79 -9.1; 87 -9.0; 96 -8.8; 106 -8.6; 116 -8.4; 128 -8.2; 141 -7.9; 155 -7.8; 170 -7.5; 187 -7.3; 206 -7.0; 227 -6.7; 249 -6.5; 274 -6.3; 302 -6.2; 332 -6.0; 365 -5.8; 402 -5.6; 442 -5.5; 486 -5.2; 535 -5.2; 588 -4.9; 647 -4.9; 712 -4.6; 783 -4.5; 861 -4.5; 947 -4.4; 1042 -4.2; 1146 -4.3; 1261 -4.5; 1387 -4.7; 1526 -5.1; 1678 -5.7; 1846 -6.5; 2031 -7.1; 2234 -7.2; 2457 -6.6; 2703 -5.5; 2973 -4.7; 3270 -3.7; 3597 -1.8; 3957 -0.5; 4353 -3.4; 4788 -7.0; 5267 -8.0; 5793 -6.0; 6373 -2.1; 7010 -2.3; 7711 -4.6; 8482 -4.8; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT03 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.18 | -5.2 dB |
| Peaking | 2186 Hz | 3.12 | -2.7 dB |
| Peaking | 3925 Hz | 3.45 | 6.1 dB  |
| Peaking | 5055 Hz | 2.67 | -4.9 dB |
| Peaking | 6546 Hz | 5.67 | 5.1 dB  |
| Peaking | 1049 Hz | 1.33 | 0.9 dB  |
| Peaking | 1786 Hz | 5.07 | -0.6 dB |
| Peaking | 4238 Hz | 1.45 | -0.5 dB |
| Peaking | 4367 Hz | 3.76 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/iBasso%20IT03/iBasso%20IT03.png)