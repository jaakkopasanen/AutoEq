# Ultrasone Signature Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.6; 25 -5.4; 28 -6.3; 31 -7.1; 34 -7.6; 37 -8.1; 41 -8.5; 45 -8.9; 49 -9.1; 54 -9.3; 60 -9.5; 66 -9.5; 72 -9.0; 79 -8.2; 87 -9.1; 96 -10.4; 106 -10.6; 116 -9.8; 128 -10.5; 141 -11.4; 155 -11.6; 170 -10.7; 187 -11.5; 206 -11.5; 227 -11.3; 249 -11.1; 274 -10.4; 302 -10.0; 332 -9.6; 365 -9.4; 402 -9.4; 442 -9.5; 486 -9.8; 535 -10.0; 588 -10.0; 647 -10.0; 712 -9.9; 783 -9.6; 861 -9.5; 947 -9.0; 1042 -8.1; 1146 -7.5; 1261 -7.7; 1387 -8.2; 1526 -7.8; 1678 -6.3; 1846 -5.6; 2031 -4.6; 2234 -1.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.2; 3597 -2.2; 3957 -2.8; 4353 -2.6; 4788 -3.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.4; 10263 -11.0; 11289 -11.6; 12418 -10.3; 13660 -7.1; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Signature Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Signature Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 171 Hz   | 1.24 | -1.9 dB |
| Peaking | 402 Hz   | 0.12 | -3.3 dB |
| Peaking | 2731 Hz  | 1.4  | 8.2 dB  |
| Peaking | 5804 Hz  | 2.26 | 6.3 dB  |
| Peaking | 11033 Hz | 2.21 | -6.0 dB |
| Peaking | 20 Hz    | 1.7  | 3.9 dB  |
| Peaking | 48 Hz    | 2.05 | -1.2 dB |
| Peaking | 375 Hz   | 3.49 | 0.8 dB  |
| Peaking | 658 Hz   | 3.1  | -0.6 dB |
| Peaking | 14421 Hz | 5.34 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Signature%20Pro/Ultrasone%20Signature%20Pro.png)