# HiFiMAN IE400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.8; 25 -2.8; 28 -2.9; 31 -3.0; 34 -3.1; 37 -3.2; 41 -3.3; 45 -3.5; 49 -3.7; 54 -3.9; 60 -4.2; 66 -4.5; 72 -4.8; 79 -5.2; 87 -5.6; 96 -6.0; 106 -6.3; 116 -6.6; 128 -6.9; 141 -7.2; 155 -7.4; 170 -7.5; 187 -7.5; 206 -7.6; 227 -7.6; 249 -7.6; 274 -7.5; 302 -7.3; 332 -7.1; 365 -7.0; 402 -6.8; 442 -6.4; 486 -6.4; 535 -6.1; 588 -5.6; 647 -5.5; 712 -5.5; 783 -5.4; 861 -5.8; 947 -6.2; 1042 -6.7; 1146 -7.3; 1261 -8.0; 1387 -9.0; 1526 -10.1; 1678 -11.1; 1846 -11.6; 2031 -11.4; 2234 -9.6; 2457 -6.8; 2703 -4.6; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -1.4; 5793 -2.9; 6373 -3.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN IE400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN IE400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.64 | 3.6 dB  |
| Peaking | 54 Hz   | 1.27 | 1.3 dB  |
| Peaking | 186 Hz  | 1.27 | -1.5 dB |
| Peaking | 1945 Hz | 1.85 | -8.6 dB |
| Peaking | 3584 Hz | 1    | 7.9 dB  |
| Peaking | 752 Hz  | 1.87 | 1.5 dB  |
| Peaking | 1643 Hz | 1.78 | -1.2 dB |
| Peaking | 1847 Hz | 5.13 | 1.5 dB  |
| Peaking | 6829 Hz | 1.84 | 2.7 dB  |
| Peaking | 7733 Hz | 1.67 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20IE400/HiFiMAN%20IE400.png)