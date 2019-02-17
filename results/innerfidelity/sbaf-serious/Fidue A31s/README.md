# Fidue A31s
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.2; 23 -14.3; 25 -14.4; 28 -14.7; 31 -14.9; 34 -15.0; 37 -15.1; 41 -15.2; 45 -15.2; 49 -15.3; 54 -15.4; 60 -15.5; 66 -15.5; 72 -15.6; 79 -15.7; 87 -15.7; 96 -15.8; 106 -15.6; 116 -15.5; 128 -15.3; 141 -15.1; 155 -14.8; 170 -14.4; 187 -13.9; 206 -13.5; 227 -12.9; 249 -12.4; 274 -11.7; 302 -11.2; 332 -10.5; 365 -9.9; 402 -9.3; 442 -8.4; 486 -8.0; 535 -7.5; 588 -6.7; 647 -6.3; 712 -6.1; 783 -5.5; 861 -5.9; 947 -6.2; 1042 -6.1; 1146 -6.6; 1261 -7.4; 1387 -8.0; 1526 -8.2; 1678 -9.5; 1846 -10.7; 2031 -11.5; 2234 -12.1; 2457 -10.7; 2703 -8.2; 2973 -5.0; 3270 -3.3; 3597 -3.2; 3957 -6.1; 4353 -10.7; 4788 -7.8; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A31s GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A31s ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.29 | -8.5 dB |
| Peaking | 167 Hz  | 0.76 | -4.4 dB |
| Peaking | 2170 Hz | 2.29 | -6.0 dB |
| Peaking | 3270 Hz | 5.4  | 5.1 dB  |
| Peaking | 5966 Hz | 4.51 | 7.2 dB  |
| Peaking | 323 Hz  | 2.33 | -0.8 dB |
| Peaking | 767 Hz  | 1.92 | 1.8 dB  |
| Peaking | 3753 Hz | 6.61 | 3.0 dB  |
| Peaking | 4457 Hz | 4.85 | -6.3 dB |
| Peaking | 5245 Hz | 8.23 | 4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.2 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A31s/Fidue%20A31s.png)