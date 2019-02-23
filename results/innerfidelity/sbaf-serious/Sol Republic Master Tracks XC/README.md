# Sol Republic Master Tracks XC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.9; 25 -8.3; 28 -8.8; 31 -9.2; 34 -9.5; 37 -9.8; 41 -10.0; 45 -10.3; 49 -10.4; 54 -10.6; 60 -10.7; 66 -10.9; 72 -11.0; 79 -11.2; 87 -11.3; 96 -11.5; 106 -11.8; 116 -12.4; 128 -12.9; 141 -12.9; 155 -13.1; 170 -12.7; 187 -13.1; 206 -13.0; 227 -12.7; 249 -12.4; 274 -12.1; 302 -11.6; 332 -10.9; 365 -9.9; 402 -9.1; 442 -9.1; 486 -9.8; 535 -9.5; 588 -8.8; 647 -8.6; 712 -8.5; 783 -8.4; 861 -8.4; 947 -8.1; 1042 -8.0; 1146 -7.8; 1261 -7.1; 1387 -7.0; 1526 -6.6; 1678 -5.9; 1846 -4.8; 2031 -3.3; 2234 -2.3; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.7; 4353 -5.3; 4788 -7.3; 5267 -1.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sol Republic Master Tracks XC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sol Republic Master Tracks XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.67 | -2.7 dB |
| Peaking | 181 Hz  | 0.59 | -6.2 dB |
| Peaking | 2624 Hz | 0.34 | -3.6 dB |
| Peaking | 2840 Hz | 1.1  | 10.2 dB |
| Peaking | 6063 Hz | 3.83 | 6.9 dB  |
| Peaking | 856 Hz  | 2.86 | -0.1 dB |
| Peaking | 2919 Hz | 7.12 | -1.0 dB |
| Peaking | 3783 Hz | 4.66 | 2.6 dB  |
| Peaking | 4702 Hz | 4.83 | -4.3 dB |
| Peaking | 5299 Hz | 9.7  | 3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sol%20Republic%20Master%20Tracks%20XC/Sol%20Republic%20Master%20Tracks%20XC.png)