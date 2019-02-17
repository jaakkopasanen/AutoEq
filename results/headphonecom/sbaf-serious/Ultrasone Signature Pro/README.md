# Ultrasone Signature Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.1; 25 -7.5; 28 -8.1; 31 -8.5; 34 -8.9; 37 -9.2; 41 -9.5; 45 -9.8; 49 -10.0; 54 -10.1; 60 -10.1; 66 -10.1; 72 -9.0; 79 -7.0; 87 -9.3; 96 -11.9; 106 -13.0; 116 -12.5; 128 -12.8; 141 -13.7; 155 -13.5; 170 -11.8; 187 -12.5; 206 -11.4; 227 -10.0; 249 -8.5; 274 -7.3; 302 -6.6; 332 -6.5; 365 -6.6; 402 -6.7; 442 -7.1; 486 -7.5; 535 -7.6; 588 -7.6; 647 -7.5; 712 -7.1; 783 -7.2; 861 -7.1; 947 -6.9; 1042 -6.2; 1146 -5.5; 1261 -6.1; 1387 -7.0; 1526 -7.3; 1678 -6.3; 1846 -4.3; 2031 -2.9; 2234 -1.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.6; 3597 -0.9; 3957 -0.9; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -5.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -10.1; 10263 -11.1; 11289 -10.7; 12418 -10.1; 13660 -8.1; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Signature Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Signature Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 1.45 | -3.1 dB |
| Peaking | 141 Hz   | 1.23 | -7.2 dB |
| Peaking | 1465 Hz  | 0.72 | -5.8 dB |
| Peaking | 2981 Hz  | 0.43 | 9.0 dB  |
| Peaking | 10462 Hz | 1.4  | -7.2 dB |
| Peaking | 167 Hz   | 5.52 | 1.8 dB  |
| Peaking | 194 Hz   | 2.84 | -2.0 dB |
| Peaking | 310 Hz   | 1.67 | 2.3 dB  |
| Peaking | 517 Hz   | 0.55 | -1.0 dB |
| Peaking | 1115 Hz  | 4.92 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20Signature%20Pro/Ultrasone%20Signature%20Pro.png)