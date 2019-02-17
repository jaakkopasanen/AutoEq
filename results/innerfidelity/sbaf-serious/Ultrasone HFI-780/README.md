# Ultrasone HFI-780
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -0.9; 72 -1.0; 79 -0.8; 87 -1.1; 96 -1.5; 106 -1.5; 116 -1.4; 128 -1.2; 141 -1.2; 155 -1.0; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.8; 249 -2.6; 274 -3.8; 302 -5.4; 332 -6.7; 365 -7.5; 402 -7.7; 442 -7.3; 486 -7.0; 535 -6.6; 588 -6.0; 647 -5.8; 712 -5.9; 783 -5.8; 861 -6.1; 947 -6.4; 1042 -6.4; 1146 -6.3; 1261 -6.7; 1387 -7.5; 1526 -8.7; 1678 -9.4; 1846 -9.6; 2031 -8.0; 2234 -2.8; 2457 -0.6; 2703 -2.9; 2973 -3.0; 3270 -4.8; 3597 -5.3; 3957 -4.1; 4353 -4.4; 4788 -5.2; 5267 -3.7; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.0; 10263 -8.8; 11289 -8.2; 12418 -8.0; 13660 -6.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-780 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-780 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.33 | 6.3 dB  |
| Peaking | 188 Hz   | 1.99 | 4.6 dB  |
| Peaking | 1912 Hz  | 2.34 | -7.8 dB |
| Peaking | 2372 Hz  | 2.27 | 9.1 dB  |
| Peaking | 6033 Hz  | 4.22 | 6.3 dB  |
| Peaking | 12 Hz    | 2.54 | 0.7 dB  |
| Peaking | 377 Hz   | 0.83 | 2.7 dB  |
| Peaking | 387 Hz   | 1.68 | -5.1 dB |
| Peaking | 9095 Hz  | 0.79 | 1.5 dB  |
| Peaking | 10325 Hz | 1.48 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | 4.7 dB  |
| Peaking | 250 Hz   | 1.41 | 3.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20HFI-780/Ultrasone%20HFI-780.png)