# Ultrasone HFI-450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.9; 66 -2.1; 72 -3.2; 79 -4.3; 87 -4.8; 96 -5.3; 106 -6.2; 116 -6.5; 128 -6.7; 141 -6.6; 155 -6.6; 170 -5.9; 187 -6.2; 206 -6.2; 227 -6.5; 249 -7.0; 274 -7.8; 302 -9.0; 332 -9.7; 365 -9.9; 402 -9.8; 442 -9.7; 486 -9.6; 535 -9.3; 588 -8.3; 647 -7.9; 712 -7.9; 783 -7.7; 861 -7.9; 947 -8.1; 1042 -8.1; 1146 -8.3; 1261 -8.4; 1387 -8.2; 1526 -8.8; 1678 -8.6; 1846 -8.6; 2031 -7.6; 2234 -6.6; 2457 -5.2; 2703 -3.9; 2973 -3.8; 3270 -3.6; 3597 -3.4; 3957 -0.5; 4353 -1.1; 4788 -6.7; 5267 -7.0; 5793 -1.1; 6373 -1.0; 7010 -4.6; 7711 -6.2; 8482 -7.3; 9330 -9.1; 10263 -8.8; 11289 -7.9; 12418 -7.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.59 | 6.8 dB  |
| Peaking | 582 Hz  | 0.31 | -2.4 dB |
| Peaking | 3735 Hz | 2.16 | 5.4 dB  |
| Peaking | 6204 Hz | 6.24 | 6.2 dB  |
| Peaking | 9871 Hz | 2.5  | -3.0 dB |
| Peaking | 226 Hz  | 1.37 | 5.2 dB  |
| Peaking | 294 Hz  | 0.65 | -5.4 dB |
| Peaking | 1004 Hz | 0.33 | 3.3 dB  |
| Peaking | 1577 Hz | 1.15 | -3.6 dB |
| Peaking | 4994 Hz | 8.25 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20HFI-450/Ultrasone%20HFI-450.png)