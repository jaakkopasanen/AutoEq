# HiFiMAN HE-300 Rev 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.2; 34 -2.2; 37 -3.2; 41 -4.3; 45 -5.2; 49 -5.8; 54 -6.3; 60 -6.8; 66 -7.2; 72 -8.0; 79 -8.6; 87 -8.8; 96 -9.4; 106 -9.5; 116 -9.4; 128 -9.3; 141 -8.9; 155 -8.5; 170 -7.9; 187 -7.6; 206 -7.2; 227 -6.9; 249 -7.6; 274 -6.9; 302 -6.2; 332 -5.6; 365 -5.1; 402 -4.7; 442 -4.2; 486 -3.9; 535 -3.3; 588 -2.6; 647 -2.5; 712 -2.1; 783 -2.7; 861 -3.6; 947 -4.0; 1042 -4.4; 1146 -5.2; 1261 -5.8; 1387 -6.8; 1526 -7.7; 1678 -8.1; 1846 -8.2; 2031 -9.0; 2234 -8.5; 2457 -7.9; 2703 -8.0; 2973 -9.3; 3270 -10.1; 3597 -8.8; 3957 -8.1; 4353 -9.3; 4788 -10.3; 5267 -9.1; 5793 -5.3; 6373 -2.5; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -7.5; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-300 Rev 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-300 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 2.06 | 7.3 dB  |
| Peaking | 714 Hz  | 1.32 | 5.0 dB  |
| Peaking | 2943 Hz | 0.5  | -2.6 dB |
| Peaking | 4993 Hz | 4.36 | -3.1 dB |
| Peaking | 6387 Hz | 3.72 | 6.1 dB  |
| Peaking | 92 Hz   | 2    | -1.6 dB |
| Peaking | 128 Hz  | 1.17 | -2.3 dB |
| Peaking | 428 Hz  | 2.83 | 0.9 dB  |
| Peaking | 1992 Hz | 9.24 | -1.1 dB |
| Peaking | 2556 Hz | 8.57 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-300%20Rev%202/HiFiMAN%20HE-300%20Rev%202.png)