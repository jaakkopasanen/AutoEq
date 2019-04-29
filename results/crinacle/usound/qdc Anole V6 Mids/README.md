# qdc Anole V6 Mids
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -6.9; 25 -6.9; 28 -7.0; 31 -7.0; 34 -7.0; 37 -7.1; 41 -7.1; 45 -7.1; 49 -7.1; 54 -7.1; 60 -7.2; 66 -7.3; 72 -7.4; 79 -7.5; 87 -7.5; 96 -7.7; 106 -7.8; 116 -7.8; 128 -7.7; 141 -7.6; 155 -7.5; 170 -7.3; 187 -7.1; 206 -6.9; 227 -6.6; 249 -6.3; 274 -6.1; 302 -5.8; 332 -5.7; 365 -5.5; 402 -5.5; 442 -5.5; 486 -5.6; 535 -5.8; 588 -6.0; 647 -6.3; 712 -6.6; 783 -6.9; 861 -7.2; 947 -7.6; 1042 -8.2; 1146 -9.0; 1261 -9.8; 1387 -10.1; 1526 -9.8; 1678 -9.2; 1846 -8.6; 2031 -8.1; 2234 -7.7; 2457 -7.2; 2703 -6.5; 2973 -5.7; 3270 -5.3; 3597 -5.4; 3957 -6.3; 4353 -6.5; 4788 -3.2; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -4.1; 7711 -6.6; 8482 -9.8; 9330 -9.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.4; 15026 -12.7; 16529 -12.6; 18182 -13.0; 20000 -19.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V6 Mids GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V6 Mids ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 101 Hz   | 1.22 | -1.4 dB  |
| Peaking | 1442 Hz  | 1.85 | -3.8 dB  |
| Peaking | 3191 Hz  | 5.9  | 1.3 dB   |
| Peaking | 5715 Hz  | 3.18 | 7.4 dB   |
| Peaking | 20470 Hz | 0.32 | -11.3 dB |
| Peaking | 422 Hz   | 1.46 | 1.3 dB   |
| Peaking | 1099 Hz  | 2.07 | -0.3 dB  |
| Peaking | 8722 Hz  | 4.61 | -4.0 dB  |
| Peaking | 11410 Hz | 2.55 | 2.3 dB   |
| Peaking | 14147 Hz | 2.41 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -8.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20V6%20Mids/qdc%20Anole%20V6%20Mids.png)