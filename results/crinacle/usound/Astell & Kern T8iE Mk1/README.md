# Astell & Kern T8iE Mk1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.1; 25 -11.2; 28 -11.3; 31 -11.4; 34 -11.4; 37 -11.5; 41 -11.5; 45 -11.6; 49 -11.7; 54 -11.8; 60 -11.9; 66 -12.1; 72 -12.3; 79 -12.5; 87 -12.7; 96 -12.9; 106 -13.0; 116 -13.1; 128 -13.2; 141 -13.2; 155 -13.1; 170 -12.9; 187 -12.7; 206 -12.3; 227 -11.9; 249 -11.5; 274 -11.0; 302 -10.5; 332 -9.9; 365 -9.4; 402 -8.8; 442 -8.2; 486 -7.6; 535 -7.0; 588 -6.4; 647 -5.7; 712 -5.1; 783 -4.4; 861 -3.9; 947 -3.8; 1042 -3.9; 1146 -4.4; 1261 -5.1; 1387 -5.4; 1526 -5.3; 1678 -4.9; 1846 -4.3; 2031 -3.7; 2234 -3.1; 2457 -2.4; 2703 -1.7; 2973 -1.2; 3270 -1.0; 3597 -1.1; 3957 -1.9; 4353 -3.6; 4788 -5.6; 5267 -3.6; 5793 -0.5; 6373 -1.6; 7010 -4.3; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astell & Kern T8iE Mk1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astell & Kern T8iE Mk1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.32 | -4.8 dB |
| Peaking | 137 Hz  | 0.92 | -4.5 dB |
| Peaking | 259 Hz  | 1.59 | -2.7 dB |
| Peaking | 2925 Hz | 0.91 | 4.9 dB  |
| Peaking | 6009 Hz | 6.27 | 5.0 dB  |
| Peaking | 917 Hz  | 1.24 | 5.1 dB  |
| Peaking | 1125 Hz | 0.53 | -2.9 dB |
| Peaking | 4702 Hz | 1.04 | 3.0 dB  |
| Peaking | 4814 Hz | 4.52 | -4.5 dB |
| Peaking | 7996 Hz | 1.37 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Astell%20&%20Kern%20T8iE%20Mk1/Astell%20&%20Kern%20T8iE%20Mk1.png)