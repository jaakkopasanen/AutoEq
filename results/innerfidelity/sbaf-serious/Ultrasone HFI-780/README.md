# Ultrasone HFI-780
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.4; 45 -2.0; 49 -2.4; 54 -2.8; 60 -3.1; 66 -3.3; 72 -3.4; 79 -3.2; 87 -3.5; 96 -3.9; 106 -3.9; 116 -3.7; 128 -3.6; 141 -3.6; 155 -3.3; 170 -2.7; 187 -2.6; 206 -2.8; 227 -3.2; 249 -5.0; 274 -6.2; 302 -7.8; 332 -9.0; 365 -9.8; 402 -10.1; 442 -9.7; 486 -9.4; 535 -9.0; 588 -8.4; 647 -8.2; 712 -8.3; 783 -8.1; 861 -8.5; 947 -8.8; 1042 -8.8; 1146 -8.7; 1261 -9.1; 1387 -9.9; 1526 -11.1; 1678 -11.7; 1846 -12.0; 2031 -10.4; 2234 -5.1; 2457 -1.8; 2703 -5.3; 2973 -5.3; 3270 -7.2; 3597 -7.7; 3957 -6.5; 4353 -6.8; 4788 -7.6; 5267 -6.1; 5793 -1.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -10.4; 10263 -11.2; 11289 -10.6; 12418 -10.4; 13660 -9.1; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-780 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-780 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.17 | 6.1 dB  |
| Peaking | 192 Hz   | 1.57 | 5.7 dB  |
| Peaking | 477 Hz   | 0.27 | -3.4 dB |
| Peaking | 6286 Hz  | 3.96 | 7.1 dB  |
| Peaking | 10896 Hz | 1.57 | -5.1 dB |
| Peaking | 388 Hz   | 2.08 | -2.8 dB |
| Peaking | 623 Hz   | 0.55 | 1.8 dB  |
| Peaking | 1915 Hz  | 2.02 | -6.6 dB |
| Peaking | 2361 Hz  | 4.42 | 9.9 dB  |
| Peaking | 4789 Hz  | 7.56 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | 2.9 dB  |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | -3.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20HFI-780/Ultrasone%20HFI-780.png)