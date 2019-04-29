# BGVP DMG Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.8; 25 -8.0; 28 -8.3; 31 -8.5; 34 -8.7; 37 -8.8; 41 -8.9; 45 -9.1; 49 -9.1; 54 -9.2; 60 -9.4; 66 -9.6; 72 -9.7; 79 -9.9; 87 -10.0; 96 -10.2; 106 -10.4; 116 -10.4; 128 -10.4; 141 -10.4; 155 -10.3; 170 -10.1; 187 -9.8; 206 -9.5; 227 -9.1; 249 -8.6; 274 -8.1; 302 -7.6; 332 -7.0; 365 -6.5; 402 -5.9; 442 -5.3; 486 -4.7; 535 -4.1; 588 -3.5; 647 -3.0; 712 -2.2; 783 -1.4; 861 -0.8; 947 -0.5; 1042 -0.5; 1146 -0.9; 1261 -1.4; 1387 -1.8; 1526 -2.1; 1678 -2.3; 1846 -2.4; 2031 -2.7; 2234 -3.0; 2457 -3.5; 2703 -4.5; 2973 -4.0; 3270 -2.4; 3597 -2.8; 3957 -3.1; 4353 -3.1; 4788 -3.9; 5267 -4.5; 5793 -5.1; 6373 -3.5; 7010 -3.1; 7711 -6.5; 8482 -8.0; 9330 -6.6; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DMG Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DMG Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.49 | -2.6 dB |
| Peaking | 148 Hz  | 0.49 | -5.0 dB |
| Peaking | 983 Hz  | 0.79 | 4.9 dB  |
| Peaking | 3776 Hz | 2.57 | 1.9 dB  |
| Peaking | 2773 Hz | 6.36 | -2.5 dB |
| Peaking | 2803 Hz | 2.48 | 1.2 dB  |
| Peaking | 6816 Hz | 7.88 | 3.1 dB  |
| Peaking | 8393 Hz | 4.06 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/BGVP%20DMG%20Black/BGVP%20DMG%20Black.png)