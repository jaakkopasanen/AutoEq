# BGVP DMG Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.7; 25 -8.1; 28 -8.4; 31 -8.7; 34 -8.9; 37 -9.1; 41 -9.3; 45 -9.4; 49 -9.6; 54 -9.7; 60 -9.9; 66 -10.1; 72 -10.3; 79 -10.5; 87 -10.6; 96 -10.9; 106 -11.0; 116 -11.1; 128 -11.1; 141 -11.0; 155 -11.0; 170 -10.8; 187 -10.5; 206 -10.2; 227 -9.8; 249 -9.3; 274 -8.8; 302 -8.3; 332 -7.7; 365 -7.2; 402 -6.6; 442 -6.0; 486 -5.4; 535 -4.8; 588 -4.2; 647 -3.6; 712 -2.8; 783 -1.9; 861 -1.3; 947 -0.9; 1042 -0.8; 1146 -1.0; 1261 -1.5; 1387 -1.8; 1526 -1.9; 1678 -1.7; 1846 -1.5; 2031 -1.4; 2234 -1.5; 2457 -1.8; 2703 -2.6; 2973 -2.3; 3270 -0.5; 3597 -0.9; 3957 -1.7; 4353 -2.4; 4788 -3.9; 5267 -4.8; 5793 -5.2; 6373 -3.7; 7010 -3.5; 7711 -6.6; 8482 -7.7; 9330 -6.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DMG Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DMG Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.5  | -2.8 dB |
| Peaking | 151 Hz  | 0.5  | -5.5 dB |
| Peaking | 967 Hz  | 1.03 | 4.5 dB  |
| Peaking | 2073 Hz | 2.05 | 2.4 dB  |
| Peaking | 3547 Hz | 2.81 | 3.9 dB  |
| Peaking | 4341 Hz | 8.73 | 0.9 dB  |
| Peaking | 5884 Hz | 3.47 | -1.4 dB |
| Peaking | 6717 Hz | 4.98 | 3.3 dB  |
| Peaking | 8256 Hz | 4.16 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/BGVP%20DMG%20Gold/BGVP%20DMG%20Gold.png)