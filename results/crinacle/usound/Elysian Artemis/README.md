# Elysian Artemis
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.2; 25 -5.6; 28 -6.1; 31 -6.4; 34 -6.7; 37 -6.9; 41 -7.2; 45 -7.5; 49 -7.8; 54 -8.2; 60 -8.5; 66 -8.8; 72 -9.1; 79 -9.5; 87 -9.9; 96 -10.3; 106 -10.7; 116 -11.1; 128 -11.3; 141 -11.5; 155 -11.6; 170 -11.8; 187 -11.8; 206 -11.8; 227 -11.7; 249 -11.5; 274 -11.2; 302 -11.0; 332 -10.7; 365 -10.3; 402 -9.9; 442 -9.5; 486 -9.0; 535 -8.5; 588 -7.9; 647 -7.3; 712 -6.6; 783 -5.8; 861 -5.2; 947 -4.8; 1042 -4.7; 1146 -5.1; 1261 -5.6; 1387 -5.6; 1526 -5.3; 1678 -4.6; 1846 -4.0; 2031 -4.2; 2234 -4.7; 2457 -4.3; 2703 -3.2; 2973 -1.8; 3270 -0.7; 3597 -0.5; 3957 -0.6; 4353 -1.1; 4788 -1.9; 5267 -3.4; 5793 -4.7; 6373 -6.7; 7010 -8.4; 7711 -6.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Elysian Artemis GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Elysian Artemis ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.12 | 2.3 dB  |
| Peaking | 139 Hz  | 0.72 | -1.2 dB |
| Peaking | 261 Hz  | 0.33 | -4.8 dB |
| Peaking | 914 Hz  | 0.74 | 3.4 dB  |
| Peaking | 3685 Hz | 1.7  | 6.5 dB  |
| Peaking | 981 Hz  | 2.44 | 1.2 dB  |
| Peaking | 1355 Hz | 1.1  | -1.4 dB |
| Peaking | 1828 Hz | 3.57 | 1.8 dB  |
| Peaking | 4938 Hz | 4.31 | 1.4 dB  |
| Peaking | 7034 Hz | 4.85 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Elysian%20Artemis/Elysian%20Artemis.png)