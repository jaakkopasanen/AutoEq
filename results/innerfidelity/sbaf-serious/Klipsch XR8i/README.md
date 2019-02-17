# Klipsch XR8i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -13.7; 25 -13.8; 28 -13.9; 31 -13.8; 34 -13.8; 37 -13.8; 41 -13.7; 45 -13.7; 49 -13.6; 54 -13.5; 60 -13.5; 66 -13.5; 72 -13.4; 79 -13.4; 87 -13.4; 96 -13.4; 106 -13.2; 116 -12.9; 128 -12.8; 141 -12.5; 155 -12.3; 170 -12.0; 187 -11.6; 206 -11.2; 227 -10.7; 249 -10.5; 274 -10.1; 302 -9.7; 332 -9.2; 365 -8.8; 402 -8.4; 442 -7.9; 486 -7.7; 535 -7.3; 588 -6.6; 647 -6.3; 712 -6.3; 783 -6.0; 861 -6.1; 947 -6.3; 1042 -6.5; 1146 -6.7; 1261 -7.0; 1387 -7.5; 1526 -7.9; 1678 -8.0; 1846 -7.9; 2031 -7.7; 2234 -7.6; 2457 -7.1; 2703 -6.5; 2973 -4.8; 3270 -2.4; 3597 -1.1; 3957 -1.4; 4353 -3.0; 4788 -2.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch XR8i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch XR8i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.13 | -7.3 dB |
| Peaking | 801 Hz  | 0.76 | 2.6 dB  |
| Peaking | 2818 Hz | 0.35 | -3.2 dB |
| Peaking | 3568 Hz | 2.37 | 7.2 dB  |
| Peaking | 5744 Hz | 2.17 | 7.9 dB  |
| Peaking | 6613 Hz | 9.68 | 1.2 dB  |
| Peaking | 7574 Hz | 5.46 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20XR8i/Klipsch%20XR8i.png)