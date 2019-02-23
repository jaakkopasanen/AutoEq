# FLC Technologies FLC8 GGBl
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.6; 25 -11.7; 28 -11.7; 31 -11.8; 34 -11.8; 37 -11.8; 41 -11.8; 45 -11.8; 49 -11.8; 54 -11.8; 60 -11.8; 66 -11.9; 72 -12.0; 79 -12.1; 87 -12.2; 96 -12.4; 106 -12.3; 116 -12.3; 128 -12.4; 141 -12.4; 155 -12.4; 170 -12.3; 187 -12.2; 206 -12.0; 227 -11.8; 249 -11.7; 274 -11.4; 302 -11.2; 332 -10.9; 365 -10.6; 402 -10.3; 442 -9.9; 486 -9.7; 535 -9.4; 588 -8.9; 647 -8.8; 712 -8.8; 783 -8.6; 861 -8.6; 947 -9.2; 1042 -9.9; 1146 -10.3; 1261 -10.4; 1387 -10.2; 1526 -9.4; 1678 -8.5; 1846 -7.0; 2031 -5.6; 2234 -4.6; 2457 -3.7; 2703 -4.0; 2973 -2.0; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technologies FLC8 GGBl GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 GGBl ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.3  | -4.6 dB |
| Peaking | 178 Hz  | 0.38 | -5.2 dB |
| Peaking | 1303 Hz | 1.79 | -4.1 dB |
| Peaking | 3621 Hz | 1.32 | 6.3 dB  |
| Peaking | 5748 Hz | 3.09 | 4.4 dB  |
| Peaking | 2228 Hz | 7.3  | 0.8 dB  |
| Peaking | 7838 Hz | 7.74 | -1.3 dB |
| Peaking | 9508 Hz | 3.11 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20GGBl/FLC%20Technologies%20FLC8%20GGBl.png)