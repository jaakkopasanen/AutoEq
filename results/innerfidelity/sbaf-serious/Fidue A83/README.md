# Fidue A83
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.3; 25 -6.6; 28 -6.9; 31 -7.2; 34 -7.5; 37 -7.6; 41 -7.8; 45 -8.1; 49 -8.3; 54 -8.5; 60 -8.8; 66 -9.1; 72 -9.4; 79 -9.6; 87 -9.9; 96 -10.2; 106 -10.3; 116 -10.3; 128 -10.5; 141 -10.5; 155 -10.4; 170 -10.3; 187 -10.1; 206 -9.9; 227 -9.5; 249 -9.1; 274 -8.7; 302 -8.2; 332 -7.7; 365 -7.3; 402 -6.7; 442 -6.0; 486 -5.8; 535 -4.5; 588 -4.0; 647 -3.7; 712 -3.7; 783 -3.5; 861 -3.8; 947 -4.3; 1042 -5.1; 1146 -6.0; 1261 -7.3; 1387 -9.2; 1526 -11.0; 1678 -12.0; 1846 -11.6; 2031 -10.2; 2234 -9.1; 2457 -8.6; 2703 -9.2; 2973 -7.2; 3270 -2.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.5; 7010 -7.5; 7711 -13.0; 8482 -15.2; 9330 -13.4; 10263 -8.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A83 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A83 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 147 Hz  | 0.46 | -4.3 dB  |
| Peaking | 891 Hz  | 0.7  | 7.6 dB   |
| Peaking | 1805 Hz | 0.73 | -11.8 dB |
| Peaking | 5098 Hz | 0.65 | 12.1 dB  |
| Peaking | 8317 Hz | 2.1  | -16.1 dB |
| Peaking | 18 Hz   | 1.48 | 1.0 dB   |
| Peaking | 2253 Hz | 4.44 | 1.8 dB   |
| Peaking | 2856 Hz | 3.8  | -3.6 dB  |
| Peaking | 3419 Hz | 4.07 | 3.5 dB   |
| Peaking | 4707 Hz | 6.01 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.3 dB |
| Peaking | 4000 Hz  | 1.41 | 10.3 dB |
| Peaking | 8000 Hz  | 1.41 | -6.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A83/Fidue%20A83.png)